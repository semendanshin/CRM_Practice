from nicegui import app, ui

from nicegui import APIRouter

from components import SideMenuButtonIcon, BaseLabel, SideMenuOption, BaseInput, CRMNameLabel, IconWithLink, BaseDiv, \
    BaseIcon
from styles import add_styles, Style, CustomersStyle

router = APIRouter(prefix='/customers')


@router.page('/')
def customers_page() -> None:
    add_styles(ui, Style, CustomersStyle)

    # with ui.element('div'):
    #     with ui.element('div'):
    #         CRMNameLabel()
    #
    # with ui.element('div'):
    #     IconWithLink(target='/', image_name='static/overview.png')
    #     IconWithLink(target='/storage', image_name='static/storage.png')
    #     IconWithLink(target='/employees', image_name='static/employees.png')
    #     IconWithLink(target='/customers', image_name='static/customers.png')
    #     IconWithLink(target='/application', image_name='static/application.png')
    #
    # with ui.element('div'):
    #     IconWithLink(target='', image_name='static/settings.png')
    #     IconWithLink(target='', image_name='static/instruction.png')
    #
    # with ui.element('div'):
    #     BaseLabel('Customers')
    #     SideMenuOption(image_name='', button_text='Name пользователя')
    #     BaseInput('Search customers').on('keydown.enter')
    with BaseDiv().classes(add='index-container gap-flex-elements'):
        with BaseDiv().classes():  # Site name
            CRMNameLabel()
            with BaseDiv().classes(add='evenly-spaced-container').style("justify-content: space-between"):  # Header
                with BaseDiv().classes(add='vertical-option-container'):  # Employees text
                    BaseLabel("CUSTOMERS").classes(add="page-name")
                with BaseDiv().classes(add='vertical-option-container full-width-element'):  # Input
                    BaseInput("Search customers").classes(add='input')
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

        with BaseDiv().classes(add='center-container').style('gap: 30px'):  # Side + View
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
                    with BaseDiv().classes(add='evenly-spaced-container').style('justify-content: flex-start; font-size: 200%'):  # User row
                        with BaseDiv().classes(add='vertical-option-container'):  # Name
                            BaseLabel("Клиент").classes(add='label-with-background').style('box-shadow: inset 0px 5px 10px 0px rgba(0, 0, 0, 0.25);border: 0.5px solid #7E7A7A;')
                    with BaseDiv().classes(add='evenly-spaced-container').style('justify-content: flex-start; font-size: 200%'):  # User row
                        with BaseDiv().classes(add='vertical-option-container'):  # Name
                            BaseLabel("Клиент").classes(add='label-with-background').style('box-shadow: inset 0px 5px 10px 0px rgba(0, 0, 0, 0.25);border: 0.5px solid #7E7A7A;')
                    with BaseDiv().classes(add='evenly-spaced-container').style('justify-content: flex-start; font-size: 200%'):  # User row
                        with BaseDiv().classes(add='vertical-option-container'):  # Name
                            BaseLabel("Клиент").classes(add='label-with-background').style('box-shadow: inset 0px 5px 10px 0px rgba(0, 0, 0, 0.25);border: 0.5px solid #7E7A7A;')
                    with BaseDiv().classes(add='evenly-spaced-container').style('justify-content: flex-start; font-size: 200%'):  # User row
                        with BaseDiv().classes(add='vertical-option-container'):  # Name
                            BaseLabel("Total Oleron").classes(add='label-with-background').style('box-shadow: inset 0px 5px 10px 0px rgba(0, 0, 0, 0.25);border: 0.5px solid #7E7A7A;')