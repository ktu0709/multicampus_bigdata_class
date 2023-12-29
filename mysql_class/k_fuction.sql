use my_exam;
/*
show global variables like 'log_bin_trust_fucntion_creators'
SET GLOBAL log_bin_trust_function_creators = 1;
*/

/*
DETERMINISTIC : 함수가 동일한 입력에 대한 항상 동일한 결과를 리턴
no sql : 함수가 sql데이터를 읽지만 변경하지 않겠다 
reads sql data : 함함수가 sql데이터를 읽지만 변경하지 않겠다 
modifies sql data : 함수가 sql데이터를 읽고 변경하겠다
contains sql : 함수가 sql문을 포함하지만 , 데이터를 변경하지는 않겠다
*/

-- Q1 길이를 리턴하는 사용자 함수
select F01('ABCDEFG');

-- Q2 대문자 변환 사용자 함수
select F02('abcdef');

-- Q3 소문자 변환 사용자 함수
select F03('ABCDEFG');

-- Q4 두 숫자의 합을 리턴하는 함수
select F04(4,5);

-- Q5 최대값 리턴 함수
select F05(8,5);

-- Q6 연도별 나이 계산 함수
select F06('1996-07-09');

-- Q7 문자열 반전 함수
select F07('ABCDEFG');
-- Q8 
select cast('123' as unsigned integer);

select cast('2023-12-23' as date);

select cast(123 as char);

select cast('123.45' as decimal(12.5));

select convert('My SQL' using binary);

set @test = 'My SQL'
select convert(@test using binary);

select convert(emp.ename using binary)
from my_emp.emp
