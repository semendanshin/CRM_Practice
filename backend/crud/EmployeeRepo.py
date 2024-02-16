from .CrudFactory import CrudFactory
from db.models import Employee

from schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse


class EmployeeRepo(
    CrudFactory(
        Employee,
        EmployeeUpdate,
        EmployeeCreate,
        EmployeeResponse
    )
):
    pass
