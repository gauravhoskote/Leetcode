# Write your MySQL query statement below
with temp as (select a1.machine_id,  (a2.`timestamp` - a1.`timestamp`) as time_taken
from Activity a1
join Activity a2
on a1.machine_id = a2.machine_id
and a1.process_id = a2.process_id
and a1.activity_type != a2.activity_type
and a2.activity_type != "start")
select temp.machine_id, ROUND(AVG(temp.time_taken),3) as processing_time
from temp
group by temp.machine_id;
