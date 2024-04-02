# Write your MySQL query statement below
with temp as (select p.product_id, IFNULL(u.units, 0) as units, p.price * u.units as sp
from Prices p
left join UnitsSold u
on p.product_id = u.product_id
and DATEDIFF(u.purchase_date, p.start_date) >= 0
and DATEDIFF(p.end_date, u.purchase_date ) >= 0)
select t.product_id, IFNULL(ROUND(SUM(t.sp)/SUM(t.units), 2), 0) as average_price
from temp t
group by t.product_id;
