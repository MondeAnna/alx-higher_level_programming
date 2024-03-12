-- alter character encoding
-- alter the database
ALTER DATABASE
    hbtn_0c_0
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

-- switch to hbtn_0c_0 database
USE hbtn_0c_0;

-- alter table
ALTER TABLE
    first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- alter column
ALTER TABLE
    first_table
    CHANGE name name
    VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
