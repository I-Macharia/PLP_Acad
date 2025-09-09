-- **Write an SQL query** to get the **firstName**, **lastName**, **email**, and **officeCode** of all employees.  
SELECT firstName, lastName, email, officeCode FROM employees AS emp;

-- Use an **INNER JOIN** to combine the **employees** table with the **offices** table using the **officeCode** column.
SELECT firstName, lastName, email, employees.officeCode
FROM employees 
INNER JOIN offices 
ON employees.officeCode = offices.officeCode;

-- **Write an SQL query** to get the **productName**, **productVendor**, and **productLine** from the **products** table.
SELECT productName, productVendor, productLine FROM products AS prods;
