USE master;

-- drop DB if already exists
IF DB_ID('FinanceApp') IS NOT NULL
    DROP DATABASE FinanceApp;
GO

-- create DB
CREATE DATABASE FinanceApp;
GO

-- use DB
USE FinanceApp;
GO

-- create users table
CREATE TABLE Users (
    UserID              int             PRIMARY KEY IDENTITY,
    FirstName           varchar(100)    NOT NULL,
    LastName            varchar(100)    NOT NULL,       
    Email               varchar(150)    NOT NULL,
    Zip                 varchar(20)     NOT NULL,
    Username            varchar(20)     NOT NULL,
    [Password]          varchar(255)    NOT NULL,
    DOB                 date            NULL,
    LastLoginDate       date            NOT NULL,
    SignUpDate          date            NOT NULL
);
GO

-- create banks table
CREATE TABLE Banks (
    BankID              int             PRIMARY KEY IDENTITY,
    BankName            varchar(200)    NOT NULL,
    RoutingNumber       varchar(100)    NOT NULL
);
GO

-- create accounts types table (i.e. 'checking', 'savings')
CREATE TABLE AccountTypes (
    AccountTypeID       int             PRIMARY KEY IDENTITY,
    AccountType         varchar(30)     NOT NULL
);
GO

-- create accounts table
CREATE TABLE Accounts (
    AccountID           int             PRIMARY KEY IDENTITY,
    BankID              int             REFERENCES Banks (BankID),
    AccountTypeID       int             REFERENCES AccountTypes (AccountTypeID),
    AccountNumber       varchar(100)    NOT NULL,
    Balance             money           NOT NULL DEFAULT 0,
    RewardsPoints       int             NOT NULL DEFAULT 0
);
GO

-- create a linking table bewteen users and accounts tables
CREATE TABLE UserAccounts (
    UserID              int             REFERENCES Users (UserID) ON DELETE CASCADE,
    AccountID           int             REFERENCES Accounts (AccountID)
);

-- create table to store credit bureau information
CREATE TABLE CreditBureaus (
    CreditBureauID      int             PRIMARY KEY IDENTITY,
    CreditBureauName    varchar(100)    NOT NULL
);
GO

-- create credit scores table, links users to their credit scores
CREATE TABLE CreditScores (
    CreditScoreID       int             PRIMARY KEY IDENTITY,
    UserID              int             REFERENCES Users (UserID) ON DELETE CASCADE,
    CreditBureauID      int             REFERENCES CreditBureaus (CreditBureauID),
    Score               int             NOT NULL
);
GO

-- create status table (i.e. 'pending', 'posted')
CREATE TABLE Statuses (
    StatusID            int             PRIMARY KEY IDENTITY,
    [Status]            varchar(30)     NOT NULL
);
GO

-- create transactions table
CREATE TABLE Transactions (
    TransactionID       int             PRIMARY KEY IDENTITY,
    AccountID           int             REFERENCES Accounts (AccountID),
    StatusID            int             REFERENCES Statuses (StatusID),
    MerchantName        varchar(200)    NOT NULL,
    Amount              money           NOT NULL,
    Currency            char(3)         NOT NULL DEFAULT 'USD'
);
GO

