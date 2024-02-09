from .AbstractRepo import AbstractRepo
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Employee


class EmployeeRepo(AbstractRepo):
    model = Employee

    @classmethod
    def get_by_id(cls, session, id):
        pass
