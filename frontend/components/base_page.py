from contextlib import contextmanager

from nicegui import ui

from components import BaseDiv, CRMNameLabel, BaseLabel, BaseInput, BaseIcon, IconWithLink
from styles import Style, BasePageStyle, add_styles


@contextmanager
def default_page_template(
        title: str,
        user_name: str,
        user_role: str,
        style: Style = None,
        show_search: bool = True,
        *args,
) -> None:
    styles = [Style, BasePageStyle]
    if style:
        styles.append(style)
    add_styles(ui, *styles)

    with BaseDiv().style("width: 98vw; height: 82vh;position: absolute;top: 10px;right: 0;bottom: 0;left: 15px;max-height: 99vh;"):
        with BaseDiv().classes(add='index-container gap-flex-elements'):
            with BaseDiv().classes().style('display: flex'):  # Site name
                CRMNameLabel().style('align-self: flex-start;')

            ui.separator()

            with BaseDiv().classes(add='evenly-spaced-container').style("justify-content: space-between"):  # Header
                with BaseDiv().classes(add='vertical-option-container'):  # Employees text
                    BaseLabel(title).classes(add="page-name")
                if show_search:
                    with BaseDiv().classes(add='vertical-option-container full-width-element'):  # Input
                        BaseInput("Search employees").classes(add='input')
                with BaseDiv().classes(add='vertical-option-container'):
                    with BaseDiv().classes(add='center-container'):  # User
                        with BaseDiv().classes(add='index-container').style("justify-content: space-around;"):  # Name and role
                            with BaseDiv().classes():  # Name
                                BaseLabel(user_name)
                            with BaseDiv().classes(add='icon-text-container gap-flex-elements'):
                                BaseIcon('static/flag.png').classes(add='position-flag')
                                BaseLabel(user_role).classes()
                        with BaseDiv().classes():  # Picture
                            BaseIcon('static/profile.png').classes(add="profile-icon")

            ui.separator()

            with BaseDiv().classes(add='center-container').style("justify-content: space-around;"):  # Side + View
                with BaseDiv().classes(add='evenly-spaced-column-container').style("min-width: 100;"):  # Side menu
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

                    with BaseDiv().classes(add='options-container'):  # Bottom group

                        with BaseDiv().classes(add='option-container'):
                            IconWithLink(target='', image_name='static/settings.png')

                        with BaseDiv().classes(add='option-container'):
                            IconWithLink(target='', image_name='static/instruction.png')

                with BaseDiv().classes(add='index-container').style("overflow: hidden;max-height: 100%"):  # View port
                    yield
