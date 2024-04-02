# Write your MySQL query statement below
with temp as (select customer_id, min(order_date) as mindate
from Delivery
group by customer_id)
select ROUND((SUM(case when temp.mindate = d.customer_pref_delivery_date then 1 else 0 end)/COUNT(*)) * 100, 2) as immediate_percentage
from Delivery d
join temp
on temp.mindate = d.order_date
  and temp.customer_id = d.customer_id;
