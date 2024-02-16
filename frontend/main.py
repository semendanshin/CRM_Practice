from pprint import pprint

from nicegui import ui, app, core

from config import STORAGE_SECRET
from middlewares import AuthMiddleware

from endpoints import index_router, auth_router, subpage_router, registr_router, storage_router, application_router, customers_router, employees_router




app.add_middleware(AuthMiddleware)

app.include_router(index_router)
app.include_router(auth_router)
app.include_router(subpage_router)
app.include_router(registr_router)
app.include_router(customers_router)
app.include_router(employees_router)
app.include_router(storage_router)
app.include_router(application_router)

app.add_static_files(url_path='/static', local_directory='static')

ui.run(storage_secret=STORAGE_SECRET, show=False, port=8060)


pprint(core.app.routes)

# if new tab shouldn't be opened after run:
# ui.run(show=False)

# to specify port
# ui.run(port=5050)
