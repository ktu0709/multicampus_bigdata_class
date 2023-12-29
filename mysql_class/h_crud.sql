start transaction;
use my_emp;

/*
create table my_emp
as 
select * from emp

create table my_dept
as 
select * from dept
*/


select * from my_emp;
select * from my_dept;

select * from my_emp where empno = 7499;

update my_emp
set sal = 5000
where empno = 7499;


select * from my_emp where empno = 7499;

-- select @autocommit; 
-- select @@global.autocommit; -- 글로벌 수준의 변수값 확인


select * from my_emp
where deptno = 20;

update my_emp set sal = 2000
where deptno = 20;

select * from my_emp
where deptno = 20;

insert into my_dept values(50,'RESERCH','BOSTON');
select * from my_dept;

update my_emp
set sal = 4000 , deptno = 30
where ename = 'FORD';
/*
update my_emp
set deptno = (select deptno
			  from my_emp
              where empno = 7934)
where empno = 7698;	
*/	

-- 7-1 :   사원의 번호 1 이고 매니저가 7785을 가진 사원을 삭제 하자.  
 delete from my_emp where empno = 1 and mgr = 7785;
 
 
 -- 7-2 : 사번 0001에  DEPTNO  20을 수정 해보자.   -- 3개의 ROW가 바뀌는지 확인 
 update my_emp
 set deptno = 20
 where empno =1 ;
 
 -- 7-3 : 홍길동의  직업을  SALESMAN으로 바꾸어 보자  -- 3개의 ROW가 바뀌는지 확인
   update my_emp
 set job = 'SALESMAN'
 where ename ='홍길동';
 
 -- 7-4 : 홍길동의  봉급을 KING과 같이 수정해 보자.
 /*
update my_emp
 set job = (select sal from my_emp where ename = 'KING' )
 where ename ='홍길동';
 */
 
 -- 7- 5: 홍길동의 매니저가 7785인  사원의 봉급만  0으로 수정해 보자.
 update my_emp
 set job = 0
 where mgr = 7785 and ename = '홍길동';
 
 -- 7- 6: 홍길동의 매니저가  7784인  사원의 커미션만  1000으로 수정해 보자.
  update my_emp
 set comm = 1000
 where mgr = 7784 and ename = '홍길동';
 
 drop temporary table temp_king;
 
 create temporary table temp_king as 
 select sal
	from my_emp
    where ename = 'king';
    
 select * from  temp_king;
  
-- 8-1
select @w_job = job from my_emp where ename = 'WARD'  ;
 delete from my_emp
 where job = @w_job;
 
 -- 8-2
 update my_emp
 set sal =(select my.sal
		   from (select sal from my_emp where ename  ='SMITH') as  my)
           where ename = 'WARD';
           
-- 8-3

select * from my_emp where ename ='KING';
update my_emp
set job  = (select a.job from(
							select job from my_emp where ename = 'SMITH'
							) as a )
where ename = 'KING';

select * from my_emp where ename ='KING';

 -- 8-4
update my_emp
set hiredate = now()
where job  = (select a.job from(
							select job from my_emp where empno = 7499
							) as a );

-- alter table my_emp add constraint my_emp_pk primary key(empno);
-- alter table my_dept add constraint my_dept_pk primary key(deptno);


select * from
information_schema.table_constraints
where table_name = 'my_emp' or table_name = 'my_dept';

alter table my_emp add constraint
foreign key(deptno) REFERENCES my_dept(deptno)
on DELETE CASCADE;

start transaction;
select * from my_emp ;
delete from my_dept  where deptno = 10;
select * from my_emp ;

rollback;
