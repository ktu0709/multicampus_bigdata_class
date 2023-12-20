use my_emp;
START TRANSACTION;
/*
SET @v1 = X'41';
SET @v2 = X'41'+0;
SET @v3 = CAST(X'41' AS UNSIGNED);
SELECT @v1, @v2, @v3;

SELECT HEX('cat');
SELECT X'636174';

SET @v1 = X'000D' | X'0BC0';
SET @v2 = _binary X'000D' | X'0BC0';
SELECT HEX(@v1), HEX(@v2);

SELECT b'1000001', CHARSET(b'1000001');
*/
/*
CREATE TABLE t (b BIT(8)); #8 BIT를 사용하겠다 / 부울 값(TRUE,FALSE)
INSERT INTO t SET b = b'11111111';
INSERT INTO t SET b = b'1010';
INSERT INTO t SET b = b'0101';
*/
desc t;


SELECT b,b+0, BIN(b), OCT(b), HEX(b) FROM t;

help bit;

select convert(b,unsigned) from t;



select * from t;
SET SQL_SAFE_UPDATES = 0;
update t set b =b'0101' where b=b'11111111';

delete from t
where b = b'11';

alter table t add c varchar(20);

alter table t drop c;

select true ,false;

select _binary'Hello'; #이진 문자열은 접두어를 사용한 구문을 함께 지정해서 저장한다
select point(10,20); #공간좌표 데이터
select st_astext(point(10,20)); #문자열로 변환 후 출력

/*
Schema Object Names
1. 스키마 개체 유형 : 테이블,뷰,인덱스,시퀀스,프로시저,함수,트리거등
2. 명명규칙 : 이름의 길이,사용할수 있는 문자유형 (일반적으로 영숫자,_,)
3. 고유성 : 단일 스키마 내에서의 이름은 고유
4. 적격스키마 : 스키마 객체를 참조하려면 스키마 명을 명시해야 한다. MY_EMP.EMP SHEMA_NAME.TABLE_TABLE
5. 키워드: 에약어 목록
6. 네임스페이스 : Schema
7. 데이터베이스 호환성 : 데이터 베이스 명세서
*/

-- Q1)
select
year(hiredate) as '입사년도', 
month(hiredate) as '입사월', 
day(hiredate) as '입사일', 
dayname(hiredate) as '입사요일',
DAYOFWEEK(hiredate)
from emp;

-- Q2)
select
extract(year from hiredate) as '입사년도', 
extract(month from hiredate) as '입사월', 
extract(day from hiredate) as '입사일', 
dayname(hiredate) as '입사요일',
case when DAYOFWEEK(hiredate) = 1 then '일요일'
when DAYOFWEEK(hiredate) = 2 then '월요일'
when DAYOFWEEK(hiredate) = 3 then '화요일'
when DAYOFWEEK(hiredate) = 4 then '수요일'
when DAYOFWEEK(hiredate) = 5 then '목요일' 
when DAYOFWEEK(hiredate) = 6 then '금요일' 
when DAYOFWEEK(hiredate) = 7 then '토요일'  end '입사요일'
from emp;

/*
Query Attributes :쿼리문을 실행할 때 쿼리구조,수행작업의 유형, 데이터접근방식, 스키마상태등
데이터 비율/쿼리 실행시 리턴되는 수 = 조인,인덱싱
비용(cost) : CPU 시간, 메모리사용량, 디스크 I/O = 데이터베이스최적화기 = 비용추정 (실행계획)
*/

SHOW VARIABLES LIKE 'character_set_system';
SHOW VARIABLES LIKE 'datadir';

select column_name,character_set_name,collation_name
from information_schema.columns
where table_schema='MY_EMP'
and Table_name = 'T';

show variables like 'character_set_%';
show variables like 'collation%';

select 65535/4;

select rand(100);

rollback;