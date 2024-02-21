from nicegui import app, ui

from nicegui import APIRouter

from components import SideMenuButtonIcon, BaseLabel, SideMenuOption, BaseInput, CRMNameLabel, IconWithLink, \
    BaseDiv
from styles import add_styles, Style, StorageStyle

router = APIRouter(prefix='/storage')


@router.page('')
def storage_page() -> None:
    add_styles(ui, Style, StorageStyle)


    CRMNameLabel()
    with BaseDiv().classes(add='storage-container'):
        with BaseDiv().classes(add='icon'):

            IconWithLink(target='/', image_name='static/overview.png')
            IconWithLink(target='/storage', image_name='static/storage.png')
            IconWithLink(target='/customers', image_name='static/customers.png')
            IconWithLink(target='/employees', image_name='static/employees.png')
            IconWithLink(target='/applications', image_name='static/application.png')

        with BaseDiv():
            IconWithLink(target='', image_name='static/settings.png')
            IconWithLink(target='', image_name='static/instruction.png')
