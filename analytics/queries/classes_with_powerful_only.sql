-- Is there any class with strong characters only??
-- spoiler: NO
SELECT
	class
FROM
	nft_data
GROUP BY
	class
HAVING
	MIN(power) > (SELECT AVG(power) from nft_data)