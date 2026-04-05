SELECT
    *
FROM
    (
        SELECT *,
        ROW_NUMBER() OVER(PARTITION BY class ORDER BY price DESC) as top_price
        FROM nft_data
    ) n
WHERE
    top_price = 1