-- add usesr
INSERT INTO Users (FirstName, LastName, Email, Zip, Username, Password, DOB, LastLoginDate, SignUpDate) VALUES 
('Colin', 'Knebl', 'colin.knebl@outlook.com', '49444', 'colinknebl', '6c14e7bbc024c6b894a9e2158145e061', '8/1/1991', '7/4/2019', '5/3/2015'),
('Jessica', 'Knebl', 'Jessica.knebl@gmail.com', '49444', 'jessicaknebl', '690654dc450a2c756d2d224397c640bc', '1/31/1990', '6/3/2019', '5/3/2015'),
('Jim', 'Williams', 'crazyjim@hotmail.com', '90210', 'slimjim', '4d88f4657176b93ebc27d0dd5b357f95', '6/6/1983', '7/15/2019', '8/1/2018'),
('Allison', 'Archer', 'aarch@maryville.edu', '45212', 'aarcher96', 'ce96e4ccaa58ec9f5456b72301c5f56b', '12/16/1996', '3/4/2019', '3/4/1019'),
('Robert', 'Wickam', 'wickam.robert@yahoo.com', '90123', 'rwick', '8fa14cdd754f91cc6554c9e71929cce7', '4/15/1985', '7/5/2019', '3/29/2015'),
('Jane', 'Wickam', 'wickamjane@hotmail.com', '73341', 'coollady01', 'b1f4f9a523e36fd969f4573e25af4540', '5/29/1988', '6/27/2019', '4/2/2015'),
('Shannon', 'Wilson', 'pinkracer@outlook.com', '5g9813', 'pinkiepie', 'ea702ba4205cb37a88cc84851690a7a5', NULL, '7/16/2019', '8/4/2017'),
('Alicia', 'Ambrose', 'rose@gmail.com', '55985', 'likearose', 'fcdc7b4207660a1372d0cd5491ad856e', '9/4/1996', '6/23/2019', '5/5/2016'),
('Jennifer', 'Washington', 'washingtonrules@gmail.com', '54561', 'washington123', '24fec7b711e18a804e4703f5fce3329f', NULL, '7/7/2019', '3/1/2019'),
('Bruce', 'Wayne', 'bwayne@wayneenterprises.com', '53540', 'batmanrules', 'a5c6aba1c0695cf1d94462c59eae33dd', '4/7/1939', '7/16/2019', '1/3/2016')
GO

-- add banks
INSERT INTO Banks VALUES
('Fifth Third (5/3)', '12345678'),
('Lake Michigan Credit Union', '98765432'),
('Chase Bank', '49832187'),
('PNC Bank', '44871693'),
('Comerica Bank', '431943765'),
('USAA Bank', '421718909'),
('Huntington Bank', '836488763'),
('Community Shores Bank', '321183599'),
('Gotham Central Bank', '789844353')
GO

-- add accounts types
INSERT INTO AccountTypes VALUES 
('Savings'),
('Checking'), 
('Credit');
GO

-- add account data
INSERT INTO Accounts (BankID, AccountTypeID, AccountNumber, Balance, RewardsPoints) VALUES
-- colin knebl 1
(1, 3, '4827887644', 895.43, 2200),
(1, 2, '4873229984', 1342844.88, 0),
-- jessica knebl 2
(1, 1, '8377365423', 98788.42, 0),
-- Jim Williams 3
(3, 1, '4987784531', 7446.43, 1400),
-- Allison Archer 4
(2, 2, '4448321475', 8834.21, 150),
-- Robert Wickam 5
(5, 2, '7443765788', 343.98, 540),
-- Jane Wickam 6
(4, 1, '2215887854', 46983.02, 1400),
-- Shannon Wilson 7
(6, 3, '9099987232', 3500.00, 340),
-- Alicia Ambrose 8
(7, 3, '9894527648', 23.28, 0),
-- Jennifer Washington 9
(3, 2, '3438765473', 755.98, 200),
-- Bruce Wayne 10
(9, 1, '565787110', 54098447.64, 0),
(9, 2, '5658934521', 12843221.99, 0);
GO

-- create the many to many relationship between users and accounts
INSERT INTO UserAccounts (UserID, AccountID) VALUES
-- Colin 1
(1, 1),
(1, 2),
(1, 3),
-- Jessica 2
(2, 1),
(2, 2),
(2, 3),
-- Jim Williams 3
(3, 4),
-- Allison Archer 4
(4, 5),
-- Robert Wickam 5
(5, 6),
-- Jane Wickam 6
(6, 7),
-- Shannon Wilson 7
(7, 8),
-- Alicia Ambrose 8
(8, 9),
-- Jennifer Washington 9
(9, 10),
-- Bruce Wayne 10
(10, 11),
(10, 12)
GO

-- Add credit bureaus
INSERT INTO CreditBureaus VALUES 
('Equifax'),
('Experian'),
('TransUnion')
GO

-- Add user's credit scores, one score for each of the 3 major bureaus
INSERT INTO CreditScores (UserID, CreditBureauID, Score) VALUES
(1, 1, 783),
(1, 2, 787),
(1, 3, 779),
(2, 1, 810),
(2, 2, 804),
(2, 3, 798),
(3, 1, 678),
(3, 2, 665),
(3, 3, 667),
(4, 1, 800),
(4, 2, 802),
(4, 3, 788),
(5, 1, 632),
(5, 2, 623),
(5, 3, 625),
(6, 1, 723),
(6, 2, 732),
(6, 3, 730),
(7, 1, 712),
(7, 2, 710),
(7, 3, 711),
(8, 1, 767),
(8, 2, 757),
(8, 3, 762),
(9, 1, 598),
(9, 2, 589),
(9, 3, 591),
(10, 1, 0),
(10, 2, 0),
(10, 3, 0);
GO

