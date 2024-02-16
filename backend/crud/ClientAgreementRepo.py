from db.models import ClientAgreement
from .CrudFactory import CrudFactory
from schemas.client_agreement import ClientAgreementCreate, ClientAgreementUpdate, ClientAgreementResponse


class ClientAgreementRepo(
    CrudFactory(
        ClientAgreement,
        ClientAgreementUpdate,
        ClientAgreementCreate,
        ClientAgreementResponse,
    )
):
    pass
