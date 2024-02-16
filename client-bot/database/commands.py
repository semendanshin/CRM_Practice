from .models import User
from sqlalchemy.orm import Session
from sqlalchemy import select


def add_user(session: Session, telegram_id: int, access_token: str) -> None:
    if user := get_user(session=session, telegram_id=telegram_id):
        user.access_token = access_token
    else:
        user = User(telegram_id=telegram_id, access_token=access_token)
        session.add(user)
    session.commit()


def get_user(session: Session, telegram_id: int) -> User:
    stm = select(User).filter_by(telegram_id=telegram_id)
    result = session.execute(stm)  # выполнить
    return result.scalar()


def get_token(session: Session, telegram_id: int) -> str:
    user = get_user(session=session, telegram_id=telegram_id)
    return user.access_token
