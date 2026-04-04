-- returns the characters w/price above its average class price but elegant
SELECT
	*
FROM
	nft_data n
WHERE
	price > (
		SELECT AVG(price)
		FROM nft_data
		WHERE class = n.class
	);