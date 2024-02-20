from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean, CheckConstraint, Enum

from datetime import datetime, date

from sqlalchemy.orm import Mapped

Base = declarative_base()


class TicketType(Base):
    __tablename__ = 'ticket_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TicketStatus(Base):
    __tablename__ = 'ticket_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    phone = Column(String)
    email = Column(String)
    position_id = Column(ForeignKey('positions.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class SLA(Base):
    __tablename__ = 'slas'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class Agreement(Base):
    __tablename__ = 'agreements'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ClientType(Base):
    __tablename__ = 'client_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sla_id = Column(Integer, ForeignKey('slas.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ClientPaymentStatus(Base):
    __tablename__ = 'client_payment_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Client(Base):
    __tablename__ = 'clients'
    __tableargs__ = [
        CheckConstraint('manager != observer', name='manager_observer_check')
    ]

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    type_id: Mapped[int] = Column(Integer, ForeignKey('client_types.id'))
    agreement_id: Mapped[int] = Column(Integer, ForeignKey('agreements.id'))
    manager_id = Column(Integer, ForeignKey('employees.id'))
    monthly_payment = Column(Float)
    comment = Column(String)
    payment_status_id: Mapped[int] = Column(Integer, ForeignKey('client_payment_statuses.id'))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ClientEmployee(Base):
    __tablename__ = 'client_employees'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    surname: Mapped[str] = Column(String)
    patronymic: Mapped[str] = Column(String)
    phone: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    client_id: Mapped[int] = Column(Integer, ForeignKey('clients.id'))
    is_contact: Mapped[bool] = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Observer(Base):
    __tablename__ = 'observers'

    id: Mapped[int] = Column(Integer, primary_key=True)
    ticket_id: Mapped[int] = Column(Integer, ForeignKey('tickets.id'))
    employee_id: Mapped[int] = Column(Integer, ForeignKey('employees.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ClientAgreement(Base):
    __tablename__ = 'client_agreements'
    __tableargs__ = [
        CheckConstraint('service_period_start < service_period_end', name='service_period_check'),
    ]

    id: Mapped[int] = Column(Integer, primary_key=True)
    agreement_id: Mapped[int] = Column(Integer, ForeignKey('agreements.id'))
    service_period_start: Mapped[date] = Column(DateTime)
    service_period_end: Mapped[date] = Column(DateTime)


class Ticket(Base):
    __tablename__ = 'tickets'

    # Добавить время реакции (реальное и ожидаемое). Добавить время закрытия тикета

    id = Column(Integer, primary_key=True)
    description = Column(String)
    status_id = Column(Integer, ForeignKey('ticket_statuses.id'))
    type_id = Column(Integer, ForeignKey('ticket_types.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    hours_spent = Column(Float)
    client_agreement_id = Column(Integer, ForeignKey('client_agreements.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TicketTaskStatuses(Base):
    __tablename__ = 'ticket_task_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TicketTask(Base):
    __tablename__ = 'ticket_tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    status_id = Column(Integer, ForeignKey('ticket_task_statuses.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Attachment(Base):
    __tablename__ = 'attachments'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ClientObject(Base):
    __tablename__ = 'client_objects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Warehouse(Base):
    __tablename__ = 'warehouses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Devices(Base):
    __tablename__ = 'devices'
    __tableargs__ = [
        CheckConstraint('client_object_id is not null or warehouse is not null',
                        name='client_object_warehouse_check')
    ]

    id = Column(Integer, primary_key=True)
    name = Column(String)
    client_object_id = Column(Integer, ForeignKey('client_objects.id'))
    warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DevicesOperationIn(Base):
    __tablename__ = 'devices_operations_in'

    id: Mapped[int] = Column(Integer, primary_key=True)
    description: Mapped[str] = Column(String)
    device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))
    warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DeviceOperationMove(Base):
    __tablename__ = 'devices_operations_move'

    id: Mapped[int] = Column(Integer, primary_key=True)
    description: Mapped[str] = Column(String)
    device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))
    from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
    to_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    to_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DeviceOperationOut(Base):
    __tablename__ = 'devices_operations_out'

    id: Mapped[int] = Column(Integer, primary_key=True)
    description: Mapped[str] = Column(String)
    device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))

    from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TMC(Base):
    __tablename__ = 'tmc'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.now)
    updated_at: Mapped[str] = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TMCOperationIn(Base):
    __tablename__ = 'tmc_operations_in'

    id: Mapped[int] = Column(Integer, primary_key=True)
    tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
    warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    amount: Mapped[int] = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TMCOperationMove(Base):
    __tablename__ = 'tmc_operations_move'

    id: Mapped[int] = Column(Integer, primary_key=True)
    tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
    from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
    to_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    to_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
    amount: Mapped[int] = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class TMCOperationOut(Base):
    __tablename__ = 'tmc_operations_out'

    id: Mapped[int] = Column(Integer, primary_key=True)
    tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
    amount: Mapped[int] = Column(Integer)
    from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Service(Base):
    __tablename__ = 'services'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ServiceToTicket(Base):
    __tablename__ = 'service_to_ticket'

    id: Mapped[int] = Column(Integer, primary_key=True)
    service_id: Mapped[int] = Column(Integer, ForeignKey('services.id'))
    ticket_id: Mapped[int] = Column(Integer, ForeignKey('tickets.id'))
    amount: Mapped[int] = Column(Integer)
    price: Mapped[float] = Column(Float)
    unit: Mapped[str] = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Instruction(Base):
    __tablename__ = 'instructions'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    short_description = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class InstructionAttachment(Base):
    __tablename__ = 'instruction_attachments'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    instruction_id = Column(Integer, ForeignKey('instructions.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Authorization(Base):
    __tablename__ = 'authorizations'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    access_token = Column(String)
    refresh_token = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class BotAuthorization(Base):
    __tablename__ = 'bot_authorizations'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    token = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now)
