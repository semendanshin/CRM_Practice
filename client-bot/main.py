import logging
import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, ConversationHandler
from telegram.ext.filters import TEXT

from sqlalchemy.orm import Session

from ticket_repo import tickets_collection, TicketCreate

from database.commands import add_user, get_user, get_token
# from database.commands import add_file, get_file_from_db, delete_file_from_db, get_files_to_list
from database import engine

from ticket_repo import tickets_collection

from config import TOKEN


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logging.getLogger('httpx').setLevel(logging.WARNING) #ЧТОБЫ ЛИШНЯЯ ИНФА НЕ ПЕЧАТАЛАСЬ


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="привет! этот бот создан для создания тикетов. "
                                        "По команде /ticket ты сможешь его добавить, "
                                        "а по команде /show посмотреть все свои тикеты! Если диалог завершен, напишите /cancel")
    if not context.args:
        await update.effective_message.reply_text("Простите, но вы не можете пользоваться ботом без токена.")
    
    token = context.args[0]
    telegram_id = update.effective_user.id
    
    logger.info(f"token is: {token}")
    with Session(engine) as session:
        add_user(session=session, telegram_id=telegram_id, access_token=token)


async def ask_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(text="Опиши свою проблему.")
    return "asked_ticket"


async def ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("tired")
    logger.critical(111111111111111111111111111111111111111111111111111)
    ticket_description = update.message.text
    with Session(engine) as session:
        token = get_token(session=session, telegram_id=update.effective_user.id)
    logger.info(f"got token {token}")
    ticket = TicketCreate(
        description=ticket_description,
        token=token,
    )
    logger.info(f"ticket object created {ticket}")
    await tickets_collection.create_ticket(ticket)
    await update.effective_message.reply_text("Тикет создан")
    return ConversationHandler.END


async def get_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with Session(engine) as session:
        user = get_user(session, update.effective_user.id)
    tickets = await tickets_collection.get_all(user.access_token)
    text = '\n\n'.join([f'{x.description}\n{x.status}' for x in tickets])
    await update.effective_message.reply_text(text)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "Диалог завершен"
    )
    return ConversationHandler.END


if __name__ == '__main__':
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    ticket_handler = ConversationHandler(
        entry_points=[CommandHandler('ticket', ask_ticket), ],
        states={
            "asked_ticket": [MessageHandler(filters=TEXT, callback=ticket)]
        },
        fallbacks=[
            CommandHandler('cancel', cancel)
        ]
    )
    application.add_handler(ticket_handler)
    
    get_tickets_handler = CommandHandler('show', get_tickets)
    application.add_handler(get_tickets_handler)

    application.run_polling()
