-- is it getting more expensive to own a decent character?
SELECT
	*
FROM
	(
    SELECT *,
    ROW_NUMBER() OVER(PARTITION BY DATE_FORMAT(date, '%Y%m') ORDER BY price DESC) as row_numba
    FROM nft_data
    ) n
WHERE n.row_numba = 1