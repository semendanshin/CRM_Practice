from db.models import Agreement
from .CrudFactory import CrudFactory
from schemas.agreement import AgreementCreate, AgreementUpdate, AgreementResponse


class AgreementRepo(
    CrudFactory(
        Agreement,
        AgreementCreate,
        AgreementUpdate,
        AgreementResponse
    )
):
    pass
