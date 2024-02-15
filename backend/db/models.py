from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean, CheckConstraint, Enum
from sqlalchemy.orm import relationship

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

    ticket = relationship('Ticket', back_populates='ticket_type')


class TicketStatus(Base):
    __tablename__ = 'ticket_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    ticket = relationship('Ticket', back_populates='ticket_status')


class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    employee = relationship('Employee', back_populates='position')


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    employee = relationship('Employee', back_populates='group')


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

    position = relationship('Position', back_populates='employee')
    group = relationship('Group', back_populates='employee')
    ticket = relationship('Ticket', back_populates='employee')


class SLA(Base):
    __tablename__ = 'slas'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    client_type = relationship('ClientType', back_populates='sla')


class Agreement(Base):
    __tablename__ = 'agreements'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    client = relationship('Client', back_populates='agreement')


class ClientType(Base):
    __tablename__ = 'client_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sla_id = Column(Integer, ForeignKey('slas.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    clients = relationship('Client', back_populates='client_type')
    sla = relationship('SLA', back_populates='client_type')


class ClientPaymentStatus(Base):
    __tablename__ = 'client_payment_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    client = relationship('Client', back_populates='client_payment_status')


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

    employee = relationship('Employee', 'client')
    agreement = relationship('Agreement', 'client')
    client_type = relationship('ClientType', 'client')
    client_payment_status = relationship('ClientPaymentStatus', 'client')
    client_employee = relationship('ClientEmployee', back_populates='client')
    ticket = relationship('Ticket', back_populates='client')
    client_object = relationship('ClientObject', back_populates='client')
    warehouse = relationship('Warehouse', back_populates='client')


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

    client = relationship('Client', back_populates='client_employee')


class Observer(Base):
    __tablename__ = 'observers'

    id: Mapped[int] = Column(Integer, primary_key=True)
    ticket_id: Mapped[int] = Column(Integer, ForeignKey('tickets.id'))
    employee_id: Mapped[int] = Column(Integer, ForeignKey('employees.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    ticket = relationship('Ticket', back_populates='observer')
    employee = relationship('Employee', back_populates='observer')


class ClientAgreement(Base):
    __tablename__ = 'client_agreements'
    __tableargs__ = [
        CheckConstraint('service_period_start < service_period_end', name='service_period_check'),
    ]

    id: Mapped[int] = Column(Integer, primary_key=True)
    agreement_id: Mapped[int] = Column(Integer, ForeignKey('agreements.id'))
    service_period_start: Mapped[date] = Column(DateTime)
    service_period_end: Mapped[date] = Column(DateTime)

    agreement = relationship('Agreement', back_populates='client_agreement')
    ticket = relationship('Ticket', back_populates='client_agreement')


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

    status = relationship('TicketStatus', back_populates='ticket')
    ticket_type = relationship('TicketType', back_populates='ticket')
    client = relationship('Client', back_populates='ticket')
    employee = relationship('Employee', back_populates='ticket')
    client_agreement = relationship('ClientAgreement', back_populates='ticket')
    ticket_task = relationship('TicketTask', back_populates='ticket')
    attachment = relationship('Attachment', back_populates='ticket')
    service_to_ticket = relationship('ServiceToTicket', back_populates='ticket')


class TicketTaskStatuses(Base):
    __tablename__ = 'ticket_task_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    ticket_task = relationship('TicketTask', back_populates='ticket_tast_statuses')


class TicketTask(Base):
    __tablename__ = 'ticket_tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    status_id = Column(Integer, ForeignKey('ticket_task_statuses.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    ticket_task_statuses = relationship('TicketTaskStatuses', back_populates='ticket_task')
    ticket = relationship('Ticket', 'ticket_task')


class Attachment(Base):
    __tablename__ = 'attachments'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    ticket = relationship('Ticket', back_populates='attachment')



class ClientObject(Base):
    __tablename__ = 'client_objects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    client = relationship('Client', back_populates='client_object')
    devices = relationship('Devices', back_populates='client_object')
    device_operation_move_from = relationship('DeviceOperationMove')
    device_operation_move_to = relationship('DeviceOperationMove')
    device_operation_out_from = relationship('DeviceOperationOut')
    device_operation_out_to = relationship('DeviceOperationOut')
    from_tmc_operation_move = relationship('TMCOperationMove')
    to_tmc_operation_move = relationship('TMCOperationMove')
    from_tmc_operation_out = relationship('TMCOperationOut')


class Warehouse(Base):
    __tablename__ = 'warehouses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    client = relationship('Client', back_populates='warehouse')
    devices = relationship('Devices', back_populates='warehouse')
    devices_operation_in = relationship('DevicesOperationIn')
    from_devices_operation_move = relationship('DeviceOperationMove')
    to_devices_operation_move = relationship('DeviceOperationMove')
    devices_operation_out_from = relationship('DeviceOperationOut')
    tmc_operation_in = relationship('TMCOperationIn')
    from_tmc_operation_move = relationship('TMCOperationMove')
    to_tmc_operation_move = relationship('TMCOperationMove')
    from_tmc_operation_out = relationship('TMCOperationOut')


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

    client_object = relationship('ClientObject', back_populates='devices')
    warehouse = relationship('Warehouse', back_populates='devices')
    devices_operation_in = relationship('DevicesOperationIn', back_populates='devices')
    devices_operation_out = relationship('DeviceOperationOut', back_populates='devices')


class DevicesOperationIn(Base):
    __tablename__ = 'devices_operations_in'

    id: Mapped[int] = Column(Integer, primary_key=True)
    description: Mapped[str] = Column(String)
    device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))
    warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    devices = relationship('Devices')
    warehouse = relationship('Warehouse')


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

    devices = relationship('Devices', 'device_operation_move')
    from_warehouse = relationship('Warehouse')
    from_client_object = relationship('ClientObject')
    to_warehouse = relationship('Warehouse')
    to_client_object = relationship('ClientObject')


