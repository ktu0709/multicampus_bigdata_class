start transaction;

show variables like 'regexp_stack_limit';
show variables like 'regexp_time_limit';

-- 1 사원이름에서 J로 시작하는 이름을 찾자
select ename
from emp
where ename regexp '^J';

-- 2 사원이름이 ER로 끝나는 이름을 찾아보자 
select ename
from emp
where ename regexp 'ER$';

-- 3 사원이름이 S이 들어있는 이름을 찾아보자 
select ename
from emp
where ename regexp 'S';

-- 4 사원이름이 숫자가 들어있는 이름을 찾아보자 
select ename
from emp
where ename regexp '[0-9]';

-- 5 사원이름이 두번째 문자가 'A'인 찾아보자 
-- ^ 문자열의 시작 앵커
-- . 단일문자와 일치하는 와일드 카드(개행문자 제외)
-- [A] []안에 문자와 일치
-- ^.[A} : 임의의 문자 .으로 시작하고 바로 뒤에 오는 문자 A가 일치하는 모든 문자열
select ename
from emp
where ename regexp '^.[A]';

select ename
from emp
where ename regexp '^..[A]';

-- 사원이름에서 JOHE 또는 JONE 라는 이름을 출력해보자.
select ename
from emp
where ename regexp 'JO(HE|NE)';

-- 사원이름에서 이름이 5글자라는 이름을 출력해보자.
select ename
from emp
where ename regexp '^.{5}$';

-- J로 시작하고 S로 끝나는 모든 내용을 출력하자
select ename
from emp
where ename regexp '^J[A-Z]*S$';

-- 직업이 대문자인 사원만 출력하자. + = 1, MORE
select job
from emp
where job regexp '^[A-Z]+$';


/*
regexp_instr()
REGEXP_INSTR(expr, pat[, pos[, occurrence[, return_option[, match_type]]]])
REGEXP_INSTR(검색할 문자열, 패턴, 위치, 일치항목,반환옵션,유형옵션)
*/

select regexp_instr('Hello, World!','o');
select regexp_instr('Hello, World!','o',1,2);
select regexp_instr('Hello, World!','W',1,1,0,'c');

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+',1,3);

-- 이메일 패턴 , 전화번호 패턴 , 우편번호 패턴 , 주민번호 , 운전면허 ,  여권 패턴, 은행 계좌번호,url 패턴


rollback;