-- 1
USE MyGuitarShop;
GO
CREATE INDEX IX_Zip ON Addresses (ZipCode);
GO

-- 2
use master;
GO

IF  DB_ID('MyWebDB') IS NOT NULL
    DROP DATABASE MyWebDB;
GO

CREATE DATABASE MyWebDB;
GO

USE MyWebDB;
GO

CREATE TABLE Users(
    UserID          INT             PRIMARY KEY IDENTITY,
    EmailAddress    VARCHAR(75)     NOT NULL,
    FirstName       VARCHAR(50)     NULL,
    LastName        VARCHAR(50)     NOT NULL
);

CREATE TABLE Products(
    ProductID       INT             PRIMARY KEY IDENTITY,
    ProductName     VARCHAR(50)     NOT NULL
);

CREATE TABLE Downloads(
    DownloadID      INT             PRIMARY KEY IDENTITY,
    UserID          INT             FOREIGN KEY REFERENCES Users (UserID),
    ProductID       INT             FOREIGN KEY REFERENCES Products (ProductID),
    DownloadDate    DATETIME        NOT NULL,
    [FileName]      VARCHAR(50)     NOT NULL
);
GO

CREATE NONCLUSTERED INDEX IX_LastName ON Users (LastName);
CREATE NONCLUSTERED INDEX IX_DownloadDate ON Downloads (DownloadDate);
GO

-- 3
INSERT INTO Users VALUES 
('colin.knebl@outlook.com', 'Colin', 'Knebl'),
('jessica.knebl@gmail.com', 'Jessica', 'Knebl')
GO

INSERT INTO Products VALUES
('Diapers'),
('Wipes')
GO

INSERT INTO Downloads VALUES
(1, 2, GETDATE(), 'wipes.txt'),
(2, 1, GETDATE(), 'diapers.txt'),
(2, 2, GETDATE(), 'wipes.txt')
GO

SELECT 
    U.EmailAddress AS [email_address],
    U.FirstName AS [first_name],
    U.LastName AS [last_name],
    D.DownloadDate AS [download_date],
    D.[FileName] AS [filename],
    P.ProductID AS [product_name]
FROM Downloads AS D
    JOIN Users AS U ON D.UserID = U.UserID
    JOIN Products AS P ON D.ProductID = P.ProductID
ORDER BY email_address DESC, product_name ASC;
GO

-- 4
ALTER TABLE Products 
ADD ProductPrice MONEY NOT NULL DEFAULT 9.99; 
GO

ALTER TABLE Products
ADD ProductAdded DATETIME NULL
GO

-- 5
ALTER TABLE Users
ALTER COLUMN FirstName varchar(20) NOT NULL;
GO

UPDATE Users
SET FirstName = NULL
WHERE UserID = 1;
GO

UPDATE Users
SET FirstName = 'supercalifragilisticexpialidocious'
WHERE UserID = 2;
GO





