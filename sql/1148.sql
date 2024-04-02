# Write your MySQL query statement below
select DISTINCT v.author_id as 'id'
from Views as v
where v.author_id = v.viewer_id
order by id;
