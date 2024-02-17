from frontend.components import BaseIcon


class OverviewIcon(BaseIcon):
    img_url = 'static/overview.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class StorageIcon(BaseIcon):
    img_url = 'static/storage.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class EmployeesIcon(BaseIcon):
    img_url = 'static/employees.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class CustomersIcon(BaseIcon):
    img_url = 'static/customers.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class Applicationcon(BaseIcon):
    img_url = 'static/application.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class SettingsIcon(BaseIcon):
    img_url = 'static/settings.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class InstructionIcon(BaseIcon):
    img_url = 'static/instruction.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class SearchIcon(BaseIcon):
    img_url = 'static/search.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class ProfileIcon(BaseIcon):
    img_url = 'static/profile.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)


class FlagIcon(BaseIcon):
    img_url = 'static/flag.png'

    def __init__(self):
        super().__init__(image_name=self.img_url)
