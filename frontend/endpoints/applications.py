from nicegui import app, ui

from nicegui import APIRouter

from components import SideMenuButtonIcon, BaseLabel, SideMenuOption, BaseInput, CRMNameLabel, IconWithLink, BaseDiv, \
    BaseIcon, default_page_template
from styles import add_styles, Style, ApplicationStyle

router = APIRouter(prefix='/application')


@router.page('')
def employees_page() -> None:
    add_styles(ui, Style, ApplicationStyle)

    with default_page_template(
        title="APPLICATION",
        user_name="User Name",
        user_role="Администратор",
        show_search=False,
    ):
        ...

