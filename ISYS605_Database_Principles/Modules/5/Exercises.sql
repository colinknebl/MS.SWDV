-- Part A --
-- 1
SELECT InvoiceNumber, InvoiceTotal - PaymentTotal - CreditTotal AS BalanceDue
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0
  AND DATEDIFF(day, InvoiceDueDate, GETDATE()) < 30;


SELECT InvoiceNumber,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance,
       InvoiceDueDate
FROM Invoices
WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0 AND
      InvoiceDueDate < GETDATE() + 30;
GO


-- 2
SELECT InvoiceNumber,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Invoices
WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0 AND
      InvoiceDueDate < GETDATE() + 30;


-- 3
SELECT InvoiceNumber,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Invoices
WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0 AND
      InvoiceDueDate <
 CAST(CAST(YEAR(GETDATE()) AS char(4)) + '-' +
      CAST(MONTH(GETDATE()) + 1 AS char(2)) + '-01' AS datetime) - 1;


-- 4
SELECT
  CASE
    WHEN GROUPING(AccountDescription) = 1 THEN '*ALL*'
    ELSE AccountDescription
  END AS Account,
  CASE
    WHEN GROUPING(VendorState) = 1 THEN '*ALL*'
    ELSE VendorState
  END AS State,
  SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts JOIN InvoiceLineItems 
  ON GLAccounts.AccountNo = InvoiceLineItems.AccountNo
 JOIN Invoices
   ON InvoiceLineItems.InvoiceID =  Invoices.InvoiceID
 JOIN Vendors
   ON Invoices.VendorID = Vendors.VendorID
GROUP BY AccountDescription, VendorState WITH CUBE;
GO

-- 5
CREATE VIEW InvoiceBasic AS 
    SELECT VendorName, InvoiceNumber, InvoiceTotal
    FROM Invoices JOIN Vendors ON Invoices.VendorID = Vendors.VendorID;
GO

SELECT * FROM InvoiceBasic
WHERE VendorName LIKE ('N%', 'O%', 'P%')
ORDER BY VendorName;
GO


-- Part B --
-- 1
CREATE VIEW InvoiceBasic
    AS
    SELECT VendorName, InvoiceNumber, InvoiceTotal
    FROM  Vendors JOIN Invoices
    ON Vendors.VendorID = Invoices.VendorID;
GO

SELECT *
FROM InvoiceBasic
WHERE VendorName LIKE '[N-P]%'
ORDER BY VendorName;
GO

-- 2
CREATE VIEW Top10PaidInvoices
    AS
    SELECT TOP 10 VendorName,
        MAX(InvoiceDate) AS LastInvoice,
        SUM(InvoiceTotal) AS SumOfInvoices
    FROM  Vendors JOIN Invoices
    ON Vendors.VendorID = Invoices.VendorID
    WHERE InvoiceTotal - CreditTotal - PaymentTotal = 0
    GROUP BY VendorName
    ORDER BY SUM(InvoiceTotal) DESC;
GO


-- 3
CREATE VIEW VendorAddress
    AS
    SELECT VendorID, VendorAddress1, VendorAddress2, VendorCity, VendorState, VendorZipCode
    FROM Vendors;
GO

SELECT *
FROM VendorAddress
WHERE VendorID = 4;

UPDATE VendorAddress
SET VendorAddress1 = '1990 Westwood Blvd',
    VendorAddress2 = 'Ste 260'
WHERE VendorID = 4;
GO


-- 4
SELECT *
FROM sys.foreign_keys;
GO

-- 5
-- Screen shot, see Exercises.docx


-- Part C --
-- 1
CREATE PROC spDateRange
       @DateMin varchar(50) = NULL,
       @DateMax varchar(50) = NULL
AS

IF @DateMin IS NULL OR @DateMax IS NULL
	THROW 50001, 'The DateMin and DateMax parameters are required.', 1;
IF NOT (ISDATE(@DateMin) = 1 AND ISDATE(@DateMax) = 1)
	THROW 50001, 'The date format is not valid. Please use mm/dd/yy.', 1;
IF CAST(@DateMin AS datetime) > CAST(@DateMax AS datetime)
	THROW 50001, 'The DateMin parameter must be earlier than DateMax', 1;

SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Invoices
WHERE InvoiceDate BETWEEN @DateMin AND @DateMax
ORDER BY InvoiceDate;
GO

EXEC spDateRange '12/7/2011', '12/9/2011';
GO


