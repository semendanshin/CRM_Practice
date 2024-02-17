import contextlib

from nicegui import APIRouter
from nicegui import ui

from components import BaseLabel, BaseInput, CRMNameLabel, IconWithLink, BaseDiv, \
    BaseIcon
from components.base_page import default_page_template
from styles import add_styles, Style, EmployeesStyle

router = APIRouter(prefix='/employees')


@router.page('')
def employees_page() -> None:
    with default_page_template(
            title="EMPLOYEE",
            user_name="User Name",
            user_role="Администратор",
    ):
        with BaseDiv().classes(add='evenly-spaced-column-container gap-flex-elements').style(
                "justify-content: flex-start;"):
            for _ in range(422):
                with BaseDiv().classes(add='evenly-spaced-container'):  # User row
                    with BaseDiv().classes(add='vertical-option-container'):  # Name
                        BaseLabel("Даньшин Семён").classes(add='label-with-background')
                    with BaseDiv().classes(add='vertical-option-container'):
                        with BaseDiv().classes(add='evenly-spaced-column-container'):  # Position
                            with BaseDiv().classes():  # Pos
                                BaseLabel("Pos").style('color: #7E7A7A;')
                            with BaseDiv().classes():  # Pos name
                                BaseLabel("Senior Pomidor")
                    with BaseDiv().classes(add='vertical-option-container'):
                        with BaseDiv().classes(add='evenly-spaced-column-container'):  # Phone
                            with BaseDiv().classes():  # Phone text
                                BaseLabel("Telephone").style('color: #7E7A7A;')
                            with BaseDiv().classes():  # phone number
                                BaseLabel("8 (800) 555-35-35")
