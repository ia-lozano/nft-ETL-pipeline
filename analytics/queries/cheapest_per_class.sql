-- returns the cheapest character per class (expensive sub-query)
SELECT
	*
FROM
 nft_data n
WHERE
	price = (
		SELECT MIN(price)
        FROM nft_data
        WHERE class = n.class
    );

-- returns the most expensive character (cheap way) of each class
SELECT
	n.*
FROM
	nft_data n
JOIN(
    SELECT class, MAX(price) as max_price
    FROM nft_data
    GROUP BY class) m
ON n.class = m.class
AND max_price = n.price
ORDER BY
	max_price ASC;
