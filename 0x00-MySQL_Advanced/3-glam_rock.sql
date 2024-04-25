-- lists all bands with Glam rock as main style, ranked by longevity
SELECT band_name AS band_name, (IFNULL(split, 2022) - formed) AS formed
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style) > 0;
