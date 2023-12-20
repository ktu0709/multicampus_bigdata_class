start transaction;
use my_emp;
/*
inner join(교집합) , outer join(차집합) ,cross join(교차조인,데카르트 곱) , full outer join(합집합) , self join(자체 테이블 조인) , 
natural join(동일한 이름을 가진 두 테이블 조인) , equi join(테이블들에 조건,범위)

조인 : 테이블의 컬럼 값에 공통값 (value)를 추출하는 것
using(같은 컬럼명) , on(다른 컬럼명)

1) 내부 조인:
두 테이블 모두에 일치하는 항목이 있으면 행을 반환
조인된 테이블의 행이 일치하지 않으면 행이 반환되지 않는다.

SELECT columns
FROM table1
INNER JOIN table2
ON table1.common_column = table2.common_column;

2)외부 조인:
OUTER JOIN에는 LEFT, RIGHT, FULL의 세 가지 유형
한 테이블의 모든 행과 다른 테이블의 일치하는 행을 반환하는 데 사용. 
일치하는 항목이 없으면 NULL 값을 사용하여 일치 항목이 없는 테이블의 열을 채운다

2-1 LEFT OUTER JOIN 구문
SELECT columns
FROM table1
LEFT OUTER JOIN table2
ON table1.common_column = table2.common_column;

2-2 RIGHT OUTER JOIN은 비슷하지만 두 번째 테이블의 모든 행과 첫 번째 테이블의 일치하는 행을 반환
2-3 FULL OUTER JOIN은 LEFT 및 RIGHT 외부 조인의 결과를 결합한다.
     
- USING 
SELECT columns
FROM table1
JOIN table2
USING (common_column);

- 열 이름이 다른 ON 절
SELECT columns
FROM table1
JOIN table2
ON table1.column_name = table2.other_column_name;

3)CROSS JOIN은 두 테이블의 데카르트 곱을 반환. 
즉, 첫 번째 테이블의 모든 행을 두 번째 테이블의 모든 행과 조인한다 
일반적으로 생성할 수 있는 행 수가 많기 때문에 덜 자주 사용된다.
SELECT columns
FROM table1
CROSS JOIN table2;

*/
-- Q1. inner join
select a.ename , b.dname
from emp as a , dept as b
where a.deptno = b.deptno;

select a.ename , b.dname
from emp as a 
join  dept as b using(deptno);

select a.ename , b.dname
from emp as a 
join  dept as b on a.deptno = b.deptno;


-- Q3)
/*
create table x(
x1 varchar(5),
x2 varchar(5)
);

create table y(
y1 varchar(5),
y2 varchar(5)
);

insert into x values('A','D');

insert  into y values('A','1');
insert  into y values('B','2');
insert  into y  values('C','3');
insert  into y values(null,'1');
*/

select * from x
join y on x.x1 = y.y1 ;

select * from x,y
where x.x1=y.y1;


-- Q5
select * 
from x
right join y on x.x1 = y.y1;

select * 
from x
left join y on x.x1 = y.y1;



select * 
from x
right join y on x.x1 = y.y1
union
select * 
from x
left join y on x.x1 = y.y1;

/*
create table salgrade(
	grade int,
    losal int,
    hisal int
);*/
/*
insert into salgrade values(1,700,1200);
insert into salgrade values(2,1201,1400);
insert into salgrade values(3,1401,2000);
insert into salgrade values(4,2001,3000);
insert into salgrade values(5,3001,9999);
*/

select 
ename ,sal , grade
 from emp
join salgrade on (sal between losal and hisal);

select 
ename ,sal , grade
 from emp,salgrade 
where emp.sal between salgrade.losal and salgrade.hisal;

-- Q8
select 
a.ename ,
a.sal ,
b.grade,
c.dname
 from emp as a
join salgrade as b on (a.sal between b.losal and b.hisal)
join dept as c on a.deptno = c.deptno;

select 
a.ename ,
a.sal ,
b.grade,
c.dname
 from emp as a,
	  salgrade as b,
      dept as c 
where 
a.sal between b.losal and b.hisal
and a.deptno = c.deptno;

-- self join
select a.empno , a.ename ,a.mgr , b.empno , b.ename
from emp as a
left join emp as b on a.mgr = b.empno;


select * from emp natural join dept;

/*
hash join : 테이블 크기, 사용가능한 인덱스 , 메모리 재약 조건
inner join : 테이블 크기,인덱스 요소에 따하 Nested loop join , Merge Join등의 알고리즘

*/

explain
  select a.ename,
		 a.job,
		 a.deptno,
		 b.dname
  from emp as a
  join dept as b on a.deptno = b.deptno
  where b.loc = 'DALLAS';
  
  
  explain
  select a.ename,
		 b.dname
  from emp as a
  join dept as b on a.deptno = b.deptno
  where a.ename like '%A%';


show variables like 'optimizer_switch'
show variables like 'join_buffer_size'

select ename,sal from emp
union
select empno,comm from emp

select * from x
union
select * from y

table x;
table y;

table y intersect distinct table x;

rollback;