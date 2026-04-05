SELECT *,
-- ROW_NUMBER() OVER(ORDER BY power DESC) -- Just gives a different number to every one
-- RANK() OVER(ORDER BY power DESC) -- tied power share rank, but skips next rank
DENSE_RANK() OVER(ORDER BY power DESC) -- gives same rank to equally powerful characters
FROM nft_data