-- add statuses
INSERT INTO Statuses VALUES
('pending'),
('posted');
GO

-- add transactions
INSERT INTO Transactions (AccountID, StatusID, MerchantName, Amount, Currency) VALUES 
-- 1
(1, 1, 'Meijer', 152.32, 'USD'),
(1, 2, 'Wesco', 19.78, 'USD'),
(1, 2, 'TJ Max', 45.33, 'USD'),
-- 2
(2, 1, 'Meijer', 77.54, 'USD'),
(2, 2, 'Meijer Gas', 13.33, 'USD'),
(2, 2, 'Aldi', 93.24, 'USD'),
-- 3
(3, 2, 'Dunhams', 435.83, 'USD'),
(3, 2, 'Wesco', 67.22, 'USD'),
(3, 2, 'Home Depot', 883.21, 'USD'),
-- 4
(4, 1, 'Tropical Smoothie', 8.77, 'USD'),
(4, 1, 'Hallmark', 15.44, 'USD'),
(4, 2, 'Pump House Frozen Yogurt', 7.32, 'USD'),
-- 5
(5, 2, 'El Toro Loco', 53.29, 'USD'),
(5, 2, 'Menards', 75.31, 'USD'),
(5, 2, 'iTunes', 12.99, 'USD'),
-- 6
(6, 1, 'Amazon', 103.49, 'USD'),
(6, 2, 'Family Video', 16.88, 'USD'),
(6, 2, 'JCPenny', 93.45, 'USD'),
-- 7
(7, 2, 'Amazon', 231.94, 'USD'),
(7, 2, 'Amazon', 31.30, 'USD'),
(7, 2, 'Home Goods', 74.00, 'USD'),
-- 8
(8, 1, 'El Burrito', 3.25, 'MXN'),
(8, 1, 'Taco Taco Taco', 8.51, 'MXN'),
(8, 1, 'Avacado Delicioso', 30.88, 'MXN'),
-- 9
(9, 2, 'Walmart Supercenter', 90.32, 'USD'),
(9, 2, 'Chow Hound Pet Supplies', 92.95, 'USD'),
(9, 2, 'Lee & Birch', 205.66, 'USD'),
-- 10
(10, 1, 'Bekins', 1402.42, 'USD'),
(10, 1, 'The Yankee Pedlar', 21.33, 'USD'),
(10, 2, 'D&W Fresh Market', 87.73, 'USD'),
-- 11
(11, 1, 'Kilwins', 731.33, 'USD'),
(11, 1, 'Walgreens', 32.87, 'USD'),
(11, 2, 'The Creative Fringe LLC', 4351.53, 'USD'),
-- 12
(12, 2, 'Dollar Tree', 3.42, 'USD'),
(12, 2, 'Beach Party Store', 74.32, 'USD'),
(12, 2, 'Surf Shop', 793.44, 'USD');
GO



-- Views --
-- A view for general account information
CREATE VIEW AccountsGeneral AS
    SELECT AccountID, BankID, AccountTypeId
    FROM Accounts;
GO

-- A view for the different account types
CREATE VIEW AccountTypesView AS 
    SELECT AccountType FROM AccountTypes;
GO

-- A view for banking names and routing numbers
CREATE VIEW BanksGeneral AS 
    SELECT BankName, RoutingNumber
    FROM Banks;
GO

-- A view that lists the Credit Bureaus
CREATE VIEW CreditBureausGeneral AS
    SELECT CreditBureauName FROM CreditBureaus;
GO

-- A view for all user info but their password
CREATE VIEW UsersGeneral AS
    SELECT UserID, FirstName, LastName, Email, Zip, Username, DOB, LastLoginDate, SignUpDate FROM Users;
GO

-- A view for login details
CREATE VIEW [Login] AS
    SELECT Username, [Password] FROM Users;
GO

-- A view for statuses
CREATE VIEW StatusesTypes AS 
    SELECT Status from Statuses;
GO

