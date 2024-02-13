from typing import Optional

from fastapi.responses import RedirectResponse

from nicegui import APIRouter

from nicegui import app, ui

from frontend.components import BaseButton, BaseInput, BaseLabel
from frontend.config import passwords
from frontend.styles import SubpageStyle, add_styles, AuthStyle

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

    add_styles(ui, SubpageStyle, AuthStyle)

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')

    #with ui.card()
    BaseLabel(text='НАЗВАНИЕ crm').style('align-item: left;')
    # with ui.element('div').classes(add='login-container'):
    with ui.element('div').classes(add='login-container'):
    # with ui.card().style(add="display: inline-flex;flex-direction: column;justify-content: center;"):
        BaseLabel(text='Sign in').classes(add='label').style('font-family: Montserrat Alternates; transform: translateY(-100px);')
        username = BaseInput('Email address').on('keydown.enter', try_login).props(add="standout style=\"border-radius: 10px\"")
        password = BaseInput('Password').on('keydown.enter', try_login).props(add="standout style=\"border-radius: 10px; transform: translateY(50px)\"")
        BaseButton(text='Sign in', on_click=try_login, color='#FFEFD5').classes(add='button').style('font-family: Montserrat Alternates;')
    return None