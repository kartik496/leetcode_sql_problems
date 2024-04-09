# Write your MySQL 
select teacher_id,count(distinct subject_id) as cnt
from teacher
group by teacher_id;