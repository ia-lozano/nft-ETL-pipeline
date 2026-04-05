-- find duplicated names
SELECT
	name,
    count(*)
FROM
	nft_data
GROUP BY
	name
HAVING
	count(*) > 1