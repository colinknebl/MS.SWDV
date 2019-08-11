USE MyGuitarShop;
GO

-- Part A --
-- 1
SELECT CategoryName, ProductName, ListPrice
FROM Categories JOIN Products
    ON Categories.CategoryID = Products.CategoryID
ORDER BY CategoryName, ProductName;


-- 2
    SELECT FirstName, LastName, Line1, City, State, ZipCode
    FROM Customers 
        JOIN Addresses AS A1 ON Customers.BillingAddressID = A1.AddressID
    WHERE Customers.EmailAddress = 'allan.sherwood@yahoo.com'
UNION
    SELECT FirstName, LastName, Line1, City, State, ZipCode
    FROM Customers 
        JOIN Addresses AS A2 ON Customers.ShippingAddressID = A2.AddressID
    WHERE Customers.EmailAddress = 'allan.sherwood@yahoo.com';

-- 3
SELECT FirstName, LastName, Line1, City, State, ZipCode
FROM Customers 
    JOIN Addresses AS A2 ON Customers.ShippingAddressID = A2.AddressID;


-- 4
SELECT LastName, FirstName, OrderDate, ProductName, ItemPrice, DiscountAmount, Quantity
FROM Customers AS C 
    JOIN Orders AS O        ON C.CustomerID = O.CustomerID
    JOIN OrderItems AS OI   ON O.OrderID = OI.OrderID
    JOIN Products AS P      ON OI.ProductID = P.ProductID
ORDER BY LastName, OrderDate, ProductName;


-- 5
SELECT P1.ProductID, P1.ProductName, P1.ListPrice
FROM Products AS P1, Products AS P2
WHERE P1.ProductID <> P2.ProductID AND
      P1.ListPrice = P2.ListPrice;


-- 6
SELECT CategoryName, ProductID
FROM Categories
    LEFT JOIN Products ON Categories.CategoryID = Products.CategoryID
WHERE ProductID IS NULL;



-- Part B --
-- 1
SELECT COUNT(*) AS [# Of Orders], SUM(TaxAmount) AS [Total Tax]
FROM Orders;


-- 2
SELECT CategoryName, COUNT(*) AS [# Of Products], MAX(ListPrice) AS [Max Price]
FROM Categories
    JOIN Products ON Categories.CategoryID = Products.CategoryID
GROUP BY CategoryName;


-- 3
SELECT 
    EmailAddress, 
    SUM(OI.ItemPrice * OI.Quantity) AS Total,
    SUM(OI.DiscountAmount * OI.Quantity) AS Discount
FROM Customers AS C
    JOIN Orders AS O ON C.CustomerID = O.CustomerID
    JOIN OrderItems AS OI ON O.OrderID = OI.OrderID
GROUP BY EmailAddress
ORDER BY Total DESC;


-- 4
SELECT EmailAddress, 
       COUNT(*) AS NumOfOrders, 
       SUM((OI.ItemPrice - OI.DiscountAmount) * OI.Quantity) AS [Orders Total]
FROM Customers AS C 
    JOIN Orders AS O ON C.CustomerID = O.CustomerID
    JOIN OrderItems AS OI ON O.OrderID = OI.OrderID
GROUP BY EmailAddress
HAVING COUNT(*) > 1
ORDER BY [Orders Total] DESC;


-- 5
SELECT EmailAddress, 
       COUNT(*) AS NumOfOrders, 
       SUM((OI.ItemPrice - OI.DiscountAmount) * OI.Quantity) AS [Orders Total]
FROM Customers AS C 
    JOIN Orders AS O ON C.CustomerID = O.CustomerID
    JOIN OrderItems AS OI ON O.OrderID = OI.OrderID
WHERE OI.ItemPrice > 400
GROUP BY EmailAddress
HAVING COUNT(*) > 1
ORDER BY [Orders Total] DESC;
