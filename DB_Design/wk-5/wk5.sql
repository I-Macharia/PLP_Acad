-- Creating an new user and granting privileges

-- use CREATE USER statement to create the account setting user name and password
-- CREATE USER 'ian'@'localhost'
-- IDENTIFIED BY '12345';


-- use GRANT statement to assign privileges to the account
-- Granting global privileges for creating, altering and dropping databases
-- GRANT CREATE, ALTER, DROP
-- ON salesDB.*
-- TO 'ian'@'localhost';


-- Granting specific privileges for a specific database
-- Granting privileges for selecting, inserting, updating and deleting data
-- GRANT SELECT, INSERT, UPDATE, DELETE
-- ON salesDB.*
-- TO 'ian'@'localhost';


-- Indexes
-- SHOW INDEXES FROM employees;

-- Creating Indexes
-- CREATE INDEX first_name_last_name_idx
-- ON employees (firstName, lastName);


-- Write an SQL query to create a table called student with the following columns:

-- name (String, maximum length of 100 characters)
-- age (Integer)
-- gender (String, maximum length of 10 characters)

-- CREATE TABLE `salesDB`.`students`(
-- 	name VARCHAR(50)NOT NULL,
--     age INT NOT NULL,
--     gender VARCHAR(10)
-- );

-- Write an SQL query to create an index named IdxAge from Student table.
-- CREATE INDEX IdxAge ON students(age);

-- Assignment Questions
-- Create the Customers table
-- CREATE TABLE `salesDB`.`customers`(
-- 	ID INT PRIMARY KEY,
--     firstName VARCHAR(50) NOT NULL,
--     lastName 	VARCHAR(50) NOT NULL,
--     phone VARCHAR(15) NOT NULL
--     );

-- Write an SQL query to drop an index named IdxPhone from customers table
-- SHOW INDEXES FROM customers;

-- Create the IdxPhone index
-- CREATE INDEX IdxPhone ON customers(phone);
-- SHOW INDEXES FROM customers;

-- Drop the index IdxPhone
-- DROP INDEX IdxPhone ON customers;
-- SHOW INDEXES FROM customers;

-- Question 2 👤
-- Write an SQL query to create a user named bob with the password 'S$cu3r3!' , restricted to the localhost hostname.
-- CREATE USER 'bob'@'localhost'
-- IDENTIFIED BY 'S$cu3r3!';

-- Question 3 🔑
-- Write an SQL query to grant the INSERT privilege to the user bob on the salesDB database.

-- GRANT INSERT 
-- ON salesDB.customers
-- TO 'bob'@'localhost';

-- Question 4 🔐
-- Write an SQL query to change the password for the user bob to 'P$55!23' .

-- ALTER USER 'bob'@'localhost'
-- IDENTIFIED BY 'P$55!23'

