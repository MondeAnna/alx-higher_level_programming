-- create table with primary key within own database
-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table with primary key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id      INT             NOT NULL    AUTO_INCREMENT,
    name    VARCHAR(256)    NOT NULL,
    PRIMARY KEY (id)
);
