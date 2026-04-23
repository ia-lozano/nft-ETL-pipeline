SELECT
	*
FROM
	(
    SELECT *,
    NTILE(4) OVER(ORDER BY power DESC) as percentile
    FROM nft_data
    ) n
WHERE
	n.percentile = 1
ORDER BY power DESC