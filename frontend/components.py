from typing import Callable

from nicegui import ui


class BaseLabel(ui.label):
    def __init__(self, text: str = ''):  # get all super().__init__() args to pass them
        super().__init__(text)

        self.tag = 'label'  # specify tag for class instances


class CRMNameLabel(BaseLabel):
    def __init__(self):
        self.label_text = 'Название CRM'
        super().__init__(self.label_text)


# class Font(ui.textarea):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.

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


class BaseInput(ui.input):
    def __init__(self, placeholder: str = ''):
        super().__init__(placeholder=placeholder)
        self.tag = 'input'
