start transaction;
use my_emp;

create view test_view
as
select * from my_emp;


select * from test_view

delete from my_emp where empno = 7934;

create view join_emp
as 
select ename, deptno ,dname
from my_emp join my_dept using(deptno);

select * from join_emp

insert into join_emp(ename,deptno,dname) values('홍길동',50,'서울');

select * from information_schema.views
 where table_schema = 'my_emp'
 
 show create view join_emp
 
create view join_emp02
as 
select ename, deptno ,dname
from my_emp join my_dept using(deptno)
where my_emp.deptno > 10
with  check option
;

drop view join_emp02

select * from join_emp02
 show create view join_emp
 
 select * from information_schema.views
 where table_schema = 'my_emp'
 
rollback;