SELECT
	YEAR(date) as year,
    MONTH(date) as month,
    AVG(price) as avg_price
FROM
	nft_data
GROUP BY
	YEAR(date),
    MONTH(date)
ORDER BY
	YEAR(date),
    MONTH(date)
    ASC