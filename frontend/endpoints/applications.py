from nicegui import APIRouter
from nicegui import ui

from components import BaseLabel, BaseDiv, \
    default_page_template, BaseCard
from styles import add_styles, Style, ApplicationStyle

router = APIRouter(prefix='/application')

statuses = [
    ("Зарегистрирован", "#92DAAB"),
    ("В работе", "#E7E79B"),
    ("На выезде", "#E8C197"),
    ("У клиента, в работе", "#E7E094"),
    ("ООК", "#D6E899"),
    ("ОТДС", "#BC8FE8"),
    ("Поставка", "#E6B7E7"),
    ("Оплата", "#8FE8E8"),
    ("Выполнен", "#8FE88F"),
    ("Отменен", "#8F8F8F"),
]


@router.page('')
def employees_page() -> None:
    add_styles(ui, Style, ApplicationStyle)

    with (default_page_template(
            title="APPLICATION",
            user_name="User Name",
            user_role="Администратор",
            show_search=False,
    )):
        with BaseDiv().classes(add='evenly-spaced-column-container gap-flex-elements').style(
                "justify-content: flex-start;"):
            with BaseDiv().classes(add='evenly-spaced-container').style(
                    ("justify-content: space-evenly;flex-wrap: wrap;align-content: left;overflow: auto;max-height: 100%;"
                     "row-gap: 10px;column-gap: 10px;max-width: 100%;")
            ):
                for status, color in statuses:
                    with BaseDiv().classes(add='evenly-spaced-column-container'
                                           ).style(
                        "min-width: 100;justify-content: space-around;height: fit-content;gap: 10px;max-height: 40%;"
                    ):
                        with BaseDiv().style('height: auto;display: contents;'):
                            BaseLabel(status).classes(add='label-with-background').style(f'background-color: {color};')
                        with BaseDiv().style('height: auto;display: contents;'):
                            ui.separator()
                        with BaseDiv().classes(add='evenly-spaced-column-container').style(
                                'justify-content: space-around;overflow: hidden;max-height: 40%;'):
                            with BaseDiv().classes(add='evenly-spaced-column-container').style(
                                    'justify-content: flex-start;overflow: auto;gap: 10px;max-height: 40%;'):
                                for _ in range(50):
                                    with BaseCard():
                                        with BaseDiv().classes(add='evenly-spaced-container'):
                                            BaseLabel("Заявка № 123").style('font-size: 90%;')
                                            BaseLabel("12.12.2021").style('font-size: 90%;')
                                        with BaseDiv().classes(add='evenly-spaced-container'):
                                            BaseLabel("Клиент:").style('font-size: 90%;')
                                            BaseLabel("Клиент").style('font-size: 90%;')
                        with BaseDiv().style('height: auto;display: contents;'):
                            ui.separator()