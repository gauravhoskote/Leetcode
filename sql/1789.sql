# Write your MySQL query statement below
select e.employee_id, e.department_id
from Employee e
where 
        employee_id in (select employee_id
                    from Employee
                    group by employee_id
                    having count(department_id) = 1)
    or  primary_flag = 'Y'
order by e.employee_id;
