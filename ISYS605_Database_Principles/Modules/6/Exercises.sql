-- Part A --
-- 1
SELECT *
FROM Vendors JOIN Invoices
    ON Vendors.VendorID = Invoices.VendorID;


-- 2
SELECT VendorName, InvoiceNumber, InvoiceDate, (InvoiceTotal - PaymentTotal - CreditTotal) AS Balance
FROM Vendors JOIN Invoices
    ON Vendors.VendorID = Invoices.VendorID
WHERE (InvoiceTotal - PaymentTotal - CreditTotal) > 0
ORDER BY VendorName ASC;


-- 3
SELECT VendorName, DefaultAccountNo, AccountDescription
FROM Vendors JOIN GLAccounts
    ON Vendors.DefaultAccountNo = GLAccounts.AccountNo
ORDER BY AccountDescription, VendorName;


-- 4
SELECT VendorName, InvoiceNumber, InvoiceDate,
       InvoiceTotal - PaymentTotal - CreditTotal AS Balance
FROM Vendors, Invoices
WHERE Vendors.VendorID = Invoices.VendorID
  AND InvoiceTotal - PaymentTotal - CreditTotal > 0
ORDER BY VendorName;


-- 5
SELECT VendorName AS Vendor,
       InvoiceDate AS Date,
       InvoiceNumber AS Number,
       InvoiceSequence AS #,
       InvoiceLineItemAmount AS LineItem
FROM Vendors AS v JOIN Invoices AS i
    ON v.VendorID = i.VendorID
    JOIN InvoiceLineItems AS li
        ON i.InvoiceID = li.InvoiceID
ORDER BY Vendor, Date, Number, #;


-- 6
SELECT V1.VendorID, V1.VendorName, V1.VendorContactFName + ' ' + V1.VendorContactLName AS Name
FROM Vendors AS V1 JOIN Vendors AS V2
    ON (V1.VendorID <> V2.VendorID) AND
    (V1.VendorContactFName = V2.VendorContactFName)
ORDER BY Name;


-- 7
SELECT GL.AccountNo, AccountDescription
FROM GLAccounts AS GL LEFT JOIN InvoiceLineItems AS I
    ON GL.AccountNo = I.AccountNo
WHERE I.AccountNo IS NULL
ORDER BY AccountNo;


-- 8
    SELECT VendorName, VendorState
    FROM Vendors
    WHERE VendorState = 'CA'
UNION
    SELECT VendorName, 'Outside CA' AS VendorState
    FROM Vendors
    WHERE VendorState != 'CA'



-- Part B --
-- 1
SELECT VendorID, SUM(PaymentTotal) AS PaymentSum
FROM Invoices
GROUP BY VendorID;


-- 2
SELECT TOP 10 VendorName, SUM(PaymentTotal) AS PaymentSum
FROM Vendors JOIN Invoices
  ON Vendors.VendorID = Invoices.VendorID
GROUP BY VendorName
ORDER BY PaymentSum DESC;


-- 3
SELECT VendorName, COUNT(*) AS InvoiceCount,
       SUM(InvoiceTotal) AS InvoiceSum
FROM Vendors JOIN Invoices
  ON Vendors.VendorID = Invoices.VendorID
GROUP BY VendorName
ORDER BY InvoiceCount DESC;


-- 4
SELECT GLAccounts.AccountDescription, COUNT(*) AS LineItemCount,
       SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts JOIN InvoiceLineItems
  ON GLAccounts.AccountNo = InvoiceLineItems.AccountNo
GROUP BY GLAccounts.AccountDescription
HAVING COUNT(*) > 1
ORDER BY LineItemCount DESC;


-- 5
SELECT GLAccounts.AccountDescription, COUNT(*) AS LineItemCount,
       SUM(InvoiceLineItemAmount) AS LineItemSum
FROM GLAccounts JOIN InvoiceLineItems
  ON GLAccounts.AccountNo = InvoiceLineItems.AccountNo
 JOIN Invoices
   ON InvoiceLineItems.InvoiceID = Invoices.InvoiceID
WHERE InvoiceDate BETWEEN '2011-12-01' AND '2012-02-29'
GROUP BY GLAccounts.AccountDescription
HAVING COUNT(*) > 1
ORDER BY LineItemCount DESC;


-- 6
SELECT AccountNo, SUM(InvoiceLineItemAmount) AS LineItemSum
FROM InvoiceLineItems
GROUP BY AccountNo WITH ROLLUP;


-- 7
SELECT VendorName, AccountDescription, COUNT(*) AS LineItemCount,
       SUM(InvoiceLineItemAmount) AS LineItemSum
FROM Vendors JOIN Invoices
   ON Vendors.VendorID = Invoices.VendorID
 JOIN InvoiceLineItems
   ON Invoices.InvoiceID = InvoiceLineItems.InvoiceID
 JOIN GLAccounts
   ON InvoiceLineItems.AccountNo = GLAccounts.AccountNo
GROUP BY VendorName, AccountDescription
ORDER BY VendorName, AccountDescription;


-- 8
SELECT VendorName,
       COUNT(DISTINCT InvoiceLineItems.AccountNo) AS [# of Accounts]
FROM Vendors JOIN Invoices
  ON Vendors.VendorID = Invoices.VendorID
 JOIN InvoiceLineItems
   ON Invoices.InvoiceID = InvoiceLineItems.InvoiceID
GROUP BY VendorName
HAVING COUNT(DISTINCT InvoiceLineItems.AccountNo) > 1
ORDER BY VendorName;


-- 9
SELECT VendorID, InvoiceDate, InvoiceTotal,
    SUM(InvoiceTotal) OVER (PARTITION BY VendorID) AS VendorTotal,
    COUNT(InvoiceTotal) OVER (PARTITION BY VendorID) AS VendorCount,
    AVG(InvoiceTotal) OVER (PARTITION BY VendorID) AS VendorAvg
FROM Invoices;

