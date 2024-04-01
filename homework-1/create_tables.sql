-- SQL-команды для создания таблиц
CREATE TABLE employees_data (
	employee_id int PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE customers_data (
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE orders_data (
	order_id int PRIMARY KEY,
	customer_id varchar (20) REFERENCES customers_data(customer_id),
	employee_id int REFERENCES employees_data(employee_id),
	order_data date,
	ship_city varchar(100)
);

SELECT * FROM customers_data

SELECT * FROM employees_data

SELECT * FROM orders_data