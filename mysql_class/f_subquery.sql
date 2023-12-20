start transaction;
-- Q1
use my_emp;


select * 
from emp
where sal > (
				select sal 
				from emp
				where ename = 'jones');
                

-- Q2)
select ename , sal,job from emp
where sal in (
select sal from emp 
where job = 'SALESMAN')	;


/*
서브쿼리의 특징  

1) 서브쿼리는 내부 쿼리(서브쿼리)와 외부 쿼리(Main query)로 구성된다. 
	
2) 서브쿼리는 SELECT, INSERT, UPDATE, DELETE 문에서 WHERE, HAVING, FROM, SELECT 절 등 위치에 사용

3) 단일 행 또는 다중 행 결과를 반환할 수 있고, 사용되는 연산자가 달라진다.

4) 일반적으로 서브쿼리는 주 쿼리의 실행에 의존적이며, 외부 쿼리의 컬럼을 참조할 수 있다.

5) EXISTS와 NOT EXISTS를 사용하여 특정 조건이 충족되는지 여부만을 판단하는 논리적 테스트를 수행한다.

6) Correlated subqueries: 서브쿼리가 외부 쿼리의 컬럼을 참조하는 경우를 말하며
   서브쿼리는 외부 쿼리의 각 행에 대해 반복적으로 실행된다.

7)서브쿼리 내에서 LIMIT 절의 사용이 제한될 수 있다.
*/		

/*
ANY

 = ANY 	 하나라도 만족하는 값이 있으면 결과를 리턴하며 IN과 동일함
 > ANY 	 값들 중 최소값 보다 크면 결과를 리턴
 >= ANY 	 값들 중 최소값 보다 크거나 같으면 결과를 리턴
 < ANY 	 값들 중 최대값 보다 작으면 결과를 리턴
 <= ANY 	 값들 중 최대값 보다 작거나 같으면 결과를 리턴
 <> ANY 	 모든 값들 중 다른 값만 리턴 ,값이 하나일 때만 가능함

ALL

 > ALL 	 값들 중 최대값 보다 크면 결과를 리턴
 >= ALL 	 값들 중 최대값 보다 크거나 같으면 결과를 리턴
 < ALL 	 값들 중 최소값 보다 작으면 결과를 리턴
 <= ALL 	 값들 중 최소값 보다 작거나 같으면 결과를 리턴
 = ALL 	 모든 값들과 같아야 결과를 리턴, 값이 하나일 때만 가능함
 <> ALL 	 모든 값들과 다르면 결과를 리턴
*/
-- Q2) 

select ename , sal from emp
where sal in(
select sal
from emp 
where deptno = 10);

-- Q3
select ename , sal , deptno from emp
where deptno in(
select deptno
from emp 
where job = 'CLERK');

-- Q4
select ename , sal , deptno from emp
where deptno in (
select deptno
from dept 
where loc = 'CHICAGO');

-- Q5
select empno,
	   ename
from emp
where empno in(
select mgr from emp);

-- Q6
select empno,
	   ename
from emp
where empno not in(
select ifnull(mgr,0) from emp);

-- Q7
select ename , sal from emp
where mgr = (
select empno from emp where ename = 'KING');


-- Q8
select ename , sal from emp
where sal >
(select max(sal) from emp where deptno = 20);


-- Q9 
select ename , sal from emp
where sal  > ANY 
(select sal from emp where deptno = 20);

-- Q10
select ename , sal from emp
where sal  > ALL
(select sal from emp where job = 'salesman');

-- Q11)
select ename , sal from emp
where sal  < ALL
(select sal from emp where job = 'salesman');

 -- Q12)
 select ename , sal , deptno from emp
 where deptno in(
 select deptno from emp where job = 'SALESMAN')
 and sal in (
 select sal from emp where job = 'SALESMAN');
 
 -- Q13)
  select ename , sal , comm from emp
 where sal in(
 select sal from emp where deptno = 30)
 and comm in (
 select ifnull(comm,0) from emp where deptno = 30)
 
 
--
select 
		ename,
        sal - (select avg(sal) from emp where deptno = a.deptno ) as res
from emp as a

select 
deptno,dname
from dept as a
where exists (select 1 from emp where  deptno  = a.deptno)


select * from emp e1
where sal = (select max(sal)
			 from emp e2
             where e1.deptno = e2.deptno)
             
select deptno , max(sal) from emp              
group by deptno with rollup


select e.empno,
	   e.ename,
       e.sal,
       e.deptno
from emp e
where 
(
select count(*) from emp              
where sal > e.sal
and e.deptno = deptno)  < 4
order by e.deptno , e.sal desc;



select e.ename,
       e.hiredate,
       e.deptno
from emp e
where 
(
select count(*) from emp              
where hiredate > e.hiredate
and e.deptno = deptno)  < 2
order  by e.deptno , e.hiredate desc;

select deptno , avg(sal) 
from emp 
group by deptno
having avg(sal) >(select avg(sal) from emp);

select deptno,count(empno) as num_count
from emp
group by deptno
having count(empno) > (
						select  avg(a.num_cnt)
						from(
							  select count(empno) as num_cnt
							  from emp
						group by deptno) as a);



select deptno ,max(sal)
from emp 
group by deptno
having max(sal) >(
					select  avg(mx_sal)
					from (
							select max(sal)  as mx_sal
							from emp
							group by deptno ) as  s1;
	)


-- from 절 서브쿼리 (인라인 뷰)

select b.dname , a.mx_sal
from
(
select deptno , max(sal) as mx_sal
from emp
group by deptno) as a 
join dept as b on a.deptno = b.deptno

/*
CREATE TABLE t1 (s1 INT, s2 CHAR(5), s3 FLOAT);
INSERT INTO t1 VALUES (1,'1',1.0);
INSERT INTO t1 VALUES (2,'2',2.0);
*/
explain format=tree
SELECT sb1,sb2,sb3
  FROM (SELECT s1 AS sb1, s2 AS sb2, s3*2 AS sb3 FROM t1) AS sb
  WHERE sb1 > 1;


SELECT AVG(sum_column1)
  FROM (SELECT SUM(sb1) AS sum_column1
        FROM t1 GROUP BY sb1) AS t1;

/* ---------------------------------------- */
 -- Q1
 create table test
 as
 select * from emp;

-- Q2
create table test02
as
select ename , job ,sal
from emp


-- Q3
create table test03(ename varchar(50))
as
select ename 
from emp

-- Q4
create table test04
as
select 
a.ename,
a.sal
from emp as a
join dept as b on a.deptno = b.deptno
where loc ='CHICAGO'

select * from test04

-- Q5)
create table test03(ename varchar(50))
as
select ename 
from emp

rollback;