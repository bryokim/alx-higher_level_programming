-- Displays the top 3 of cities temperatur dusing July and August
-- ordered by temperature(descending).
USE hbtn_0c_0
SET autocommit=0; source temperatures.sql; COMMIT;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
