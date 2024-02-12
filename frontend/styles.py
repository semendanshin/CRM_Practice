import os.path


class Fonts:
    preconnect: str = '<link rel="preconnect" href="https://fonts.googleapis.com"> ' \
                      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    link: str = '<link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500;600;700&display=swap" rel="stylesheet">'

    @classmethod
    def get_fonts(cls):
        return f"{cls.preconnect}\n{cls.link}"


class Style:
    dir: str = 'styles'
    file: str = 'base_styles.css'

    def __init__(self):
        self.path = os.path.join(self.dir, self.file)

    @classmethod
    def path(cls):
        return cls().path

    @classmethod
    def get_styles(cls):
        with open(cls.path(), 'rt', encoding='utf-8') as styles:
            return f"""<style>{styles.read()}</style>"""


class SubpageStyle(Style):
    file = 'subpage_styles.css'


def add_styles(ui, *args) -> None:
    ui.add_head_html(
        Fonts.get_fonts()
    )

    for style in args:
        ui.add_head_html(
            style.get_styles()
        )
