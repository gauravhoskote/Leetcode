# Write your MySQL query statement below
with temp as (select *, count(email) as 'cnt'
from Person as p
group by email)
select email 
from temp
where temp.cnt > 1;
