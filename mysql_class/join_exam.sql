start transaction;

USE MY_EMP;
-- 1. 사원들의 이름, 부서번호, 부서이름을 출력하라.
-- ANSI
  select a.ename,
		 a.deptno,
		 b.dname
  from emp as a
  join dept as b on a.deptno = b.deptno;
  
-- MYSQL 
  select a.ename,
		 a.deptno,
		 b.dname
  from emp as a
  , dept as b
  where a.deptno = b.deptno;



-- 2. DALLAS에서 근무하는 사원의 이름, 직위, 부서번호, 부서이름을
-- 출력하라.
-- ANSI
  select a.ename,
		 a.job,
		 a.deptno,
		 b.dname
  from emp as a
  join dept as b on a.deptno = b.deptno
  where b.loc = 'DALLAS';
  
-- MYSQL 
  select a.ename,
		 a.job,
		 a.deptno,
		 b.dname
  from emp as a
  ,dept as b 
  where  a.deptno = b.deptno
  and b.loc = 'DALLAS';

-- 3. 이름에 'A'가 들어가는 사원들의 이름과 부서이름을 출력하라.
-- ANSI
  select a.ename,
		 b.dname
  from emp as a
  join dept as b on a.deptno = b.deptno
  where a.ename like '%A%';

-- MYSQL 
   select a.ename,
		 b.dname
  from emp as a
  , dept as b 
  where  a.deptno = b.deptno
  and 	 a.ename like '%A%';

-- 4. 사원이름과 그 사원이 속한 부서의 부서명, 그리고 월급을 
-- 출력하는데 월급이 3000이상인 사원을 출력하라.
-- ANSI
  select a.ename,
		 b.dname,
         a.sal
  from emp as a
  join dept as b on a.deptno = b.deptno
  where a.sal >= 3000;
  
-- MYSQL 
  select a.ename,
		 b.dname,
         a.sal
  from emp as a
  , dept as b 
  where  a.deptno = b.deptno
	and  a.sal >= 3000;
 
-- 5. 직위가 'SALESMAN'인 사원들의 직위와 그 사원이름, 그리고
-- 그 사원이 속한 부서 이름을 출력하라.
-- ANSI
  select a.job,
		 a.ename,
		 b.dname
  from emp as a
  join dept as b on a.deptno = b.deptno
  where a.job = 'SALESMAN';
  
-- MYSQL 
  select a.job,
		 a.ename,
		 b.dname
  from emp as a
  , dept as b 
  where a.deptno = b.deptno 
  and	a.job = 'SALESMAN';

-- 6. 커미션이 책정된 사원들의 사원번호, 이름, 연봉, 연봉+커미션,
-- 급여등급을 출력하되, 각각의 컬럼명을 '사원번호', '사원이름',
-- '연봉','실급여', '급여등급'으로 하여 출력하라.

-- ANSI
  select a.empno as '사원번호',
		 a.ename as '사원이름', 
         a.sal *12    as '연봉',
         a.sal*12 + a.comm as '실급여',
         b.grade as '급여등급'
  from emp as a
  left join salgrade as b on a.sal between b.losal and b.hisal
  where a.comm is not null;
  
  
-- MYSQL 
  select a.empno as '사원번호',
		 a.ename as '사원이름', 
         a.sal *12 + a.comm  as '연봉',
         a.sal*12 + a.comm as '실급여',
         b.grade as '급여등급'
  from emp as a
  , salgrade as b 
  where a.sal between b.losal and b.hisal
  and a.comm is not null;

-- 7. 부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름,
-- 월급, 급여등급을 출력하라.
-- ANSI
  select a.deptno,		 
		 b.dname,
         a.ename,
         a.sal,
         c.grade as '급여등급'
  from emp as a
  join dept as b on a.deptno = b.deptno
  left join salgrade as c on a.sal between c.losal and c.hisal
  where a.deptno = 10;

