from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ClientAgreement
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(ClientAgreement)):
    @classmethod
    async def get_client_agreement_by_id(cls, session: AsyncSession, record_id: int) -> "ClientAgreement":
        res = await session.execute(select(cls.ClientAgreement).where(ClientAgreement.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_client_agreements(cls, session: AsyncSession) -> "ClientAgreement":
        res = await session.execute(select(cls.ClientAgreement))
        return res.scalar().all()

    @classmethod
    async def create_client_agreement(cls, session: AsyncSession, **kwargs) -> "ClientAgreement":
        instance = cls.ClientAgreement(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_client_agreement(cls, session: AsyncSession, client_agreement_id: int):
        res = await session.execute(select(ClientAgreement).where(ClientAgreement.id == client_agreement_id))
        client_agreement_to_delete = res.scalar_one()
        await session.delete(client_agreement_to_delete)
        await session.commit()
