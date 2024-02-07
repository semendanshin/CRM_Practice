
CREATE TABLE ticket_types (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	latitude FLOAT, 
	longitude FLOAT, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE ticket_statuses (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE positions (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE groups (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE slas (
	id SERIAL NOT NULL, 
	file_id VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE agreements (
	id SERIAL NOT NULL, 
	file_id VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE client_payment_statuses (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE ticket_task_statuses (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE tmc (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	description VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE services (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	description VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE instructions (
	id SERIAL NOT NULL, 
	category VARCHAR, 
	short_description VARCHAR, 
	description VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE authorizations (
	id SERIAL NOT NULL, 
	access_token VARCHAR, 
	refresh_token VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	expired_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
)

;

CREATE TABLE employees (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	surname VARCHAR, 
	patronymic VARCHAR, 
	phone VARCHAR, 
	email VARCHAR, 
	position_id INTEGER, 
	group_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(position_id) REFERENCES positions (id), 
	FOREIGN KEY(group_id) REFERENCES groups (id)
)

;

CREATE TABLE client_types (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	sla_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sla_id) REFERENCES slas (id)
)

;

CREATE TABLE client_agreements (
	id SERIAL NOT NULL, 
	agreement_id INTEGER, 
	service_period_start TIMESTAMP WITHOUT TIME ZONE, 
	service_period_end TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(agreement_id) REFERENCES agreements (id)
)

;

CREATE TABLE instruction_attachments (
	id SERIAL NOT NULL, 
	file_id VARCHAR, 
	instruction_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(instruction_id) REFERENCES instructions (id)
)

;

CREATE TABLE clients (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	type_id INTEGER, 
	agreement_id INTEGER, 
	manager_id INTEGER, 
	monthly_payment FLOAT, 
	comment VARCHAR, 
	payment_status_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES client_types (id), 
	FOREIGN KEY(agreement_id) REFERENCES agreements (id), 
	FOREIGN KEY(manager_id) REFERENCES employees (id), 
	FOREIGN KEY(payment_status_id) REFERENCES client_payment_statuses (id)
)

;

CREATE TABLE client_employees (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	surname VARCHAR, 
	patronymic VARCHAR, 
	phone VARCHAR, 
	email VARCHAR, 
	client_id INTEGER, 
	is_contact BOOLEAN, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES clients (id)
)

;

CREATE TABLE tickets (
	id SERIAL NOT NULL, 
	description VARCHAR, 
	status_id INTEGER, 
	type_id INTEGER, 
	client_id INTEGER, 
	employee_id INTEGER, 
	hours_spent FLOAT, 
	client_agreement_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(status_id) REFERENCES ticket_statuses (id), 
	FOREIGN KEY(type_id) REFERENCES ticket_types (id), 
	FOREIGN KEY(client_id) REFERENCES clients (id), 
	FOREIGN KEY(employee_id) REFERENCES employees (id), 
	FOREIGN KEY(client_agreement_id) REFERENCES client_agreements (id)
)

;

CREATE TABLE client_objects (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	client_id INTEGER, 
	latitude FLOAT, 
	longitude FLOAT, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES clients (id)
)

;

CREATE TABLE warehouses (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	client_id INTEGER, 
	latitude FLOAT, 
	longitude FLOAT, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES clients (id)
)

;

CREATE TABLE observers (
	id SERIAL NOT NULL, 
	ticket_id INTEGER, 
	employee_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ticket_id) REFERENCES tickets (id), 
	FOREIGN KEY(employee_id) REFERENCES employees (id)
)

;

CREATE TABLE ticket_tasks (
	id SERIAL NOT NULL, 
	description VARCHAR, 
	status_id INTEGER, 
	ticket_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(status_id) REFERENCES ticket_task_statuses (id), 
	FOREIGN KEY(ticket_id) REFERENCES tickets (id)
)

;

CREATE TABLE attachments (
	id SERIAL NOT NULL, 
	file_id VARCHAR, 
	ticket_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ticket_id) REFERENCES tickets (id)
)

;

CREATE TABLE devices (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	client_object_id INTEGER, 
	warehouse_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_object_id) REFERENCES client_objects (id), 
	FOREIGN KEY(warehouse_id) REFERENCES warehouses (id)
)

;

CREATE TABLE tmc_operations_in (
	id SERIAL NOT NULL, 
	tmc_id INTEGER, 
	warehouse_id INTEGER, 
	amount INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tmc_id) REFERENCES tmc (id), 
	FOREIGN KEY(warehouse_id) REFERENCES warehouses (id)
)

;

CREATE TABLE tmc_operations_move (
	id SERIAL NOT NULL, 
	tmc_id INTEGER, 
	from_warehouse_id INTEGER, 
	from_client_object_id INTEGER, 
	to_warehouse_id INTEGER, 
	to_client_object_id INTEGER, 
	amount INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tmc_id) REFERENCES tmc (id), 
	FOREIGN KEY(from_warehouse_id) REFERENCES warehouses (id), 
	FOREIGN KEY(from_client_object_id) REFERENCES client_objects (id), 
	FOREIGN KEY(to_warehouse_id) REFERENCES warehouses (id), 
	FOREIGN KEY(to_client_object_id) REFERENCES client_objects (id)
)

;

CREATE TABLE tmc_operations_out (
	id SERIAL NOT NULL, 
	tmc_id INTEGER, 
	amount INTEGER, 
	from_warehouse_id INTEGER, 
	from_client_object_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tmc_id) REFERENCES tmc (id), 
	FOREIGN KEY(from_warehouse_id) REFERENCES warehouses (id), 
	FOREIGN KEY(from_client_object_id) REFERENCES client_objects (id)
)

;

CREATE TABLE service_to_ticket (
	id SERIAL NOT NULL, 
	service_id INTEGER, 
	ticket_id INTEGER, 
	amount INTEGER, 
	price FLOAT, 
	unit VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(service_id) REFERENCES services (id), 
	FOREIGN KEY(ticket_id) REFERENCES tickets (id)
)

;

CREATE TABLE devices_operations_in (
	id SERIAL NOT NULL, 
	description VARCHAR, 
	device_id INTEGER, 
	warehouse_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(device_id) REFERENCES devices (id), 
	FOREIGN KEY(warehouse_id) REFERENCES warehouses (id)
)

;

CREATE TABLE devices_operations_move (
	id SERIAL NOT NULL, 
	description VARCHAR, 
	device_id INTEGER, 
	from_warehouse_id INTEGER, 
	from_client_object_id INTEGER, 
	to_warehouse_id INTEGER, 
	to_client_object_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(device_id) REFERENCES devices (id), 
	FOREIGN KEY(from_warehouse_id) REFERENCES warehouses (id), 
	FOREIGN KEY(from_client_object_id) REFERENCES client_objects (id), 
	FOREIGN KEY(to_warehouse_id) REFERENCES warehouses (id), 
	FOREIGN KEY(to_client_object_id) REFERENCES client_objects (id)
)

;

CREATE TABLE devices_operations_out (
	id SERIAL NOT NULL, 
	description VARCHAR, 
	device_id INTEGER, 
	from_warehouse_id INTEGER, 
	from_client_object_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id), 
	FOREIGN KEY(device_id) REFERENCES devices (id), 
	FOREIGN KEY(from_warehouse_id) REFERENCES warehouses (id), 
	FOREIGN KEY(from_client_object_id) REFERENCES client_objects (id)
)

;
