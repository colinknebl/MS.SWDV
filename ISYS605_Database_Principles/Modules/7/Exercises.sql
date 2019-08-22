-- 1
CREATE ROLE PaymentEntry;

GRANT UPDATE
  ON Invoices
  TO PaymentEntry;

GRANT INSERT, UPDATE
  ON InvoiceLineItems
  TO PaymentEntry;

ALTER ROLE db_datareader ADD MEMBER PaymentEntry;
GO

-- 2
CREATE LOGIN AAaron WITH PASSWORD = 'AAar99999',
    DEFAULT_DATABASE = AP;

CREATE USER AAaron FOR LOGIN AAaron;

ALTER ROLE PaymentEntry ADD MEMBER AAaron;
-- DROP LOGIN AAaron;
-- DROP USER AAaron

-- 3
-- Part A
CREATE TABLE NewLogins
(LoginName varchar (128));

INSERT NewLogins
VALUES ('BBrown'), ('CChaplin'), ('DDyer'), ('EEbbers');

DROP user BBrown;
DROP user CChaplin;
DROP user DDyer;
DROP user EEbbers;
DROP TABLE NewLogins;

-- Part B
DECLARE @DynamicSQL varchar(256),
        @LoginName varchar(128),
        @TempPassword char(8);

DECLARE Login_Cursor CURSOR
DYNAMIC
FOR
  SELECT DISTINCT *
  FROM NewLogins;

OPEN Login_Cursor;
FETCH NEXT FROM Login_Cursor
  INTO @LoginName;
WHILE @@FETCH_STATUS = 0
  BEGIN
    SET @TempPassword = LEFT(@LoginName, 4) + '9999';
    SET @DynamicSQL = 'CREATE LOGIN ' + @LoginName + ' ' +
                      'WITH PASSWORD = ''' + @TempPassword + ''', ' +
                      'DEFAULT_DATABASE = AP';
    EXEC (@DynamicSQL);
    SET @DynamicSQL = 'CREATE USER ' + @LoginName + ' ' +
                      'FOR LOGIN ' + @LoginName;
    EXEC (@DynamicSQL);
    SET @DynamicSQL = 'ALTER ROLE PaymentEntry ADD MEMBER ' + @LoginName;
    EXEC (@DynamicSQL);
    FETCH NEXT FROM Login_Cursor
      INTO @LoginName;
  END;
CLOSE Login_Cursor;

DEALLOCATE Login_Cursor;

-- 4
-- see images in Word doc


-- 5
ALTER ROLE PaymentEntry DROP MEMBER AAaron;
ALTER ROLE PaymentEntry DROP MEMBER BBrown;
ALTER ROLE PaymentEntry DROP MEMBER CChaplin;
ALTER ROLE PaymentEntry DROP MEMBER DDyer;
ALTER ROLE PaymentEntry DROP MEMBER EEbbers;
-- ALTER ROLE PaymentEntry DROP MEMBER FFalk;
DROP ROLE PaymentEntry;


-- 6
CREATE SCHEMA Admin;
GO

ALTER SCHEMA Admin TRANSFER dbo.ContactUpdates;

ALTER USER AAaron WITH DEFAULT_SCHEMA = Admin;

GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE
ON SCHEMA :: Admin
TO AAaron;