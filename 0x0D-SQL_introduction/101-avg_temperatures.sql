-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, ROUND(AVG(temperature * 1.8 + 32), 2) AS average_temperature_fahrenheit FROM temperatures GROUP BY city ORDER BY average_temperature_fahrenheit DESC;
