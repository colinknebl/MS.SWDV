-- 1
SELECT DISTINCT CategoryName
FROM Categories
WHERE CategoryID IN 
    (SELECT CategoryID FROM Products)
ORDER BY CategoryName;

-- 2
SELECT ProductName, ListPrice
FROM Products
WHERE ListPrice > (SELECT AVG(ListPrice) FROM Products)
ORDER BY ListPrice DESC;

-- 3
SELECT CategoryName
FROM Categories
WHERE NOT EXISTS
    (SELECT *
     FROM Products
     WHERE Products.CategoryID = Categories.CategoryID);


-- Part B
-- 1
INSERT INTO Categories
VALUES ('Brass');

-- 2
UPDATE Categories
SET CategoryName = 'Woodwinds'
WHERE CategoryID = 5;

-- 3
DELETE Categories
WHERE CategoryID = 5;


-- PART C
-- 1
SELECT ListPrice, 
    CAST(ListPrice AS decimal(18,1)) AS CastAsDecimal,
    CONVERT(int, ListPrice) AS ConvertToInt,
    CAST(ListPrice AS int) AS CastAsInt
FROM Products;

-- 2
SELECT DateAdded,
    CAST(DateAdded AS [date]) AS CastAsDate,
    CAST(DateAdded AS [time]) AS CastAsTime,
    (CAST((MONTH(DateAdded)) AS [varchar]) + ' - ' + CAST(DAY(DateAdded) AS [varchar])) AS 'MM - DD'
FROM Products;