-- A view for general transaction data
-- Example usage:
-- SELECT * FROM TransactionsGeneral
CREATE VIEW TransactionsGeneral AS
    SELECT MerchantName, Amount, Currency, Status
    FROM Transactions AS T 
        JOIN Statuses AS S ON T.StatusID = S.StatusID;
GO

-- A view that retrieves credit scores from all three bureaus for the specified users
-- Example usage:
-- SELECT * FROM UserCreditScores
-- WHERE FirstName = 'Colin'
CREATE VIEW UserCreditScores AS
    SELECT U.FirstName, U.LastName, C.Score, CB.CreditBureauName
    FROM 
        CreditScores AS C JOIN Users AS U 
        ON C.UserID = U.UserID JOIN CreditBureaus AS CB 
            ON C.CreditBureauID = CB.CreditBureauID;;
GO


-- Queries Containing Calculated Fields --
-- A query for summing a user's rewards points
SELECT LastName + ', ' + FirstName AS Name, 
       SUM(A.RewardsPoints) AS [Total Rewards]
FROM Users AS U 
    JOIN UserAccounts AS UA ON U.UserID = UA.UserID
    JOIN Accounts AS A ON A.AccountID = UA.AccountID
GROUP BY LastName, FirstName
ORDER BY [Total Rewards] DESC;
GO

-- A query for getting the sum of a user's transactions that 
-- have a currency type of 'USD' and transactions totalling over $1,000
SELECT LastName + ', ' + FirstName AS Name, 
       COUNT(*) AS [Number of Transactions],
       CONCAT('$', SUM(T.Amount)) AS [Total of Transactions]
FROM Users AS U 
    JOIN UserAccounts AS UA ON U.UserID = UA.UserID
    JOIN Accounts AS A ON A.AccountID = UA.AccountID
    JOIN Transactions AS T ON T.AccountID = A.AccountID
WHERE Currency = 'USD'
GROUP BY LastName, FirstName
HAVING SUM(T.Amount) > 1000
ORDER BY Name;
GO


-- Procedures --
-- A procedure that selects all users
-- Example usage: EXEC SelectAllUsers
CREATE PROCEDURE SelectAllUsers AS
    SELECT * FROM Users;
GO

-- A procedure that selects all columns from the UsersGeneral view that signed up on the specified date
-- Example usage: EXEC SelectUsersBySignUpDate '2015-05-03' OR EXEC SelectUsersBySignUpDate @SignUpDate = '2015-05-03'
CREATE PROCEDURE SelectUsersBySignUpDate @SignUpDate DATETIME
AS
    SELECT * FROM UsersGeneral
    WHERE SignUpDate = @SignUpDate
GO

-- A procedure that selects all columns from the UsersGeneral view that logged in between the provided dates
-- The LoginMin has a default value that is prior to all user's sign up date. This allows for only specifying
-- a LoginMax date to view all users in which their last login was prior to/including the specified date.
-- Example usage 1: EXEC SelectUsersSignedUpBetween '2019-07-15', '2019-07-17'
-- Example usage 2: EXEC SelectUsersSignedUpBetween @LoginMin = '2000-01-01', @LoginMax = '2019-08-08'
-- Example usage 3: EXEC SelectUsersSignedUpBetween @LoginMax = '2019-03-17'
CREATE PROCEDURE SelectUsersSignedUpBetween @LoginMin DATETIME = '2000-01-01', @LoginMax DATETIME
AS
    SELECT * FROM UsersGeneral
    WHERE LastLoginDate BETWEEN @LoginMin AND @LoginMax
GO



-- Functions --
-- Returns a table of all of the User's transactions
-- Example usage 1: SELECT * from dbo.fnUserTransactions('Wayne');
-- Example usage 2 (Totals the user's transactions): 
--      SELECT SUM(AMOUNT) AS [Total of Transactions] FROM dbo.fnUserTransactions('Knebl');
CREATE FUNCTION fnUserTransactions( @UserLastName varchar(50))
RETURNS table
AS
RETURN (
    SELECT DISTINCT T.AccountID, Amount, MerchantName
    FROM Transactions AS T 
        JOIN Accounts AS A ON T.AccountID = A.AccountID 
        JOIN UserAccounts AS UA ON A.AccountID = UA.AccountID 
        JOIN Users AS U ON UA.UserID = U.UserID
    WHERE U.LastName = @UserLastName
);
GO
