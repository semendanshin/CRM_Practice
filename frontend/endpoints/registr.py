from typing import Optional

from fastapi.responses import RedirectResponse

from nicegui import APIRouter

from nicegui import app, ui

from frontend.components import BaseButton, BaseInput, BaseLabel, CRMNameLabel, BaseDiv, BaseLine, BaseSelect, Select, \
    BaseLink
from frontend.config import passwords
from frontend.styles import SubpageStyle, add_styles, AuthStyle, RegistrStyle

router = APIRouter(prefix='/signup')

@router.page('')
def signup() -> Optional[RedirectResponse]:
    def try_signup() -> None:
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.open(app.storage.user.get('referrer_path', '/'))
        else:
            ui.notify('Wrong username or password', color='negative')
    add_styles(ui, SubpageStyle, RegistrStyle)

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')

    CRMNameLabel()

    BaseLine().classes(add='create-line')
    with ui.element('div').classes(add='login-container'):
        with BaseDiv().classes(add='login-child'):
            BaseLabel(text='Sign up').classes(add='label').style('font-weight: 700;')
            BaseLabel(text='Enter your email and password').classes(add='label').style('color: #C0C0C0;')
        BaseLabel(text='Email').classes(add='label').style('align-self: left;')
        username = BaseInput('Email address').on('keydown.enter', try_signup).props(add="standout style=\"border-radius: 10px\"")
        BaseLabel(text='Password').classes(add='label').style('align-items: flex-start !important;')
        password = BaseInput('Password').on('keydown.enter', try_signup).props(add="standout style=\"border-radius: 10px\"")
        BaseLabel(text='What is your role?').classes(add='label').style('align-items: flex-start !important;')
    #     Select(options= ['Admin', 'Manager', 'User'], label='Select a role').classes(add='select').props(add="standout style=\"border-radius: 10px\"").style(add="""height: 30px;
    # width: 100%;
    # box-shadow: inset 0px 5px 10px 0px rgba(0, 0, 0, 0.25);
    # border: 0.5px solid coral;
    # background-color: #DCDCDC;
    # text-indent: 10px;
    # flex-grow: 0;
    # flex-shrink: 1;""")
        select = Select()
        select.set_options(['Select a role', 'Admin', 'Manager', 'User'])

        BaseLink(text='Do you already have an account? Sign in', target='/login')
        BaseButton(text='Sign up', on_click=try_signup, color='#FFEFD5').classes(add='button')
    return None
