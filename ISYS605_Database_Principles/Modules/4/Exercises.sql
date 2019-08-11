-- Part A --
-- 1
SELECT DISTINCT VendorName
FROM Vendors 
WHERE VendorID IN (SELECT DISTINCT VendorID
                   FROM Invoices)
ORDER BY VendorName;

-- 2
SELECT InvoiceNumber, InvoiceTotal
FROM Invoices
WHERE PaymentTotal > (
    SELECT AVG(PaymentTotal) 
    FROM Invoices 
    WHERE PaymentTotal <> 0
);

-- 3
SELECT InvoiceNumber, InvoiceTotal
FROM Invoices
WHERE PaymentTotal > ALL
     (SELECT TOP 50 PERCENT PaymentTotal
      FROM Invoices
      WHERE PaymentTotal <> 0
      ORDER BY PaymentTotal);

-- 4
SELECT AccountNo, AccountDescription
FROM GLAccounts
WHERE NOT EXISTS
    (SELECT *
     FROM InvoiceLineItems
     WHERE InvoiceLineItems.AccountNo = GLAccounts.AccountNo)
ORDER BY AccountNo;

-- 5
SELECT VendorName, Invoices.InvoiceID, InvoiceSequence, InvoiceLineItemAmount
FROM Vendors JOIN Invoices 
  ON Vendors.VendorID = Invoices.VendorID
JOIN InvoiceLineItems
  ON Invoices.InvoiceID = InvoiceLineItems.InvoiceID
WHERE Invoices.InvoiceID IN
      (SELECT InvoiceID
       FROM InvoiceLineItems
       WHERE InvoiceSequence > 1)
ORDER BY VendorName, Invoices.InvoiceID, InvoiceSequence;

-- 6
SELECT SUM(InvoiceMax) AS SumOfMaximums
FROM (SELECT VendorID, MAX(InvoiceTotal) AS InvoiceMax
      FROM Invoices
      WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
      GROUP BY VendorID) AS MaxInvoice;

-- 7
SELECT VendorName, VendorCity, VendorState
FROM Vendors
WHERE VendorState + VendorCity NOT IN 
	(SELECT VendorState + VendorCity
	FROM Vendors
	GROUP BY VendorState + VendorCity
	HAVING COUNT(*) > 1)
ORDER BY VendorState, VendorCity;

-- 8
SELECT VendorName, InvoiceNumber AS FirstInv,
       InvoiceDate, InvoiceTotal
FROM Invoices AS I_Main JOIN Vendors
  ON I_Main.VendorID = Vendors.VendorID
WHERE InvoiceDate =
  (SELECT MIN(InvoiceDate)
   FROM Invoices AS I_Sub
   WHERE I_Sub.VendorID = I_Main.VendorID)
ORDER BY VendorName;

-- 9
WITH MaxInvoice AS
(
    SELECT VendorID, MAX(InvoiceTotal) AS InvoiceMax
    FROM Invoices
    WHERE InvoiceTotal - CreditTotal - PaymentTotal > 0
    GROUP BY VendorID
)
SELECT SUM(InvoiceMax) AS SumOfMaximums
FROM MaxInvoice;

-- Part B --
-- 1a
DROP TABLE VendorCopy;
DROP TABLE InvoiceCopy;
-- 1b
SELECT *
INTO VendorCopy
FROM Vendors;
-- 1c
SELECT *
INTO InvoiceCopy
FROM Invoices;

-- 2
INSERT INTO InvoiceCopy
VALUES (32, 'AX-014-027', '6/21/12', 434.58, 0, 0, 2, '7/8/12', NULL)
SELECT * from InvoiceCopy where InvoiceNumber = 'AX-014-027'

-- 3
INSERT INTO VendorCopy
SELECT VendorName, VendorAddress1, VendorAddress2,
       VendorCity, VendorState, VendorZipCode,
       VendorPhone, VendorContactLName, VendorContactFName,
       DefaultTermsID, DefaultAccountNo
FROM Vendors
WHERE VendorState <> 'CA';

-- 4
UPDATE VendorCopy 
SET DefaultAccountNo = 403 
WHERE DefaultAccountNo = 400;

-- 5
UPDATE InvoiceCopy
SET PaymentDate = GETDATE(), 
    PaymentTotal = InvoiceTotal - CreditTotal
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

-- 6
UPDATE InvoiceCopy
SET TermsID = 2
WHERE InvoiceCopy.VendorID IN (
    SELECT VendorID
    FROM VendorCopy
    WHERE DefaultTermsID = 2);

-- 7
UPDATE InvoiceCopy
SET TermsID = 2
FROM InvoiceCopy AS I JOIN VendorCopy AS V ON I.VendorID = V.VendorID
WHERE DefaultTermsID = 2;

-- 8
DELETE VendorCopy
WHERE VendorState = 'MN'

-- 9
DELETE VendorCopy
WHERE VendorState NOT IN 
    (SELECT DISTINCT VendorState 
     FROM VendorCopy JOIN InvoiceCopy
     ON VendorCopy.VendorID = InvoiceCopy.VendorID);


-- PART C --
-- 1
SELECT CAST(InvoiceTotal AS decimal(17,2)) AS CastAsDecimal,
       CAST(InvoiceTotal AS varchar) AS CastAsVarchar,
       CONVERT(decimal(17,2),InvoiceTotal) AS ConvertToDecimal,
       CONVERT(varchar,InvoiceTotal,1) AS ConvertToVarchar
FROM Invoices;

-- 2
SELECT CAST(InvoiceDate AS varchar) AS CastAsVarchar,
       CONVERT(varchar,InvoiceDate,1) AS ConvertToStyle1,
       CONVERT(varchar,InvoiceDate,10) AS ConvertToStyle10,
       CAST(InvoiceDate AS real) AS ConvertToReal
FROM Invoices;