from typing import Optional

from fastapi.responses import RedirectResponse

from nicegui import APIRouter

from nicegui import app, ui
from frontend.config import passwords

router = APIRouter(prefix='/login')


@router.page('')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            # app.storage.user: individual dictionary for user (persisted)
            # for more details jump to definition (ctrl/cmd + click) or see docs on
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.open(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    ui.card().classes(add='container')
    username = ui.input('Username').on('keydown.enter', try_login)
    password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
    ui.button('Sign in', on_click=try_login, color='#D9CDC4').classes(add='container')#.style('border: 1px solid black; border-radius: 12px; text-transform: none; flex-direction: row; align-items: center; weidth: 500%;')
    return None