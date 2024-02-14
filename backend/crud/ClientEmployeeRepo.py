from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ClientEmployee
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(ClientEmployee)):
    @classmethod
    async def get_client_employee_by_id(cls, session: AsyncSession, record_id: int) -> "ClientEmployee":
        res = await session.execute(select(cls.ClientEmployee).where(ClientEmployee.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_client_employees(cls, session: AsyncSession) -> "ClientEmployee":
        res = await session.execute(select(cls.ClientEmployee))
        return res.scalar().all()

    @classmethod
    async def create_client_employee(cls, session: AsyncSession, **kwargs) -> "ClientEmployee":
        instance = cls.ClientEmployee(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_client_employee(cls, session: AsyncSession, client_employee_id: int):
        res = await session.execute(select(ClientEmployee).where(ClientEmployee.id == client_employee_id))
        client_employee_to_delete = res.scalar_one()
        await session.delete(client_employee_to_delete)
        await session.commit()
