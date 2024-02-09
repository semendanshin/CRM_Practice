import os.path


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
