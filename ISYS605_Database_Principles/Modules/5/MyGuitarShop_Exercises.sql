USE MyGuitarShop;
GO

-- ***************************************************
-- Part A
-- 1
SELECT ListPrice, DiscountPercent, 
    ROUND(ListPrice * (DiscountPercent * .01), 2) AS DiscountAmount
FROM Products;
GO


-- 2
SELECT OrderDate, YEAR(OrderDate) AS [Year], DAY(OrderDate) AS [Day], OrderDate + 30 AS [OrderDate + 30 days]
FROM Orders;
GO


-- 3
SELECT 
    CardNumber, 
    LEN(CardNumber) AS [Length], 
    RIGHT(CardNumber, 4) AS [Last 4],
    STUFF(CardNumber, 1, LEN(CardNumber) - 4, 'XXXX-XXXX-XXXX-') AS Concealed
    -- CONCAT(REPLICATE('XXXX-', 3), RIGHT(CardNumber, 4)) AS Concealed -- this also works
FROM Orders;
GO


-- ***************************************************
-- Part B
-- 1
CREATE VIEW CustomerAddresses AS
    SELECT 
        C.CustomerID, EmailAddress, LastName, FirstName,
        A1.Line1 AS BillLine1, 
        A1.Line2 AS BillLine2, 
        A1.City AS BillCity, 
        A1.[State] AS BillState,
        A1.ZipCode AS BillZip,
        A2.Line1 AS ShipLine1, 
        A2.Line2 AS ShipLine2, 
        A2.City AS ShipCity, 
        A2.[State] AS ShipState, 
        A2.ZipCode AS ShipZip
    FROM Customers AS C JOIN Addresses AS A1 
        ON C.BillingAddressID = A1.AddressID 
        JOIN Addresses AS A2 
            ON C.ShippingAddressID = A2.AddressID
GO


-- 2
SELECT CustomerID, LastName, FirstName, BillLine1
FROM CustomerAddresses;
GO


-- ***************************************************
-- Part C
-- 1
-- select all addresses by state
CREATE PROCEDURE SelectAddressesByState @State VARCHAR(4) AS
    SELECT * FROM Addresses WHERE State = @State
GO
-- EXEC SelectAddressesByState 'MI';

-- 2
-- Counts the number of products associated to a particular order 
CREATE FUNCTION fnNumProdutsOrdered(
    @OrderID int
)
RETURNS int
AS 
BEGIN
    RETURN (SELECT COUNT(*) FROM OrderItems WHERE OrderID = @OrderID);
END
GO
SELECT dbo.fnNumProdutsOrdered(41); -- returns 2 (Order 41 has 2 items on it)
