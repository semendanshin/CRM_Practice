from nicegui import ui
from frontend.styles import SubpageStyle
from frontend.components import Label

from nicegui import APIRouter

router = APIRouter(prefix='/subpage')


@router.page('/label')
def label_page() -> None:
    ui.add_head_html(
        SubpageStyle.get_styles()  # styling endpoint with SubpageStyle.file css file
    )

    # ui.label('some text')  # if element shouldn't be styled by tag

    Label('This is a sub page.')  # if element should be styled by tag you should create custom class


@router.page('/link')
def link_page() -> None:
    ui.add_head_html(
        SubpageStyle.get_styles()  # styling endpoint with SubpageStyle.file css file
    )

    # ui.label('some text')  # if element shouldn't be styled by tag

    ui.link(text='check label test page',
            target='/subpage/label')  # if element should be styled by tag you should create custom class
