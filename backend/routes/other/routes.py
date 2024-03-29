from fastapi import APIRouter
from .generator import generate_crud_router, GeneratorParams, CustomHandler

import crud
from .tickets import get_employees_tickets

router = APIRouter(
    prefix="",
    tags=[],
)


data = [
    GeneratorParams(
        prefix="agreement",
        repository=crud.AgreementRepo,
    ),
    GeneratorParams(
        prefix="attachment",
        repository=crud.AttachmentRepo,
    ),
    GeneratorParams(
        prefix="client_agreement",
        repository=crud.ClientAgreementRepo,
    ),
    GeneratorParams(
        prefix="client_employee",
        repository=crud.ClientEmployeeRepo,
    ),
    GeneratorParams(
        prefix="client_object",
        repository=crud.ClientObjectRepo,
    ),
    GeneratorParams(
        prefix="client_payment_status",
        repository=crud.ClientPaymentStatusRepo,
    ),
    GeneratorParams(
        prefix="client",
        repository=crud.ClientRepo,
    ),
    GeneratorParams(
        prefix="client_type",
        repository=crud.ClientTypeRepo,
    ),
    GeneratorParams(
        prefix="device_operation_in",
        repository=crud.DeviceOperationInRepo,
    ),
    GeneratorParams(
        prefix="device_operation_out",
        repository=crud.DeviceOperationOutRepo,
    ),
    GeneratorParams(
        prefix="device_operation_move",
        repository=crud.DeviceOperationMoveRepo,
    ),
    GeneratorParams(
        prefix="device",
        repository=crud.DeviceRepo,
    ),
    GeneratorParams(
        prefix="employee",
        repository=crud.EmployeeRepo,
    ),
    GeneratorParams(
        prefix="group",
        repository=crud.GroupRepo,
    ),
    GeneratorParams(
        prefix="instruction_attachment",
        repository=crud.InstructionAttachmentRepo,
    ),
    GeneratorParams(
        prefix="instruction",
        repository=crud.InstructionRepo,
    ),
    GeneratorParams(
        prefix="observer",
        repository=crud.ObserverRepo,
    ),
    GeneratorParams(
        prefix="position",
        repository=crud.PositionRepo,
    ),
    GeneratorParams(
        prefix="service",
        repository=crud.ServiceRepo,
    ),
    GeneratorParams(
        prefix="service_to_ticket",
        repository=crud.ServiceToTicketRepo,
    ),
    GeneratorParams(
        prefix="sla",
        repository=crud.SLARepo,
    ),
    GeneratorParams(
        prefix="ticket_task",
        repository=crud.TicketTaskRepo,
    ),
    GeneratorParams(
        prefix="ticket",
        repository=crud.TicketRepo,
        get_all=False,
        custom_handlers=[
            CustomHandler(
                method="GET",
                handler=get_employees_tickets,
            ),
        ],
    ),
    GeneratorParams(
        prefix="ticket_task_status",
        repository=crud.TicketTaskStatusRepo,
    ),
    GeneratorParams(
        prefix="ticket_type",
        repository=crud.TicketTypeRepo,
    ),
    GeneratorParams(
        prefix="tmc_operation_in",
        repository=crud.TMCOperationInRepo,
    ),
    GeneratorParams(
        prefix="tmc_operation_out",
        repository=crud.TMCOperationOutRepo,
    ),
    GeneratorParams(
        prefix="tmc_operation_move",
        repository=crud.TMCOperationMoveRepo,
    ),
    GeneratorParams(
        prefix="tmc",
        repository=crud.TMCRepo,
    ),
    GeneratorParams(
        prefix="warehouse",
        repository=crud.WarehouseRepo,
    ),
]

for item in data:
    router.include_router(
        generate_crud_router(
            item
        )
    )
