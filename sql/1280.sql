# Write your MySQL query statement below
with temp as (
    select * 
    from Students s
    join Subjects
    on True
)
,
t2 as (select  student_id,subject_name, count(subject_name) as cnt
from Examinations e
group by student_id,subject_name)

select t1.student_id, t1.student_name, t1.subject_name, IFNULL(t2.cnt, 0) as attended_exams
from temp t1
left join t2
on t1.student_id = t2.student_id
and t1.subject_name = t2.subject_name
ORDER BY t1.student_id, t1.student_name, t1.subject_name;
