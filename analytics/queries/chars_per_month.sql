SELECT
	EXTRACT(YEAR_MONTH from date) as month_year,
    COUNT(*) as chars_published
FROM
	nft_data
GROUP BY
	EXTRACT(YEAR_MONTH from date)