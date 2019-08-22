USE MyGuitarShop;
GO

CREATE ROLE OrderEntry;

GRANT INSERT, UPDATE
    ON Orders
    TO OrderEntry;

GRANT INSERT, UPDATE
    ON OrderItems
    TO OrderEntry;

GRANT SELECT
    ON DATABASE :: MyGuitarShop
    TO OrderEntry;
