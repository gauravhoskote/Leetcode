-- # Write your MySQL query statement below
with temp as (select c.id, c.name, o.id as oid
from Customers as c
left join Orders as o
on c.id = o.customerId)
select name as 'Customers'
from temp
where oid is NULL;
