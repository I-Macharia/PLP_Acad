SELECT * 
FROM payments;
-- insert into payments table some data
-- INSERT INTO `salesDB`.`payments`(customerNumber, checkNumber, PaymentDate, amount) 
-- VALUES
-- ('335','565463','2025-01-15','4350'),
-- ('134','886743','2025-02-13','2670'),
-- ('233','688466','2025-07-04','1340'),
-- ('279','769766','2025-07-28','1345'),
-- ('656','467466','2025-04-07','2345'),
-- ('868','267566','2025-11-04','7564'),
-- ('467','857555','2025-11-12','9755'),
-- ('575','832536','2025-11-12','7564');
SELECT * 
FROM payments;

-- Question 1
-- Write an SQL query to show the total payment amount for each payment date from payments table.
SELECT paymentDate, amount
FROM salesDB.payments;

-- Display the payment date and the total amount paid on that date.
SELECT  paymentDate, SUM(amount) AS total
FROM payments
GROUP BY paymentDate;

-- Sort the results by payment date in descending order.
SELECT paymentDate, SUM(amount) AS total
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC;

-- Show only the top 5 latest payment dates.

SELECT paymentDate, SUM(amount) AS total
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;




