-- 코드를 작성해주세요
select id, email, first_name, last_name
from developer_infos
where skill_1 in ('Python') or skill_2 in ('Python') or skill_3 in ('Python')
order by id;