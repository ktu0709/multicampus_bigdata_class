start transaction;
use my_emp;

SELECT HireYear, 
       GROUP_CONCAT(HireDateCount ORDER BY HireDate ASC SEPARATOR ', ') AS HireInfo
FROM (
    SELECT EXTRACT(YEAR FROM HIREDATE) AS HireYear,
           DATE_FORMAT(HIREDATE, '%Y-%m-%d') AS HireDate,
           COUNT(*) AS NumHires,
           CONCAT(DATE_FORMAT(HIREDATE, '%Y-%m-%d'), ' (', COUNT(*), ')') AS HireDateCount
    FROM EMP
    GROUP BY HireYear, HireDate
) AS SubQuery
GROUP BY HireYear;


-- Q13 이름과 직업을 연결해서 하나의 컬럼을 만들어서 사원번호 결합내용을 별칭으로 출력하자 concat
 select concat(ename ,'-', job)	as test
 from emp;
 
-- Q14 직업의 처음 세글자를 추출해서 출력하자 substr , substring
select substring(job,1,3)
from emp;

-- Q15 사원의 번호, 사원의 이름을 출력하되 사원의 이름의 첫들자만 대문자 나머지 소문자로 출력하자
select concat(UPPER(substring(ename,1,1)),lower(substring(ename,2,100)))
from emp;

-- Q16 사원의 이름, 입사한 날짜(0000년도 00월 00일) 출력하자
select ename,
	  #concat(substring(hiredate,1,4) ,'년', substring(hiredate,6,2),'월',substring(hiredate,9,2),'일')
      date_format(hiredate,'%y년도 %m월 %d일')
from emp;

-- Q17 사원의 이름을 구번째 글자를 기준으로 내림차순 정렬하자
select ename,
		substring(ename,2,1)
from emp
order by substring(ename,2,1) desc;

-- Q18 사원의 이름과 길이를 출력하자
select ename,
		length(ename)
from emp;

-- Q19 사원번호,사원의 이름 , 연봉의 별칭으로 하나의 문자열로 출력하자
select ename,
		concat_ws('-',empno,ename,sal)
from emp;

-- Q20 사원의 이름을 역순으로 출력하자
select ename,
	   reverse(ename)
from emp;

-- base64 : 이메일 -> 텍스트 전용 시스템을 통해서 문제 발생될 부분(프린트 할수없는) 의 인코딩
-- radix-64 : 64를 밑수로 사용하는  것 [a-z,A-Z,0-9]

/*
BASE64 : 바이너리 데이터 각 3byte(24bit)씩 4개의 6bit 그룹으로 나눈다. 
		 6bit 그룹에 2진 데이터를 표현할 수 있는 -> 문자열로 리턴(만일 바이너리 데이터가 3의 배수가) 아닌 경우 패딩문자 = 추가된다.
         
		이진 데이터 분류 -> 문자에 매핑 -> 인코딩 프로세싱 -> 패딩
*/

select to_base64('abc') , from_base64(to_base64('abc'));

select length('text'), char_length('text'),length('한글'),char_length('한글');


show variables like 'secure_file_priv' 
show variables like 'max_allowed_packet' 

select load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\temp.log');
select load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\meadow.jpg');
select load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\my.ini');


create table my_file(
id int auto_increment primary key,
file_content longtext
);

create table my_image(
id int auto_increment primary key,
file_content longblob
);

insert into my_file(file_content)
values(load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\temp.log'));

insert into my_image(file_content)
values(load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\meadow.jpg'));

insert into my_file(file_content)
values(load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\my.ini'));


select * from my_file
select * from my_image

select make_set(1|4,'hello','nice','world',null) as res
select make_set(1|5,'hello','nice','world',null) as res

select weight_string('Hello')

select ename , weight_string(ename)
from emp
order by weight_string(ename); #이름의 기준으로 정렬하겠다 , 

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



rollback;