from typing import Optional

from fastapi.responses import RedirectResponse

from nicegui import APIRouter

from nicegui import app, ui

from components import BaseButton, BaseInput, BaseLabel, CRMNameLabel, BaseDiv, BaseLine, BaseLink
from config import passwords, STORAGE_SECRET
from styles import SubpageStyle, add_styles, AuthStyle, RegistrStyle

router: APIRouter = APIRouter(prefix='/login')


@router.page('')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        print(222222222222222222)
        if passwords.get(username.value) == password.value:
            # app.storage.user: individual dictionary for user (persisted)
            # for more details jump to definition (ctrl/cmd + click) or see docs on
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.open(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            print(1111111111111111)
            print(username.value, password.value)
            ui.notify('Wrong username or password', color='negative')

    add_styles(ui, SubpageStyle, AuthStyle, RegistrStyle)

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')

    CRMNameLabel()
    BaseLine().classes(add='create-line')
    with ui.element('div').classes(add='login-container'):
        with BaseDiv().classes(add='login-child'):
            BaseLabel(text='Sign in').classes(add='label').style('font-weight: 700;')
            BaseLabel(text='Enter your email and password').classes(add='label').style('color: #C0C0C0;')
        BaseLabel(text='Email').classes(add='label').style('align-self: left;')
        username = BaseInput('Email address').on('keydown.enter', try_login).props(add="standout style=\"border-radius: 10px\"")
        BaseLabel(text='Password').classes(add='label').style('align-items: flex-start !important;')
        password = BaseInput('Password').on('keydown.enter', try_login).props(add="standout style=\"border-radius: 10px\"")
        BaseLink(text='New to НАЗВАНИЕ crm? Sign up', target='/signup')
        BaseButton(text='Sign in', on_click=try_login, color='#FFEFD5').classes(add='button')

    return None

