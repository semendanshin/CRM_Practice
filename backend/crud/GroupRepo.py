from .CrudFactory import CrudFactory
from db.models import Group

from schemas.group import GroupCreate, GroupUpdate, GroupResponse


class GroupRepo(
    CrudFactory(
        Group,
        GroupCreate,
        GroupUpdate,
        GroupResponse
    )
):
    pass
