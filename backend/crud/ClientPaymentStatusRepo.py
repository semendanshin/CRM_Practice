from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ClientPaymentStatus
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(ClientPaymentStatus)):
    @classmethod
    async def get_client_payment_status_by_id(cls, session: AsyncSession, record_id: int) -> "ClientPaymentStatus":
        res = await session.execute(select(cls.ClientPaymentStatus).where(ClientPaymentStatus.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_client_payment_status(cls, session: AsyncSession) -> "ClientPaymentStatus":
        res = await session.execute(select(cls.ClientPaymentStatus))
        return res.scalar().all()

    @classmethod
    async def create_client_payment_status(cls, session: AsyncSession, **kwargs) -> "ClientPaymentStatus":
        instance = cls.ClientPaymentStatus(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_client_payment_status(cls, session: AsyncSession, client_payment_status_id: int):
        res = await session.execute(select(ClientPaymentStatus).where(ClientPaymentStatus.id == client_payment_status_id))
        client_payment_status_to_delete = res.scalar_one()
        await session.delete(client_payment_status_to_delete)
        await session.commit()
