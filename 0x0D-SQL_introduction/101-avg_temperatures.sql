-- importing a file 
SELECT city ,AVG((value * 1.8) + 32) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
