from nicegui import app, ui

from nicegui import APIRouter

from frontend.components import SideMenuButtonIcon, BaseLabel, SideMenuOption, BaseInput, CRMNameLabel, IconWithLink
from frontend.styles import add_styles, Style, ApplicationStyle

router = APIRouter(prefix='/application')


@router.page('/')
def application_page() -> None:
    add_styles(ui, Style, ApplicationStyle)

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