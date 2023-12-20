start transaction;
use my_emp;
# /------------------------------------------------------/
-- percent_rank() over_clause : 결과 집합의 행의 상대적 순위를 계산하는 윈도우 함수
-- 0~1 / 만일 행이 1이면 0이다.
-- 사원 테이블에서 봉급의 백분율 순위를 계산해보자 (상대적 순위)
select sal,
	percent_rank() over(order by sal) as p_rank
    from emp;

select sal,
	percent_rank() over(order by sal) as p_rank,
	rank() over(order by sal) as 'rank'
    from emp;

-- over는 행의 결과 집합이 리턴된다 / 결과 집합의 시작부터 현재 행까지의 모든 행에 대한 누적 합계
select sal,
        sum(sal) over(order by sal)
    from emp;

-- 같은 부서내 모든 사원의 급여의 합계를 내보자
select sal,
	   deptno,
        sum(sal) over(partition by deptno),
        sum(sal) over(partition by deptno order by sal)
    from emp;
    
-- 지정된 날짜까지 입사합 사원의 직원 수를 해보자
select hiredate ,
	   count(*) over(order by hiredate) as res
from emp;    


select  
extract(year from hiredate) as '입사년도',
count(*) as '년도별 입사한 수'	
from emp 
group by hiredate;

-- 사원테이블에서 부서번호와 각 부서(deptno) 직원의 평균 재직 기간(년)을 출력해보자
-- 현재날짜는 오늘날짜로 , 직원이 있는 부서에 대한 계산만 한다   
select  
deptno,
avg(TIMESTAMPDIFF(year,hiredate , sysdate()))
from emp 
group by deptno
having count(deptno) > 0;


-- 사원테이블에서 직업과 사원의 근무가긴의 표준편차를 출력해보자.
select  
job,
std(TIMESTAMPDIFF(year,hiredate , sysdate()))
from emp 
group by job;

-- 부서번호와 각 부서에 대한 봉급의 차이를 출력해보자
-- variance(sal) : 각 부서의 급여차이를 sal를 계산한다
-- 				   분산은 각 부서의 급여가 해당 부서의 평균 급여와 얼마나 다른지 측정하는 것
--                 차이가  클수록 급여간 격차가 더 크다는 것을 의미한다
-- 			      - 급여 분포를 계산한 것
-- 				  variance(sal) 결과가 높다면 해당 부서내 급여 범위가 넓다는 의미이고 일부 직원은
-- 				  다른 직원 보다 훨씬 급여가 많거나 적은 급여를 받는 것을 의미한다.
select  
deptno,
variance(sal)
from emp 
group by deptno;


-- 부서번호와 각 부서에 대한 표본 분산을 출력해보자
-- 전체 데이터 셋이 아닌 하위 집합을 나타날때 사용된다
select  
deptno,
var_samp(sal) as "부서내의 모집단 표본분산"
from emp 
group by deptno;

select  
deptno,
var_pop(sal) as "부서내의 모집단 표본분산"
from emp 
group by deptno;

-- 사원테이블에서 각 부서별 직원 봉급의 표준편차를 계산 해보자
-- sttdev(sal)[over] : 표준편차가 높을수록 급여 범위가 더 넓다
select  
deptno,
stddev(sal) as "부서내의 모집단 표본분산"
from emp 
group by deptno;

select  
deptno,
std(sal)
from emp 
group by deptno;

-- 부서별 사원의 목록을 ,로 나열해서 출력해보자
select deptno,
	   group_concat(ename order by ename asc separator ', ') as res
from emp
group by deptno;

-- 부서별 직업의 목록을 ,로 나영해서 출력해보자
select deptno,
	   group_concat(distinct job  order by job asc separator ', ') as res
from emp
group by deptno;

-- 사원의 테이블에서 연도별 사원이 입사한 날짜를 ,로 나열해보자
select year(hiredate),
	   group_concat(distinct hiredate  order by hiredate asc separator ', ') as res
from emp
group by year(hiredate);

rollback;