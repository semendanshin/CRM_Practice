from nicegui import app, ui

from nicegui import APIRouter

from frontend.components import CRMNameLabel, BaseLabel
from frontend.styles import Style, Fonts, add_styles

router = APIRouter()


@router.page('/')
def main_page() -> None:
    add_styles(ui, Style)

    with ui.element('div').classes(''):
        with ui.element('div').classes(''):
            CRMNameLabel()

        with ui.element('div').classes(''):
            BaseLabel('Overview').classes('')
            ui.label('Объекты и склады').classes()
            ui.label('Сотрудники').classes()
            ui.label('Клиенты').classes()
            ui.label('Заявки').classes()

        with ui.element('div').classes():
            ui.button('Новое добавление')
            ui.label('Настройки').classes()
            ui.label('Инструкции').classes()
