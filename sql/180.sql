# Write your MySQL query statement below
with cte as (select *,
lag(num,1) over() as l1,
lag(num,2) over() as l2
from Logs)
select distinct num as ConsecutiveNums
from cte
where num = l1
and l1 = l2;
