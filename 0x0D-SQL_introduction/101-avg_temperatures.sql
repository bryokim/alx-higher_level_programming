-- Displays the average temperature(Fahrenheit) by city ordered by
-- temperature(descending).
USE hbtn_0c_0
SET autocommit=0; source temperatures.sql; COMMIT;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
