start transaction;

-- 1) CREATE TABLE로 새 테이블 만들기
-- 2) CREATE TABLE에서 기본 키 (PRIMARY KEY) 제약 조건 지정
-- 3) CREATE TABLE에서 고유 키(UNIQUE KEY) 제약 조건 지정
-- 4) CREATE TABLE에서 검사 (CHECK) 제약 조건 지정
-- 5) CREATE TABLE에서 열에 기본값 지정
-- 6) CREATE TABLE에서 외래 키 (FOREIGN KEY) 제약 조건 지정

--  << 학생 정보를 유지하기 위한 students 테이블 생성 >>- 
/*
student_id: 레코드 ID(정수 유형)  --INT 
student_number: 학생 번호(최대 10자리 문자열 유형) VARCHAR
first_name: 아래 이름(최대 50자리 문자열 유형)  VARCHAR
last_name: 이름(최대 50자리 문자열 유형)VARCHAR 
middle_name: 중간 이름(최대 50자리 문자열 유형) VARCHAR
birthday: 생일(날짜형)   DATE
gender: 성별(문자열 형식으로 M: 남성, F: 여성)  ENUM  
paid_flag : 수업료를 지불했는지 여부 플래그 (BOOL 형식으로 FALSE (0) : 미결제, TRUE (1) : 지불됨) - BOOL  

*/

-- create database students;
use students;

create table students(
student_id int,
student_number varchar(10),
first_name  varchar(50),
last_name	varchar(50),
middle_name varchar(50),
birthday   date,
gender   enum('M','F'),
paid_flag bool
);
insert into students values(1,1,1,1,1,now(),'M',true);
insert into students values(1,1,1,1,1,now(),'F',0);

select * from students;

create table students02(
student_id int,
student_number varchar(10) not null,
first_name  varchar(50),
last_name	varchar(50),
middle_name varchar(50),
birthday   date,
gender   enum('M','F'),
paid_flag bool,
primary key(student_id)
);

desc students02;

insert into students02 values(1,1,1,1,1,now(),'M',true);
insert into students02 values(2,1,1,1,1,now(),'F',0);

select * from students02

create table students03(
student_id int,
student_number varchar(10) not null,
primary key(student_id,student_number)
);

desc students03

create table students04(
student_id int auto_increment,
student_number varchar(10) not null,
primary key(student_id)
);


create table students07(
student_id int,
student_number varchar(10),
birthday date,
unique key (student_id),
check(birthday >= '2000-01-01')
);


desc students07
insert into students07(student_id) values(null);

select * from students07
insert into students07(student_id,birthday) values(1,now());
insert into students07(student_id,birthday) values(2,now());
insert into students07(student_id,birthday) values(3,'1999-09-09');


select * from  information_schema.table_constraints
where table_name = 'students07';

desc information_schema.table_constraints;

create table students05(
student_id int auto_increment,
student_number varchar(10) default 'abc',
primary key (student_id)
);

desc students05;
insert into students05 values(1,1);
insert into students05 values(2,2);
select * from students05;

create table students_my(
student_id int not null,
foreign key(student_id) references students05 (student_id)
);


show keys from students.students_my;


insert into students_my values(1);
select * from students_my;


select * 
from information_schema.table_constraints
where table_name = 'students07';

alter table students03 drop primary key;

alter table students07 drop CHECK students07_chk_1;

alter table students07
add constraint unique key(student_number);

select * 
from information_schema.table_constraints
where table_name = 'students07';

rollback;