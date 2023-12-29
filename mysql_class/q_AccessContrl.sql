/*
트랜잭션의 대표적인 4가지 특성
 ⦁원자성(Atomicity)
원자성은 트랜잭션 안의 SQL 명령문을 모두 성공적으로 실행하여 완료하거나 아니면 모두 
철회하여 무효화해야함을 의미한다. 전부 혹은 전무(all or nothing) 실행 규칙을 적용한다. 

⦁일관성(Consistency)
일관성은 데이터베이스가 트랜잭션 실행 전의 일관된 상태에서 트랜잭션 실행 후에도 또 다
른 일관된 상태로 전환되어야함을 의미한다. 

⦁고립성(Isolation)
고립성은 커밋될 때까지 트랜잭션이 수행한 임시 실행 결과가 다른 트랜잭션에게 공개되지 
않아야함을 의미한다. 
⦁ 지속성(Durability)
지속성은 일단 트랜잭션이 커밋되면 그 트랜잭션의 실행 결과는 장애가 발생하더라도 보존
되어야함을 의미한다
*/



/*
1) MySQL은 데이터베이스, 호스트, 사용자, 테이블, 필드별로 데이터베이스를 조작(브라우징, 삽입, 업데이트, 삭제 등)하는 
 다양한 권한을 설정할 수 있다.
2) 데이터베이스에 액세스 할 수 있는 유저/패스워드/호스트명을 mysql 이라고 하는 데이타베이스에 등록하여 관리한다. 

3) 관리용 테이블 db , host , user , tables_priv , columns_priv 의 5개 
		db :  각 데이터베이스에 대한 액세스 제한
		hose: 호스트별 제한
		user: 사용자가 액세스 제한
		tables_priv	: 테이블에 대한 액세스 제한
		columns_priv: 필드에 대한 액세스 제한
4) db 및 host 테이블은 특정 데이터베이스에 대한 권한을 부여한다.  
  - 와일드카드 문자 `%' 와 `_' 는 Db 테이블과 Host필드에만 사용
  - '%' Host 값은 모든 호스트를 의미
 */



-- mysql  -u root   -p => 'root'@'%'  ,
--  로컬 호스트 접속    mysql  -u  'root'@'localhost'  -p
use mysql;

-- db 테이블 표시
show fields from db;
select * from db;
 

-- 사용자 테이블 표시
show fields from user;
select * from user;

/*
mysqladmin : 관리자 조작 권한  
reload  : 	reload, refresh,flush-privileges, flush-hosts, flush-logs,flush-tables
shutdown :	shutdown
process :	processlist, kill
*/ 
-- 접근 권한 Access Control
/*
  DCL 명령은 데이터베이스에 대한 액세스를 제어하고 사용자 권한을 관리하는 데 사용
1) GRANT: GRANT 명령은 데이터베이스 개체에 대한 사용자 또는 역할에 특정 권한을 제공하는 데 사용.
 권한에는 SELECT, INSERT, UPDATE, DELETE 등과 같은 다양한 작업을 수행할 수 있는 권한이 포함된다.
 
 GRANT를 사용하여 데이터베이스의 데이터에 액세스, 조작 및 수정할 수 있는 사람을 정의한다. 
      GRANT privileges ON object TO user_or_role;
      
2) REVOKE: REVOKE 명령은 사용자 또는 역할에서 이전에 부여된 권한을 제거하는 데 사용
           REVOKE privileges ON object FROM user_or_role;


		
exam) 
-- 로컬 호스트만 접근할 수 있는 new_user 계정생성
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'new_password'; 계정생성

-- 네트워크로 접근할 수 있는 new_user 계정생성
CREATE USER 'new_user'@'%' IDENTIFIED BY 'new_password'; 계정생성

GRANT ALL PRIVILEGES ON my_emp.* TO 'new_user'@'localhost';  권한 부여  

ALTER USER 'new_user'@'localhost' IDENTIFIED BY 'new_password'; 비밀번호 변경  

계정 생성후 권한을 추가로 계속 지정할 수 있다. 
GRANT ALL PRIVILEGES ON my_test.* TO 'existing_user'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON my_emp.table_name TO 'existing_user'@'localhost';

FLUSH PRIVILEGES;  변경사항 즉시 적용 , 서버에 GRANT테이블에 즉시 리로드  
*/
       
desc mysql.user;

select host, user from mysql.user;
       
      -- 계정생성 
create user 'mysample'@'%' identified by 'test';
create user 'mysample'@'localhost' identified by 'test';
select host, user from mysql.user;

-- 권한 확인
show grants for 'mysample'@'%';
show grants for 'mysample'@'localhost';
show databases;
-- 권한 설정  world의 모든 테이블에게 권한설정
GRANT ALL PRIVILEGES  on world.*  to 'mysample'@'%' ;
FLUSH PRIVILEGES;

-- localhost는 world.city만 권한 설정
GRANT ALL PRIVILEGES  on world.city  to 'mysample'@'localhost'; 
FLUSH PRIVILEGES;
-- 

############################################ROLE생성 -> 계정권한부여 ->set 설정  
-- ROLE 생성
CREATE ROLE 'myselect';
CREATE ROLE 'myupdate';
-- ROLE 권한
GRANT SELECT ON *.* TO 'myselect';
GRANT UPDATE ON *.* TO 'myupdate';
-- 계정생성 
CREATE USER 'my_select'@'%' IDENTIFIED BY '111';
CREATE USER 'my_update'@'%' IDENTIFIED BY '111';
-- 권한 부여
GRANT 'myselect' TO 'my_select'@'%';
GRANT 'myupdate' TO 'my_update'@'%';
FLUSH PRIVILEGES;  -- 권한 즉시 적용
show grants for    'my_select'@'%';
show grants for   'my_update'@'%';
-- 각 권한 확인  
###########  myselect, myupdate로 권한을 받은 다음 각 계정으로 접속을 해서 확인한다. 
-- 룰 지정  Create user 권한이 있는 mysql 사용자로 실행해야 SET DEFAULT ROLE 적용된다.  
-- 로그인 했을 경우 사용자에게 부여된 모든 역할이  적용 : 로그인시 권한 활성화  
SET DEFAULT ROLE ALL TO 'my_select'@'%';   -- 계정생성된 권한에 따라 달라진다.  
SET DEFAULT ROLE ALL TO 'my_update'@'%';

-- 권한을 확인한다. 
show grants for    'my_select'@'%';
show grants for   'my_update'@'%';
#############################################################################

-- 권한 해제
REVOKE 'myselect' FROM 'my_select'@'%';
REVOKE SELECT ON *.* FROM 'my_select'@'%';
show grants for 'my_select'@'%';