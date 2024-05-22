-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id AS "id", cities.name AS "name", states.name
FROM cities
LEFT JOIN states
ON cities.id = states.id
ORDER BY cities.id
