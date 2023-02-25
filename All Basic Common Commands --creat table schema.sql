--creat table schema
SELECT * FROM employee;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    birth_date DATE,
    sex VARCHAR(1),
    salary INT,
    super_id INT,
    branch_id INT
);


CREATE TABLE branch (
    branch_id INT,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    PRIMARY KEY (branch_id),
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);


SELECT * FROM branch;

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;


ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

CREATE TABLE Client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40),
    branch_id INT,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

CREATE TABLE work_with (
    emp_id INT,
    client_id INT,
    total_sales INT,
    PRIMARY KEY(emp_id, client_id),
    FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
    FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);

CREATE TABLE branch_supplier (
    branch_id INT,
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY(branch_id, supplier_name),
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

----------------------------------------------------------------------------

-- Cooperate

INSERT INTO employee VALUES(100, "David", "Wallace", "1967-11-17", "M", 250000, NULL, NULL);
INSERT INTO branch VALUES(1, "Corperate", 100, "2006-02-09");

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUE(101, "Jan", "Levinson", "1961-05-11", "F", 110000, 100, 1);

--Scranton

INSERT INTO employee VALUES(102, "Michael", "Scott", "1964-03-15", "M", 70000, 100, NULL);
INSERT INTO branch VALUES(2, "Scranton", 102, "1992-04-06");

UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, "Angela", "Martin", "1971-06-25", "F", 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO work_with VALUES(105, 400, 55000);
INSERT INTO work_with VALUES(102, 401, 267000);
INSERT INTO work_with VALUES(108, 402, 22500);
INSERT INTO work_with VALUES(107, 403, 5000);
INSERT INTO work_with VALUES(108, 403, 12000);
INSERT INTO work_with VALUES(105, 404, 33000);
INSERT INTO work_with VALUES(107, 405, 26000);
INSERT INTO work_with VALUES(102, 406, 15000);
INSERT INTO work_with VALUES(105, 406, 130000);

SELECT * FROM work_with;


--MORE BASIC QUERIES
--QUESTIONS AND ANSWERS

-- 1. Find all employees 

SELECT * 
FROM employee;

-- 2. Find all client

SELECT * 
FROM client;

-- 3. Find all employees ordered by salary

-- ASCENDING
SELECT * 
FROM employee
ORDER BY salary DESC;

-- DESCENDING
SELECT * 
FROM employee
ORDER BY salary DESC;

-- 4. Find all employees ordered by sex then name

SELECT *
FROM employee
ORDER BY sex, first_name, last_name;


-- 5. Find the first 5 employee in the table
--use LIMIT

SELECT *
FROM employee
LIMIT 5;

-- 6. Find the first and last names of all the employee

SELECT first_name, last_name
FROM employee;

--7. Find the forename and surnames names of the employees
--changes the naming of the column to what its assigned

SELECT first_name AS forename, last_name AS surmane
FROM employee;

--8. find out all the different genders
--DISTINCT

SELECT DISTINCT sex
FROM employee;

SELECT DISTINCT branch_id
FROM employee;

-------------------------------------------------------------------

--SQL FUNCTIONS

-- Find the number of employee
--COUNT

SELECT COUNT(emp_id)
FROM employee;

SELECT COUNT(super_id)
FROM employee;

--Find the number of female employee born after 1970
SELECT COUNT(emp_id)
FROM employee
WHERE sex = "F" AND birth_date > "1970-12-31";

--Find the average of all employee's salaries
--AVG

SELECT AVG(salary)
FROM employee;

--Find the average of all employee's salaries from all male employees

SELECT AVG(salary)
FROM employee
WHERE sex = "M";

--Find sum for all the salaries of the employees
--SUM
SELECT SUM(salary)
FROM employee;

----------------------------------------------------------------------------
--Find how many males and females there are the employee
--count + GROUP BY  to perform this!

SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;

--Find the total sales of each salesman
--count + GROUP BY  to perform this!

SELECT emp_id, SUM(total_sales)
FROM work_with
GROUP BY emp_id;


--Find the total sales of each client
--count + GROUP BY  to perform this!

SELECT client_id, SUM(total_sales)
FROM work_with
GROUP BY client_id
ORDER BY client_id DESC;


-----------------------------------------------------------------------------
--WILDCARDS (*)
--WILDCARS IS A WAY OF DEFINE PATTERNS THAT THE DATA WANT TO BE SPECIFICALLY BE MATCH TO
-- % = any # characters, _ = one character

-- if the client name match the pattern it will be returned using two character % and _ 
-- Consider any number of character that ends with LLC

--FIND any client's who are LLC
SELECT * 
FROM client
WHERE client_name LIKE "%LLC";


--FIND any branch suppliers who are in the label business
SELECT * 
FROM branch_supplier
WHERE supplier_name LIKE "%Labels%";


--Find Any employee born in october (YYYY-10-DD format)

SELECT * 
FROM employee
WHERE birth_date LIKE "____-10%";


OR

SELECT * 
FROM employee
WHERE birth_date LIKE "____-10__";


-- Find any client who are schools
SELECT *
FROM client
WHERE client_name LIKE "%school%";


----------------------------------------------------------------------------------
--how to use UNION -- used to combine two or more SELECT statement together in SQL

--Find a list of employee and branch names
--NOTE: Same number of column and data type must be picked!! this is one column each

SELECT emp_id
FROM employee
UNION
SELECT branch_name
FROM branch;

--Add client name - using two UNION and Change the naming convention USING "AS"
SELECT emp_id AS Company_Names
FROM employee
UNION
SELECT branch_name
FROM branch
UNION
SELECT client_name
FROM client;


-- Find a list of all clients and branch suppliers' names
SELECT client.client_name, client.branch_id
FROM client
UNION
SELECT branch_supplier.supplier_name, branch_supplier.branch_id
FROM branch_supplier;


--Find the list of all the money spent or earned by the company
SELECT salary AS Amount_spent
FROM employee
UNION
SELECT total_sales
FROM work_with;


-- -------------------------------------------------------------------------------------
---- using  JOIN - use to join rows from two from two or more columns from different tables with similar attributes

--Adding values to branch tables:

INSERT INTO branch VALUES(4, 'Buffalo', NULL, NULL);
SELECT * FROM branch;

-- Find all branches and the names of their managers
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;

--using LEFT join -- all the emp_id (the first table stated) will be listed and produce then marched with the mgr_id (second table)
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON employee.emp_id = branch.mgr_id
ORDER BY branch_name DESC;  -- I ADDED ORDER BY to arrange base on specifit column

--twist switching columns declare for ON function
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON  branch.mgr_id = employee.emp_id
ORDER BY branch_name DESC;  -- closer look at the differece ON makes the difference list all the mgr_id and match it with emp_id

---- RIGHT join function usage
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT JOIN branch
ON employee.emp_id = branch.mgr_id;

-----------------------------------------------------------------------------------------------
--nest queries entail getting multiple SELECT queries embedded together
--useful when using the result of one statement to inform another statement in a complex query

--Find names of all employees who have
-- sold over 30,000 to a single client


----METHOD
--1. I develop query for emp_id from branch table who whose total_sale is greater that 30000
--2. I develop query to extract the names of the workers with the emp_id on employee table.
--1.
SELECT emp_id 
FROM work_with
WHERE total_sales>30000;

--2. SELECT first_name,last_name
FROM employee
WHERE emp_id IN ();
--completely merged together


SELECT employee.first_name,employee.last_name
FROM employee
WHERE emp_id IN (
    SELECT work_with.emp_id 
    FROM work_with
    WHERE total_sales>30000);


--Find all clients who are handled by the branch
--that Michael Scott manages
--assume you know Micheal's ID

--1. get micheal ID
SELECT employee.emp_id
FROM employee
WHERE employee.first_name = "Michael";
--OR
SELECT employee.emp_id
FROM employee
WHERE first_name LIKE "%Michael%";
--2. Find the branch Id (added the code snippet above using IN function)
SELECT branch.branch_id
FROM branch
WHERE branch.mgr_id IN (
    SELECT employee.emp_id
    FROM employee
    WHERE first_name LIKE "%Michael%"
);
---3. get the clients (COMPLETE)
SELECT client.client_name
FROM client
WHERE client.branch_id IN(
    SELECT branch.branch_id
    FROM branch
    WHERE branch.mgr_id IN (
        SELECT employee.emp_id
        FROM employee
        WHERE first_name LIKE "%Michael%"
    )
)
ORDER BY client.client_name DESC;



---------------------------------------------------------------------------------------------
--using DELETE FUNCTION
-- how to delete entries in tables when they have foreign keys associated to them.

--how ON DELET SET NULL works

DELETE FROM employee
WHERE emp_id = 102;

--view effect of the delete on branch
SELECT * FROM branch;


--ON DELETE CASCADE  -- deletes the entire rows associated to the item delete (having it as foreign key)

DELETE FROM branch
WHERE branch_id = 2;

SELECT * FROM branch_supplier;


