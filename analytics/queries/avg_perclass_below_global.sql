-- returns the characters whose power is above the avg of their class
-- but below the global average
SELECT
	*
FROM
	(
    SELECT *,
    AVG(power) OVER(PARTITION BY class) as power_within,
    AVG(power) OVER() as global_power
    FROM nft_data
    ) n
WHERE
	power > n.power_within
    and
    power < n.global_power
ORDER BY power DESC