# Write your MySQL query statement below
with temp as (select product_id, min(year) as minyr
from Sales
group by product_id)
select t.product_id, t.minyr as first_year, s.quantity, s.price
from temp t
join Sales s
on s.year = t.minyr
and s.product_id = t.product_id;
