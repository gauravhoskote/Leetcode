-- # Write your MySQL query statement below

with temp as (select class, count(distinct student) as cnt
from Courses
group by class) 
select class 
from temp
where cnt >= 5;



-- OR


select class
from Courses
group by class
having count(distinct student)>=5;

