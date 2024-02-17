from nicegui import app, ui

from nicegui import APIRouter

from components import SideMenuButtonIcon, BaseLabel, SideMenuOption, BaseInput, CRMNameLabel, IconWithLink, BaseDiv, \
    SideButton, BaseIcon
from styles import add_styles, Style, EmployeesStyle

router = APIRouter(prefix='/employees')


@router.page('/')
def employees_page() -> None:
    add_styles(ui, Style, EmployeesStyle)

    with BaseDiv().classes(add='index-container gap-flex-elements'):
        with BaseDiv().classes():  # Site name
            CRMNameLabel()
        with BaseDiv().classes(add='evenly-spaced-container').style("justify-content: space-between"):  # Header
            with BaseDiv().classes(add='vertical-option-container'):  # Employees text
                BaseLabel("EMPLOYEE").classes(add="page-name")
            with BaseDiv().classes(add='vertical-option-container full-width-element'):  # Input
                BaseInput("Search employees").classes(add='input')
            with BaseDiv().classes(add='vertical-option-container'):
                with BaseDiv().classes(add='center-container'):  # User
                    with BaseDiv().classes(add='index-container'):  # Name and role
                        with BaseDiv().classes():  # Name
                            BaseLabel("User Name")
                        with BaseDiv().classes(add='icon-text-container gap-flex-elements'):
                            BaseIcon('static/flag.png').classes(add='position-flag')
                            BaseLabel('Администратор').classes()
                    with BaseDiv().classes():  # Picture
                        BaseIcon('static/profile.png').classes(add="profile-icon")
        with BaseDiv().classes(add='center-container'):  # Side + View
            with BaseDiv().classes(add='evenly-spaced-column-container'):  # Side menu
                with BaseDiv().classes(add='options-container'):  # Top group
                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='/', image_name='static/overview.png')
                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='/storage', image_name='static/storage.png')
                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='/employees', image_name='static/employees.png')
                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='/customers', image_name='static/customers.png')
                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='/application', image_name='static/application.png')

                with BaseDiv().classes(add='options-container bottom-position'):  # Bottom group

                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='', image_name='static/settings.png')

                    with BaseDiv().classes(add='option-container'):
                        IconWithLink(target='', image_name='static/instruction.png')

            with BaseDiv().classes(add='index-container').style("overflow: hidden;"):  # View port
                with BaseDiv().classes(add='evenly-spaced-column-container gap-flex-elements'):
                    for _ in range(5):
                        with BaseDiv().classes(add='evenly-spaced-container'):  # User row
                            with BaseDiv().classes(add='vertical-option-container'):  # Name
                                BaseLabel("Даньшин Семён").classes(add='label-with-background')
                            with BaseDiv().classes(add='vertical-option-container'):
                                with BaseDiv().classes(add='evenly-spaced-column-container'):  # Position
                                    with BaseDiv().classes():  # Pos
                                        BaseLabel("Pos")
                                    with BaseDiv().classes():  # Pos name
                                        BaseLabel("Senior Pomidor")
                            with BaseDiv().classes(add='vertical-option-container'):
                                with BaseDiv().classes(add='evenly-spaced-column-container'):  # Phone
                                    with BaseDiv().classes():  # Phone text
                                        BaseLabel("Telephone")
                                    with BaseDiv().classes():  # phone number
                                        BaseLabel("8 (800) 555-35-35")
