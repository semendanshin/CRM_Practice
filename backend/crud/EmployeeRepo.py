from .CrudFactory import CrudFactory
from db.models import Employee

from schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse


class EmployeeRepo(
    CrudFactory(
        Employee,
        EmployeeCreate,
        EmployeeUpdate,
        EmployeeResponse
    )
):
    pass
