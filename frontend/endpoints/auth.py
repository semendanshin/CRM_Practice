from typing import Optional

from fastapi.responses import RedirectResponse

from nicegui import APIRouter

from nicegui import app, ui
from nicegui.binding import BindableProperty

from components import BaseButton, BaseInput, BaseLabel, CRMNameLabel, BaseDiv, BaseLine, BaseLink
from config import passwords, STORAGE_SECRET
from styles import SubpageStyle, add_styles, AuthStyle, RegistrStyle

router: APIRouter = APIRouter(prefix='/login')


@router.page('')
def login() -> Optional[RedirectResponse]:
    # def try_login() -> None:  # local function to avoid passing username and password as arguments
    #     username_input = ui.label().bind_text_from(username, 'value')
    #     print(username_input)
    #     # username_value: BindableProperty = username.
    #     # password_value: BindableProperty = password.value
    #
    #     print(username_value, password_value)
    #
    #     if passwords.get(username.value) == password.value:
    #         # app.storage.user: individual dictionary for user (persisted)
    #         # for more details jump to definition (ctrl/cmd + click) or see docs on
    #         app.storage.user.update({'username': username.value, 'authenticated': True})
    #         ui.open(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
    #     else:
    #         print(username.value, password.value)
    #         ui.notify('Wrong username or password', color='negative')
    #
    # add_styles(ui, SubpageStyle, AuthStyle, RegistrStyle)
    #
    # if app.storage.user.get('authenticated', False):
    #     return RedirectResponse('/')
    #
    # CRMNameLabel()
    # BaseLine().classes(add='create-line')
    # with ui.element('div').classes(add='login-container'):
    #     with BaseDiv().classes(add='login-child'):
    #         BaseLabel(text='Sign in').classes(add='label').style('font-weight: 700;')
    #         BaseLabel(text='Enter your email and password').classes(add='label').style('color: #C0C0C0;')
    #     BaseLabel(text='Email').classes(add='label').style('align-self: left;')
    #     username = BaseInput('Email address').on('keydown.enter', try_login).props(add="standout style=\"border-radius: 10px\"")
    #     BaseLabel(text='Password').classes(add='label').style('align-items: flex-start !important;')
    #     password = BaseInput('Password').on('keydown.enter', try_login).props(add="standout style=\"border-radius: 10px\"")
    #     BaseLink(text='New to НАЗВАНИЕ crm? Sign up', target='/signup')
    #     BaseButton(text='Sign in', on_click=try_login, color='#FFEFD5').classes(add='button')
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.open(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    add_styles(ui, SubpageStyle, AuthStyle, RegistrStyle)

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')

    CRMNameLabel()
    BaseLine().classes(add='create-line')
    with (((ui.element('div').classes(add='login-container')))):
        with BaseDiv().classes(add='login-child'):
            BaseLabel(text='Sign in').classes(add='label').style('font-weight: 700;')
            BaseLabel(text='Enter your email and password').classes(add='label').style('color: #C0C0C0;')
        BaseLabel(text='Email').classes(add='label').style('align-self: left;')
        username = ui.input(label='Username').on('keydown.enter', try_login).props(
            add="standout style=\"border-radius: 10px\""
        ).classes(add="input")
        BaseLabel(text='Password').classes(add='label').style('align-items: flex-start !important;')
        password = ui.input('Password', password=True, password_toggle_button=True
                            ).on('keydown.enter', try_login
                                 ).props(add="standout style=\"border-radius: 10px; height: 30px !important; width: 100% !important; box-shadow: inset 0px 5px 10px 0px rgba(0, 0, 0, 0.25) !important; border: 0.5px solid coral !important; background-color: #DCDCDC !important; text-indent: 10px !important; flex-grow: 0 !important; flex-shrink: 1 !important;\""
                                         ).classes(add='input')

        BaseLink(text='New to НАЗВАНИЕ crm? Sign up', target='/signup')
        ui.button('Log in', on_click=try_login, color='#FFEFD5').classes(add='button')
    return None
