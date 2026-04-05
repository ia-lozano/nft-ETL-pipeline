-- returns a new colum with the power difference between per class AVG per row
SELECT
	name,
    class,
    price,
    power,
    ROUND(power - AVG(power) OVER(PARTITION BY class), 0) as power_gap
FROM
	nft_data
ORDER BY
	power_gap DESC -- grouping by alias, bad moves i know