from nicegui import app, ui

from nicegui import APIRouter

from frontend.components import CRMNameLabel, BaseLabel, SideMenuOption, BaseIcon
from frontend.styles import Style, Fonts, add_styles

router = APIRouter()


@router.page('/')
def main_page() -> None:
    add_styles(ui, Style)

    with ui.element('div'):
        with ui.element('div'):
            CRMNameLabel()

        with ui.element('div'):
            SideMenuOption(icon_name='', button_text='Overview')
            SideMenuOption(icon_name='', button_text='Объекты и склады')
            SideMenuOption(icon_name='', button_text='Сотрудники')
            SideMenuOption(icon_name='', button_text='Клиенты')
            SideMenuOption(icon_name='', button_text='Заявки')

        with ui.element('div'):
            SideMenuOption(icon_name='', button_text='Новое добавление')
            SideMenuOption(icon_name='', button_text='Настройки')
            SideMenuOption(icon_name='', button_text='Инструкции')
