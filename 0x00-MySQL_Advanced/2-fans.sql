-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Requirements:
-- Column names must be: origin and nb_fans

SELECT origin, sum(fans) as nb_fans
FROM metal_bands
group by origin
ORDER BY nb_fans DESC;
