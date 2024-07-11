-- List all bands with Glam rock as their main style
SELECT
    band_name,
    YEAR(MAX(year_end)) - YEAR(MIN(year_start)) AS lifespan
FROM bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;