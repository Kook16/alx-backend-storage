-- script that:
-- ranks origins of bands (country)
-- sorted by number of fans from each country

SELECT origin,
	SUM(fans) AS nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
