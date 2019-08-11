-- 1
CREATE DATABASE Membership;

-- 2
CREATE TABLE Individuals (
    IndividualID        int             PRIMARY KEY IDENTITY,
    FirstName           varchar(50)     NOT NULL,
    LastName            varchar(50)     NOT NULL,
    [Address]           varchar(100)    NULL,
    Phone               varchar(50)     NULL
);

CREATE TABLE Groups (
    GroupID             int             PRIMARY KEY IDENTITY,
    GroupName           varchar(50)     NOT NULL,
    Dues                money           NOT NULL DEFAULT 0 CHECK (Dues >= 0)
);

CREATE TABLE GroupMembership (
    GroupID             INT             NOT NULL    FOREIGN KEY REFERENCES Groups (GroupID),
    IndividualID        INT             NOT NULL    FOREIGN KEY REFERENCES Individuals (IndividualID)
);

-- 3
CREATE CLUSTERED INDEX IX_GroupID ON GroupMembership (GroupId);
CREATE NONCLUSTERED INDEX IX_IndividualID ON GroupMembership (IndividualID);

-- 4
ALTER TABLE Individuals 
ADD DuesPaid BIT NOT NULL DEFAULT 0;

-- 5
-- use AP;
-- ALTER TABLE Invoices
-- ADD CHECK ((PaymentDate IS NULL     AND PaymentTotal = 0) OR
--            (PaymentDate IS NOT NULL AND PaymentTotal > 0)),
--     CHECK ((PaymentTotal + CreditTotal) <= InvoiceTotal);

-- 6
DROP TABLE GroupMembership;
CREATE TABLE GroupMembership (
    GroupID             INT            REFERENCES Groups (GroupID),
    IndividualID        INT            REFERENCES Individuals (IndividualID),
    UNIQUE (GroupID, IndividualID)
);
