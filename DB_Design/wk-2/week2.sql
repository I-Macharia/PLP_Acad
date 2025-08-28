SELECT productName, quantityInStock , buyPrice
FROM `salesDB`.`products`
ORDER BY buyPrice ASC
LIMIT 5;