class DeviceOperationOut(Base):
    __tablename__ = 'devices_operations_out'

    id: Mapped[int] = Column(Integer, primary_key=True)
    description: Mapped[str] = Column(String)
    device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))

    from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    device = relationship('Devices')
    from_warehouse = relationship('Warehouse')
    from_client_object = relationship('ClientObject')


class TMC(Base):
    __tablename__ = 'tmc'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.now)
    updated_at: Mapped[str] = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    tmc_operation_in = relationship('TMCOperationIn', back_populates='tmc')
    tmc_operation_move = relationship('TMCOperationMove', back_populates='tmc')
    tmc_operation_out = relationship('TMCOperationOut', back_populates='tmc')


class TMCOperationIn(Base):
    __tablename__ = 'tmc_operations_in'

    id: Mapped[int] = Column(Integer, primary_key=True)
    tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
    warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    amount: Mapped[int] = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    tmc = relationship('TMC', back_populates='tmc_operation_in')
    warehouse = relationship('Warehouse')


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

    tmc = relationship('TMC', back_populates='tmc_operation_move')
    from_warehouse = relationship('Warehouse')
    from_client_object = relationship('ClientObject')
    to_warehouse = relationship('Warehouse')
    to_client_object = relationship('ClientObject')


class TMCOperationOut(Base):
    __tablename__ = 'tmc_operations_out'

    id: Mapped[int] = Column(Integer, primary_key=True)
    tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
    amount: Mapped[int] = Column(Integer)
    from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
    from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    tmc = relationship('TMC', back_populates='tmc_operation_out')
    from_warehouse = relationship('Warehouse')
    from_client_object = relationship('ClientObject')


class Service(Base):
    __tablename__ = 'services'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    service_to_ticket = relationship('ServiceToTicket', back_populates='service')


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

    service = relationship('Service', back_populates='service_to_ticket')
    ticket = relationship('Tickets', back_populates='service_to_ticket')


class Instruction(Base):
    __tablename__ = 'instructions'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    short_description = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    instruction_attachment = relationship('InstructionAttachment', back_populates='instruction')


class InstructionAttachment(Base):
    __tablename__ = 'instruction_attachments'

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    instruction_id = Column(Integer, ForeignKey('instructions.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    instruction = relationship('Instruction', back_populates='instruction_attachment')


class Authorization(Base):
    __tablename__ = 'authorizations'

    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    refresh_token = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class BotAuthorization(Base):
    __tablename__ = 'bot_authorizations'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client')
    token = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now)
