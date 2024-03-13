-- create a table with foreign keys
-- create mutual database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table with foreign key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id              INT                 NOT NULL        AUTO_INCREMENT,
    state_id        INT                 NOT NULL,
    name            VARCHAR(256)        NOT NULL,
    PRIMARY KEY     (id),
    FOREIGN KEY     (state_id)          REFERENCES      states (id)
);
