use ap;

-- SELECT *
-- FROM Vendors
-- WHERE VendorState = 'MI' OR VendorState = 'MA' OR VendorState = 'MO' OR VendorState = 'MN'

-- SELECT *
-- FROM Vendors
-- WHERE VendorState IN ('MI', 'MA', 'MO', 'MN')

-- SELECT *
-- FROM Vendors
-- WHERE VendorState LIKE 'M%' AND VendorPhone IS NOT NULL

-- SELECT VendorID, InvoiceTotal
-- FROM Invoices
-- ORDER BY InvoiceTotal DESC
--     OFFSET 5 ROWS
--     FETCH NEXT 5 ROWS ONLY;

-- Week 2 - Exercises
-- Q1
Select VendorContactLName, VendorContactFName, VendorName
From Vendors
ORDER By VendorContactLName, VendorContactFName;

-- Q2
-- SELECT InvoiceNumber AS [Number], 
--         InvoiceTotal AS Total,
--         PaymentTotal + CreditTotal AS Credits,
--         InvoiceTotal - (PaymentTotal + CreditTotal) AS Balance
-- FROM Invoices;

-- Q3
-- SELECT VendorContactLName + ', ' + VendorContactFName AS [Full Name]
-- FROM Vendors
-- ORDER BY VendorContactLName, VendorContactFName

-- Q4
-- SELECT InvoiceTotal, 
--     InvoiceTotal / 10 AS [10%], 
--     InvoiceTotal * 1.1 AS [Plus 10%]
-- FROM Invoices
-- WHERE InvoiceTotal - PaymentTotal - CreditTotal > 1000
-- ORDER BY InvoiceTotal DESC

-- Q5
-- SELECT InvoiceNumber AS [Number], 
--         InvoiceTotal AS Total,
--         PaymentTotal + CreditTotal AS Credits,
--         InvoiceTotal - (PaymentTotal + CreditTotal) AS Balance
-- FROM Invoices
-- WHERE InvoiceTotal BETWEEN 500 AND 10000;
-- -- WHERE InvoiceTotal >= 500 AND InvoiceTotal <= 10000;

-- Q6
-- SELECT VendorContactLName + ', ' + VendorContactFName AS [Full Name]
-- FROM Vendors
-- WHERE VendorContactLName LIKE '[A-C, E]%'
-- ORDER BY VendorContactLName, VendorContactFName

-- Q7
-- SELECT *
-- FROM Invoices
-- WHERE (InvoiceTotal - PaymentTotal - CreditTotal <= 0 AND -- Balance Due > 0
--       PaymentDate IS NULL) OR
--       (InvoiceTotal - PaymentTotal - CreditTotal > 0 AND -- Balance Due = 0
--       PaymentDate IS NOT NULL)
