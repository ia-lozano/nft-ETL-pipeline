SELECT
	*
FROM
	(
    SELECT *,
    ROUND(PERCENT_RANK() OVER(ORDER BY power DESC), 2) as percentile
    FROM nft_data
    ) n
WHERE
	n.percentile <= 0.25