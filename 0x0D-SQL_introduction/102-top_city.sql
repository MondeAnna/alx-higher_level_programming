-- top three temperatures during July and August by city
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY CITY
ORDER BY avg_temp DESC
LIMIT 3;
