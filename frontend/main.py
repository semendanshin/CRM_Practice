from pprint import pprint

from nicegui import ui, app, core

from config import STORAGE_SECRET
from middlewares import AuthMiddleware

from frontend.endpoints import index_router, auth_router, subpage_router


app.add_middleware(AuthMiddleware)

app.include_router(index_router)
app.include_router(auth_router)
app.include_router(subpage_router)

ui.run(storage_secret=STORAGE_SECRET, show=False, port=8000)

pprint(core.app.routes)

# if new tab shouldn't be opened after run:
# ui.run(show=False)

# to specify port
# ui.run(port=5050)