-- MYSQL 
  select a.deptno,		 
		 b.dname,
         a.ename,
         a.sal,
         c.grade as '급여등급'
  from emp as a
  ,dept as b 
  ,salgrade as c
  where  a.deptno = b.deptno
  and	 a.sal between c.losal and c.hisal
  and 	 a.deptno = 10;

-- 8. 부서번호가 10번, 20번인 사원들의 부서번호, 부서이름, 
-- 사원이름, 월급, 급여등급을 출력하라. 그리고 그 출력된 
-- 결과물을 부서번호가 낮은 순으로, 월급이 높은 순으로 
-- 정렬하라.
  
-- ANSI
  select a.deptno,		 
		 b.dname,
         a.ename,
         a.sal,
         c.grade as '급여등급'
  from emp as a
  join dept as b on a.deptno = b.deptno
  left join salgrade as c on a.sal between c.losal and c.hisal
  where a.deptno in (10,20)
  order by a.deptno , a.sal desc;

-- MYSQL 
  select a.deptno,		 
		 b.dname,
         a.ename,
         a.sal,
         c.grade as '급여등급'
  from emp as a
  , dept as b 
  , salgrade as c
  where a.deptno = b.deptno
  and  a.sal between c.losal and c.hisal
  and a.deptno in (10,20)
  order by a.deptno , a.sal desc;

-- 9. 사원번호와 사원이름, 그리고 그 사원을 관리하는 관리자의 
-- 사원번호와 사원이름을 출력하되 각각의 컬럼명을 '사원번호',
-- '사원이름', '관리자번호', '관리자이름'으로 하여 출력하라.
-- ANSI
  select a.empno as '사원번호' , 
	     a.ename as '사원이름',
         b.empno as '관리자번호',
         b.ename as '관리자이름'
from emp as a
left join emp as b on a.mgr = b.empno;
  
-- MYSQL 
  select a.empno as '사원번호' , 
	     a.ename as '사원이름',
         b.empno as '관리자번호',
         b.ename as '관리자이름'
from emp as a
,	 emp as b 
 where  a.mgr = b.empno;

 
-- 10 -자신의 관리자보다 먼저 입사한 모든 사원의 이름 및 입사일을 해당
 -- 관리자의 이름 및입사일과 함게 표시하고 열 이름을 각각 
-- EMPLOYEE,EMPHIREDATE,MANAGER,MGRHIREDATE로 저장한다.

-- ANSI
  select a.ename as 'EMPLOYEE' , 
	     a.hiredate as 'EMPHIREDATE',
         b.ename as 'MANAGER',
         b.hiredate as 'MGRHIREDATE'
from emp as a
left join emp as b on a.mgr = b.empno
where a.hiredate < b.hiredate;


-- MYSQL 
  select a.ename as 'EMPLOYEE' , 
	     a.hiredate as 'EMPHIREDATE',
         b.ename as 'MANAGER',
         b.hiredate as 'MGRHIREDATE'
from emp as a
, 	 emp as b 
where  a.mgr = b.empno
and    a.hiredate < b.hiredate;

-- 11 해당 부서의 모든 사원에 대한 부서 이름, 위치, 사원 수 및 평균 급여를
 -- 표시하는 정의를 작성한다. 
-- 열 이름을 각각 DNAME,LOC,NUMBER OF PEOPLE,SALARY로 한다.
-- ANSI
  select b.dname as 'DNAME' , 
	     b.loc as 'LOC',
         count(ename) as 'NUMBER OF PEOPLE',
         avg(a.sal) as 'SALARY'
from emp as a
left join dept as b on a.deptno = b.deptno
group by b.dname , b.loc;

-- MYSQL 
  select b.dname as 'DNAME' , 
	     b.loc as 'LOC',
         count(ename) as 'NUMBER OF PEOPLE',
         avg(a.sal) as 'SALARY'
from emp as a
, dept as b 
where a.deptno = b.deptno
group by b.dname , b.loc;

rollback;