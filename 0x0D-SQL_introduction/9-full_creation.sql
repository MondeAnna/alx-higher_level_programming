-- creates a populated table in the current database
-- should the table already exist, nothing is done
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score)
VALUES (2, "Alex", 4);
INSERT INTO second_table (id, name, score)
VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score)
VALUES (4, "George", 8);
