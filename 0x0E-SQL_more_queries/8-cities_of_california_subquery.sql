-- subquery primary key to value for conditional evaluation
SELECT *
  FROM cities
 WHERE cities.state_id =
       (SELECT id
          FROM states
         WHERE states.name = "California")
 ORDER BY cities.id;
