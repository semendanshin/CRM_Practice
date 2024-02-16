from nicegui import app, ui

from nicegui import APIRouter

from components import SideMenuButtonIcon, BaseLabel, SideMenuOption, BaseInput, CRMNameLabel, IconWithLink
from styles import add_styles, Style, CustomersStyle

router = APIRouter(prefix='/customers')


@router.page('/')
def customers_page() -> None:
    add_styles(ui, Style, CustomersStyle)

    with ui.element('div'):
        with ui.element('div'):
            CRMNameLabel()

    with ui.element('div'):
        IconWithLink(target='/', image_name='static/overview.png')
        IconWithLink(target='/storage', image_name='static/storage.png')
        IconWithLink(target='/employees', image_name='static/employees.png')
        IconWithLink(target='/customers', image_name='static/customers.png')
        IconWithLink(target='/application', image_name='static/application.png')

    with ui.element('div'):
        IconWithLink(target='', image_name='static/settings.png')
        IconWithLink(target='', image_name='static/instruction.png')

    with ui.element('div'):
        BaseLabel('Customers')
        SideMenuOption(image_name='', button_text='Name пользователя')
        BaseInput('Search customers').on('keydown.enter')
