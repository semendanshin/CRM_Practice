from fastapi import APIRouter
from .generator import generate_crud_router

import crud

router = APIRouter(
    prefix="",
    tags=[],
)


data = [
    {
        "prefix": "agreement",
        "repository": crud.AgreementRepo,
    },
    {
        "prefix": "attachment",
        "repository": crud.AttachmentRepo,
    },
    {
        "prefix": "authorization",
        "repository": crud.AuthorizationRepo,
    },
    {
        "prefix": "bot_auth",
        "repository": crud.BotAuthRepo,
    },
    {
        "prefix": "client_agreement",
        "repository": crud.ClientAgreementRepo,
    },
    {
        "prefix": "client_employee",
        "repository": crud.ClientEmployeeRepo,
    },
    {
        "prefix": "client_object",
        "repository": crud.ClientObjectRepo,
    },
    {
        "prefix": "client_payment_status",
        "repository": crud.ClientPaymentStatusRepo,
    },
    {
        "prefix": "client",
        "repository": crud.ClientRepo,
    },
    {
        "prefix": "client_type",
        "repository": crud.ClientTypeRepo,
    },
    {
        "prefix": "device_operation_in",
        "repository": crud.DeviceOperationInRepo,
    },
    {
        "prefix": "device_operation_out",
        "repository": crud.DeviceOperationOutRepo,
    },
    {
        "prefix": "device_operation_move",
        "repository": crud.DeviceOperationMoveRepo,
    },
    {
        "prefix": "device",
        "repository": crud.DeviceRepo,
    },
    {
        "prefix": "employee",
        "repository": crud.EmployeeRepo,
    },
    {
        "prefix": "group",
        "repository": crud.GroupRepo,
    },
    {
        "prefix": "instruction_attachment",
        "repository": crud.InstructionAttachmentRepo,
    },
    {
        "prefix": "instruction",
        "repository": crud.InstructionRepo,
    },
    {
        "prefix": "observer",
        "repository": crud.ObserverRepo,
    },
    {
        "prefix": "position",
        "repository": crud.PositionRepo,
    },
    {
        "prefix": "service",
        "repository": crud.ServiceRepo,
    },
    {
        "prefix": "service_to_ticket",
        "repository": crud.ServiceToTicketRepo,
    },
    {
        "prefix": "sla",
        "repository": crud.SLARepo,
    },
    {
        "prefix": "ticket_task",
        "repository": crud.TicketTaskRepo,
    },
    {
        "prefix": "ticket",
        "repository": crud.TicketRepo,
    },
    {
        "prefix": "ticket_type",
        "repository": crud.TicketTypeRepo,
    },
    {
        "prefix": "ticket_task_status",
        "repository": crud.TicketTaskStatusRepo,
    },
    {
        "prefix": "tmc_operation_in",
        "repository": crud.TMCOperationInRepo,
    },
    {
        "prefix": "tmc_operation_out",
        "repository": crud.TMCOperationOutRepo,
    },
    {
        "prefix": "tmc_operation_move",
        "repository": crud.TMCOperationMoveRepo,
    },
    {
        "prefix": "tmc",
        "repository": crud.TMCRepo,
    },
    {
        "prefix": "warehouse",
        "repository": crud.WarehouseRepo,
    },
]

for item in data:
    prefix = item["prefix"]
    repository = item["repository"]
    router.include_router(
        generate_crud_router(
            prefix=prefix,
            repository=repository,
        )
    )
