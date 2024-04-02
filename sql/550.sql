# Write your MySQL query statement below
with temp as (select a.player_id, min(a.event_date) as firstdate
from Activity a
group by a.player_id)
select round(sum(case when abs(datediff(firstdate, event_date)) = 1 then 1 else 0 end)/count(distinct t.player_id), 2) as fraction
-- select *
from Activity a2
join temp t
on t.player_id = a2.player_id;
