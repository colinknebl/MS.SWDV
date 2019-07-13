use MyGuitarShop;

-- Q1
SELECT ProductCode, ProductName, ListPrice, DiscountPercent
FROM Products
ORDER BY ListPrice DESC;

-- Q2
SELECT LastName + ', ' + FirstName  AS [Full Name]
FROM Customers
WHERE LastName LIKE '[M-Z]%'
ORDER BY LastName;

-- Q3
SELECT ProductName, ListPrice, DateAdded
FROM Products
WHERE ListPrice BETWEEN 500 AND 2000
ORDER BY DateAdded DESC;

-- Q4
SELECT ProductName, ListPrice, DiscountPercent, 
       ListPrice * (DiscountPercent * 0.01) AS DiscountAmount, 
       ListPrice - (ListPrice * (DiscountPercent * 0.01)) AS DiscountPrice
FROM Products
ORDER BY ListPrice DESC;

-- Q5
SELECT ItemID, ItemPrice, DiscountAmount, Quantity,
       ItemPrice * Quantity AS PriceTotal,
       DiscountAmount * Quantity AS DiscountTotal,
       (ItemPrice - DiscountAmount) * Quantity AS ItemTotal
FROM OrderItems
WHERE (ItemPrice - DiscountAmount) * Quantity > 500
ORDER BY [ItemTotal] DESC;

-- Q6
SELECT OrderID, OrderDate, ShipDate
FROM Orders
WHERE ShipDate IS NULL;

-- Q7
SELECT Price = 100, TaxRate = 0.07, 100 * 0.07 AS TaxAmount, 100 + (100 * 0.07) AS Total;
