select "abc\n de \t f" ; #별칭이 없을경우 컬려명과 값으로 출력
select "abc\n de \t f" as test;


use my_emp;
-- Q1)
select now();

-- Q2)
select * from  my_emp.emp;


-- Q3)
select * from  my_emp.dept;

-- Q4)
use my_emp;
show tables;

-- Q5)
DESC my_emp.emp;

DESC my_emp.dept;
-- Q7)
select deptno,dname from my_emp.dept

-- Q8)
select * from my_emp.dept , my_emp.emp;

-- Q9)
select enams as 'name' , empno as 'no' from my_emp.emp;

-- Q10)

-- Q12)

-- Q13)
select a.ename,a.sal from my_emp.emp as a

/*
select 컬럼리스트
from	테이블리스트
where	조건문,[숫자비교,문자비교,대소문자 비교,NULL,날짜값]
having
group by 
order by 
*/


