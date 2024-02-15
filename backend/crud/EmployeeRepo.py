from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Employee
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Employee)):
    @classmethod
    async def get_employee_by_id(cls, session: AsyncSession, record_id: int) -> "Employee":
        res = await session.execute(select(cls.Employee).where(Employee.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_employees(cls, session: AsyncSession) -> list["Employee"]:
        res = await session.execute(select(cls.Employee))
        return res.all()

    @classmethod
    async def create_employee(cls, session: AsyncSession, **kwargs) -> "Employee":
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_employee(cls, session: AsyncSession, employee_id: int):
        client_to_delete = await session.execute(select(Employee).where(Employee.id == employee_id))
        client_to_delete = client_to_delete.scalar_one()
        await session.delete(client_to_delete)
        await session.commit()




