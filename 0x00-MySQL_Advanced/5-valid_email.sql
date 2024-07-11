-- CONTEXT
-- Nothing related to MySQL, but perfect for user email validation
-- distribute the logic to the database itself!

-- script that creates a trigger resets the attribute valid_email
-- only when the email has been changed


DELIMITER ** ;
CREATE TRIGGER reset_valid_email
    BEFORE UPDATE
    ON users
    FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; **
DELIMITER ;

