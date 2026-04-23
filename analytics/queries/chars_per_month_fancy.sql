SELECT
	YEAR(date) as year,
    MONTH(date) as month,
    COUNT(*) as chars_published
FROM nft_data
GROUP BY
	YEAR(date),
    MONTH(date);