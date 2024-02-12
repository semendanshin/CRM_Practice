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