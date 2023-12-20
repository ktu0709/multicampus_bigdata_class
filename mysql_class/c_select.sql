/*
CUBE = 소계 , 총계: GROUP BY 문과 함께 사용되며 GROUP BY 문에서 명시한 
전체 컬럼에서 대하여 추가적인 요약 정보를 단계적으로 만들어 준다
*/

/*
GROUPING : GROUPING 함수는  그룹 기준에서 고려하지 않은 부분 총계인 경우에 1을 리턴하고,
                    그렇지 않은 경우 0을 리턴한다. 
*/

SELECT ENAME, COMM, SUM(COMM) as SUM, GROUPING(ENAME), GROUPING(COMM) 
FROM EMP
GROUP BY ENAME,COMM  WITH ROLLUP;

SELECT job, ename, SUM(sal) as SUM, GROUPING(job), GROUPING(ename) 
FROM EMP
GROUP BY job,ename  WITH ROLLUP;

SELECT job, ename, SUM(sal) as SUM
FROM EMP
GROUP BY job,ename  WITH ROLLUP;

/*---------------ROW_NUMBER()---------------------------
SELECT ROW_NUMBER() [OVER  PARTITION BY, 
                            ORDER BY ]	
                    
 열 A 값의 내림차순으로 일련 번호 리턴 : SELECT ROW_NUMBER() OVER (ORDER BY A DESC);
 
 컬럼 X 의 값으로 그룹핑 분할 하고 ,그 중에서 컬럼 A 의 값의 내림차순으로 일련번호를 리턴
 SELECT ROW_NUMBER() OVER (PARTITION BY X ORDER BY  A DESC);
 
SELECT RANK() OVER  (PARTITION BY,   ORDER BY)	1,2,2,2,5,6,6,8
                    
SELECT DENSE_RANK() OVER  (PARTITION BY,   ORDER BY )	1,2,2,2,3,4,4,5
                    
  */
  
SELECT ROW_NUMBER()  OVER (ORDER BY ENAME ), ENAME
FROM EMP;

SELECT ROW_NUMBER()  OVER (ORDER BY ENAME) as no, ENAME
FROM EMP
order by 1 desc;
 
 -- Q3 사원 테이블에서 사원의 이름이 Z~A 순으로 정렬되고 번호를 매기고 싶다. NO라는 별칭
SELECT ROW_NUMBER()  OVER (ORDER BY ENAME desc) as no, ENAME
FROM EMP;

-- Q3 사원 테이블에서 사원의 이름이 Z~A 순으로 정렬되고 번호를 매기고 싶다. NO라는 별칭 , 홀수 라벨링
SELECT 2*(ROW_NUMBER()  OVER (ORDER BY ENAME desc))-1 as no, ENAME
FROM EMP;

-- Q3 사원 테이블에서 사원의 이름이 Z~A 순으로 정렬되고 번호를 매기고 싶다. NO라는 별칭 , 짝수 라벨링
SELECT 2*(ROW_NUMBER()  OVER (ORDER BY ENAME desc)) as no, ENAME
FROM EMP;

select t1.*
from 
(
SELECT ROW_NUMBER()  OVER (ORDER BY ENAME desc) as no, ENAME
FROM EMP
) as t1 
where no % 2 != 0;

-- Q6.직업별로 번호를 그룹화한후 번호를 출력, 이름순으로 정렬하자 
SELECT ROW_NUMBER()  OVER (PARTITION BY JOB ORDER BY ENAME ), ENAME , job
FROM EMP;

SELECT  RANK() OVER  ( ORDER BY  DAY(HIREDATE))  AS RANK_NO,
        DENSE_RANK() OVER  (  ORDER BY DAY(HIREDATE)) AS DENSE_NO,
        EMPNO, ENAME ,HIREDATE
FROM EMP;
        
SELECT  RANK() OVER  ( ORDER BY  YEAR(HIREDATE))  AS RANK_NO,
        DENSE_RANK() OVER  (  ORDER BY YEAR(HIREDATE)) AS DENSE_NO,
        EMPNO, ENAME ,HIREDATE
FROM EMP;      
  
SELECT  RANK() OVER  ( ORDER BY  MONTH(HIREDATE))  AS RANK_NO,
        DENSE_RANK() OVER  (  ORDER BY MONTH(HIREDATE)) AS DENSE_NO,
        EMPNO, ENAME ,HIREDATE
FROM EMP;  
  
 SELECT  RANK() OVER  ( ORDER BY  DATE(HIREDATE))  AS RANK_NO,
        DENSE_RANK() OVER  (  ORDER BY DATE(HIREDATE)) AS DENSE_NO,
        EMPNO, ENAME ,HIREDATE
FROM EMP;        
        
   SELECT  RANK() OVER  ( ORDER BY  WEEKDAY(HIREDATE))  AS RANK_NO,
        DENSE_RANK() OVER  (  ORDER BY WEEKDAY(HIREDATE)) AS DENSE_NO,
        EMPNO, ENAME ,HIREDATE, WEEKDAY(HIREDATE)
FROM EMP;         

SELECT WEEKDAY('23-01-04'); # 0  ~  6
/*(DATETIME OR DATE)
  YEAR(): 1000 ~  9999  4자리 표시  
  MONTH() : 1 ~ 12
  DAY ()  : 1~  31
  DAYOFMONTH()  = DAY()  
  HOUR() / MINUTE() / SECOND() 
  DATE_ADD( INTERVAL ) , DATE_SUB() 
 
*/
select year(hiredate) from emp;
