from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
agreement_id: Mapped[int] = Column(Integer, ForeignKey('agreements.id'))
service_period_start: Mapped[date] = Column(DateTime)
service_period_end: Mapped[date] = Column(DateTime)
"""


class ClientAgreementUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    agreement_id: Optional[int] = None
    service_period_start: Optional[datetime] = None
    service_period_end: Optional[datetime] = None


class ClientAgreementCreate(ClientAgreementUpdate):
    agreement_id: int
    service_period_start: datetime
    service_period_end: datetime


class ClientAgreementResponse(ClientAgreementCreate):
    id: int
