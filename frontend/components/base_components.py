from typing import Callable

from nicegui import ui

from fastapi.responses import RedirectResponse


class BaseLabel(ui.label):
    def __init__(self, text: str = ''):  # get all super().__init__() args to pass them
        super().__init__(text)

        self.tag = 'label'  # specify tag for class instances


class CRMNameLabel(BaseLabel):
    def __init__(self):
        self.label_text = 'Название CRM'
        super().__init__(self.label_text)


class BaseButton(ui.button):
    def __init__(self, text: str = '', on_click: Callable = None, color: str = None, ):
        super().__init__(text, on_click=on_click, color=color)
        self.tag = 'button'
        self._text = text
        self.props(add=f'value="{text}"')


class BaseInput(ui.input):
    def __init__(self, placeholder: str = ''):
        super().__init__(placeholder=placeholder)
        self.tag = 'input'


class BaseDiv(ui.element):
    def __init__(self):
        super().__init__('div')


class BaseIcon(ui.image):
    def __init__(self, image_name: str):
        super().__init__(image_name)

        self.tag = 'img'


class SideMenuOption:
    def __init__(self, image_name: str, button_text: str, button_href: str = ''):
        with BaseDiv():
            BaseIcon(image_name)
            BaseButton(button_text, on_click=lambda: ui.open(button_href)).classes(add='button')


class SideMenuButtonIcon(BaseIcon):
    def __init__(self, image_name: str):
        with BaseDiv():
            BaseIcon(image_name)

class BaseLink(ui.link):
    def __init__(self, target: str):
        super().__init__(target=target)


class IconWithLink:
    def __init__(self, target: str, image_name):

        with BaseDiv():
            with BaseLink(target=target):
                BaseIcon(image_name=image_name)
