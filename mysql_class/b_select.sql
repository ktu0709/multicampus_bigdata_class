use my_emp;
-- Q1.) 전체 테이블 목록을 출력하자.  
show tables;
-- Q2.) 사원의 이름 , 봉급, 커미션을 출력해보자. 
select ename,sal,comm from emp;
-- Q3.)  사원의 이름과 매니저를 출력해보자.  
select ename,mgr from emp;
-- Q4.) 사원의 이름과 연봉을 출력해보자
select ename,sal,comm,sal+comm from emp;

-- Q6.)
select ename,ifnull(sal,0),ifnull(comm,'값 업음'),ifnull(sal,0)+ifnull(comm,0) from emp;

-- Q7)
select ename,sal,ifnull(comm,3000) from emp;

-- Q8)
select ename as '사원의 이름',sal as '봉급',comm as '커미션', sal * 0.15 as '세금' ,ifnull(sal,0) + ifnull(comm,0) - (sal * 0.15) as '급여' from emp;


-- Q9)
select * from emp where deptno = 10;

-- Q10)
select ename , deptno , sal from emp where deptno = 10 and sal >= 1000;

-- Q11)
select ename , deptno  from emp where deptno in (10,20) ;

-- Q12)
select * from emp where right(convert(hiredate,NCHAR(10)),2) = '08';  
select * from emp where hiredate >= '1980-01-01';

-- Q13)
select * from emp where ename like 'A%';

-- Q14)
select * from emp where ename like '%T%T%';

-- Q15)
select * from emp where ename like '%L%L%';

-- Q16)
select * from emp where ename like 'A%' and ename like '%N';

-- Q17)
select * from emp where ename like '_M%';

select avg(sal) from emp where deptno in (10,20);
select job,avg(sal) from emp where job ='salesman';

/*
 -group by
1. group by 문 다음에는 데이터를 구분 짓기위한 표현식으로  해당 테이블의 컬럼 명이나 변수 값 등이 올수 있으며 
        그룹 함수를 사용한 형태는 올 수 없다< group by avg(sal) 안됨>

2. select-list에는 group by문에는 명시된 표현식과  그외 그룹합수를 사용한 표현식만이 올 수있다
     (*는 안됨 )
3. 출력된 결과를 정렬하기 위해 order by 문을 사용하면 된다
  단 order by 문 다음에는 select-list에서 명시된 컬럼 또는   표현식과 컬럼의 별칭(alias), 컬럼 번호 등만 사용

실행순서
from -> GROUP BY -> select -> order by 
*/

select deptno,avg(sal) 
from emp 
where deptno = 10 
group by deptno;

select job,sum(sal) from  emp group by job;
select job,sum(sal) from  emp where job = 'SALESMAN' group by job;
select job,max(sal) from  emp group by job;
select job,min(sal) from  emp group by job;

select deptno,max(sal) from  emp group by deptno;

select ename,comm from emp where comm is not null;

select ename,comm from emp where comm is  null;

select job,sum(sal) from  emp group by job having sum(sal) >= 5000;

select deptno,sum(sal) from  emp group by deptno having sum(sal) >= 10000;

select deptno , ename ,sum(sal)
from emp
group by deptno , ename;

select deptno , ename ,sum(sal)
from emp
group by deptno , ename with rollup;

select job , ename ,sum(sal)
from emp
group by job , ename with rollup;
