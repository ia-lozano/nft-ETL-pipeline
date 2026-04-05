-- returns the 2 most powerfull characters from their class
SELECT
	*
FROM
	(
		SELECT *,
			   ROW_NUMBER() OVER(PARTITION BY class ORDER BY power DESC) as position
        FROM nft_data
	) n
WHERE
	position <= 2