-- 2
EXEC spBalanceRange 'M%';
EXEC spBalanceRange @BalanceMin = 200, @BalanceMax = 1000;
EXEC spBalanceRange '[C,F]%', 0, 200;
GO

-- 3
CREATE PROC spDateRange
       @DateMin varchar(50) = NULL,
       @DateMax varchar(50) = NULL
AS

IF @DateMin IS NULL OR @DateMax IS NULL
	THROW 50001, 'The DateMin and DateMax parameters are required.', 1;
IF NOT (ISDATE(@DateMin) = 1 AND ISDATE(@DateMax) = 1)
	THROW 50001, 'The date format is not valid. Please use mm/dd/yy.', 1;
IF CAST(@DateMin AS datetime) > CAST(@DateMax AS datetime)
	THROW 50001, 'The DateMin parameter must be earlier than DateMax', 1;

SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Invoices
WHERE InvoiceDate BETWEEN @DateMin AND @DateMax
ORDER BY InvoiceDate;
GO


-- 4
BEGIN TRY
	EXEC spDateRange '2011-12-10', '2011-12-20';
END TRY
BEGIN CATCH
	PRINT 'Error Number:  ' + CONVERT(varchar(100), ERROR_NUMBER());
	PRINT 'Error Message: ' + CONVERT(varchar(100), ERROR_MESSAGE());
END CATCH;
GO

-- 5
CREATE FUNCTION fnUnpaidInvoiceID()
RETURNS int
BEGIN
    RETURN
    (SELECT MIN(InvoiceID)
     FROM Invoices
     WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0 AND
           InvoiceDueDate =
     (SELECT MIN(InvoiceDueDate)
      FROM Invoices
      WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0));
END;
GO

SELECT VendorName, InvoiceNumber, InvoiceDueDate,
       InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Vendors JOIN Invoices
  ON Vendors.VendorID = Invoices.VendorID
WHERE InvoiceID = dbo.fnUnpaidInvoiceID();
GO

-- 6
CREATE FUNCTION fnDateRange
      (@DateMin smalldatetime, @DateMax smalldatetime)
RETURNS table

RETURN
(SELECT InvoiceNumber, InvoiceDate, InvoiceTotal,
        InvoiceTotal - CreditTotal - PaymentTotal AS Balance
 FROM Invoices
 WHERE InvoiceDate BETWEEN @DateMin AND @DateMax);
GO

SELECT *
FROM dbo.fnDateRange('12/10/11','12/20/11');


-- 7
SELECT VendorName, FunctionTable.*
FROM Vendors JOIN Invoices
  ON Vendors.VendorID = Invoices.VendorID
JOIN dbo.fnDateRange('12/10/11','12/20/11') AS FunctionTable
  ON Invoices.InvoiceNumber = FunctionTable.InvoiceNumber;


-- 8
CREATE TABLE ShippingLabels
(VendorName varchar(50),
 VendorAddress1	varchar(50),
 VendorAddress2 varchar(50),
 VendorCity varchar(50),
 VendorState char(2),
 VendorZipCode varchar(20));
GO

CREATE TRIGGER Invoices_UPDATE_Shipping
    ON Invoices
    AFTER INSERT, UPDATE
AS
    INSERT ShippingLabels
    SELECT VendorName, VendorAddress1, VendorAddress2,
           VendorCity, VendorState, VendorZipCode
    FROM Vendors JOIN Inserted
      ON Vendors.VendorID = (SELECT VendorID FROM Inserted)
    WHERE Inserted.InvoiceTotal - Inserted.PaymentTotal
        - Inserted.CreditTotal = 0;
GO

UPDATE Invoices
SET PaymentTotal = 67.92, PaymentDate = '2012-04-23'
WHERE InvoiceID = 100;


-- 9
CREATE TABLE TestUniqueNulls
(RowID int IDENTITY NOT NULL,
 NoDupName varchar(20) NULL);
GO

CREATE TRIGGER NoDuplicates
ON TestUniqueNulls
AFTER INSERT, UPDATE AS
BEGIN
   IF
    (SELECT COUNT(*)
     FROM TestUniqueNulls JOIN Inserted
       ON TestUniqueNulls.NoDupName = Inserted.NoDupName) > 1
   BEGIN
    ROLLBACK TRAN;
	THROW 50001, 'Duplicate value.', 1;
   END;
END;
GO

INSERT into TestUniqueNulls 
VALUES (NULL);

INSERT into TestUniqueNulls 
VALUES (NULL);

INSERT into TestUniqueNulls 
VALUES ('Anne Boehm');

INSERT into TestUniqueNulls 
VALUES ('Anne Boehm');
