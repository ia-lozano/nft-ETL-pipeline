-- returns the characters w/price above its class average price
select
	*
from
	(
    select
		class,
        AVG(price) as avg_per_class
	from
		nft_data
	group by
		class
    ) as apc, nft_data
where
	price > avg_per_class and nft_data.class = apc.class
order by price ASC