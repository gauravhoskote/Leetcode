# Write your MySQL query statement below
with temp as(
    select query_name,rating/position as ratio, IF(rating < 3, 1, 0) as cnt
    from Queries
)
select t.query_name, ROUND(AVG(ratio),2) as quality, ROUND((SUM(cnt)/COUNT(*))*100, 2) as poor_query_percentage
from temp t
where t.query_name is not NULL
group by t.query_name;
