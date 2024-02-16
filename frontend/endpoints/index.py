from nicegui import app, ui

from nicegui import APIRouter

from frontend.components import CRMNameLabel, BaseLabel, SideMenuOption, BaseIcon, BaseInput, BaseDiv, SideButton, \
    IconWithLink
from frontend.styles import Style, Fonts, add_styles, IndexStyle

router = APIRouter()


@router.page('/')
def main_page() -> None:
    add_styles(ui, Style, IndexStyle)

    with BaseDiv().classes(add='center-container'):

        with BaseDiv().classes(add='index-container'):
            with BaseDiv().classes(add='options-container'):
                CRMNameLabel()
                SideMenuOption(image_name='static/overview.png', button_text='Overview', button_href='/')
                SideMenuOption(image_name='static/storage.png', button_text='Объекты и склады', button_href='/storage')
                SideMenuOption(image_name='static/customers.png', button_text='Сотрудники', button_href='/employees')
                SideMenuOption(image_name='static/employees.png', button_text='Клиенты', button_href='/customers')
                SideMenuOption(image_name='static/application.png', button_text='Заявки', button_href='/application')

            with BaseDiv().classes(add='options-container'):
                SideButton(button_text='Новое добавление')
                SideMenuOption(image_name='static/settings.png', button_text='Настройки')
                SideMenuOption(image_name='static/instruction.png', button_text='Инструкции')

        with BaseDiv().classes(add='center-container'):
            with BaseDiv().classes(add='index-container'):
                with BaseDiv():
                    BaseLabel('Overview').classes(add='one')

                with BaseDiv():
                    BaseLabel('Task Tracker')

                with BaseDiv().classes(add='center-container'):
                    with BaseDiv().classes(add='index-container'):
                        with BaseDiv():
                            BaseLabel('Просрочены')
                        IconWithLink(target='', image_name='static/plus.png')
                        with BaseDiv().classes(add='task-container'):
                            BaseLabel('#Содержание таски')
                            with BaseDiv().classes(add='center-container'):
                                with BaseDiv().classes(add='index-container'):
                                    BaseLabel('Сотрудник')
                                    BaseLabel('Name сотрудника')
                                with BaseDiv().classes(add='index-container'):
                                    BaseLabel('Дедлайн')
                                    BaseLabel('02.02.2024')

            with BaseDiv():
                SideMenuOption(image_name='static/profile.png', button_text='Name пользователя')
                SideMenuOption(image_name='static/flag.png', button_text='Администратор')
                BaseInput('Искать сотрудника, клиетна, прочее').on('keydown.enter')
