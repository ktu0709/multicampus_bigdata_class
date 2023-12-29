/*
트리거
데이터 변경 등 명세된 이벤트 발생시 감지하여 자동 실행되는 사용자 정의 프로시저
INSERT, UPDATE, DELETE 명령문의 실행 직전·후 자동으로 호출되어 실행
보통 무결성 제약 조건을 유지하거나 업무 규칙 등을 적용하기 위해 사용
*/
use my_emp;

CREATE TABLE emp_test (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    change_date DATETIME,
    PRIMARY KEY(id)
);
-- 새 행이 emp_test 테이블에 삽입될 때마다 새 행의 change_date 필드가 자동으로 현재 타임스탬프로 설정
-- <<트리거를 추가해보자>>

/*
CREATE DEFINER = CURRENT_USER TRIGGER `my_emp`.`emp_test_BEFORE_INSERT` 
BEFORE INSERT ON `emp_test` FOR EACH ROW
BEGIN
set new.change_date = now();
END
*/

-- 트리거 확인: 설정한 트리거 때문에 change_date 필드는 삽입 시점의 현재 타임스탬프로 자동으로 설정
INSERT INTO emp_test (first_name, last_name) VALUES ('John', 'Doe');

SELECT * FROM emp_test;


/*
TRIGGER: 테이블에서 특정 유형의 작업(예: INSERT, UPDATE 또는 DELETE)에 의해 실행되거나 트리거되는 일련의 명령
DEFAULT:  키워드를 사용하면 테이블을 생성하거나 변경할 때 열에 대한 기본값을 설정(단순고정값)
*/

USE MY_EMP;
-- Q1)  employees 테이블에 새 행이 삽입될 때마다 departments 테이블의 해당 부서에 대한 
 -- num_employees 필드가 자동으로 1씩 증가 시키자.  
CREATE TABLE Test_departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50),
    num_employees INT DEFAULT 0
);


CREATE TABLE Test_employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Test_departments(id)
);

-- 트리거 적용후  
INSERT INTO Test_departments (dept_name, num_employees) VALUES
														('Sales', 0),
														('Marketing', 0),
														('HR', 0),
														('IT', 0);
													
INSERT INTO Test_employees (first_name, last_name, dept_id) VALUES
														('John', 'Doe', 1),
														('Jane', 'Smith', 2),
														('Bob', 'Johnson', 3),
														('Alice', 'Williams', 4);


-- 트리거 추가  
INSERT INTO Test_employees (first_name, last_name, dept_id) VALUES
														('John', 'Doe', 4);
SELECT  * FROM  Test_employees;
SELECT  * FROM   Test_departments;

DROP  TABLE  Test_employees;
DROP  TABLE Test_departments;

-- Q2)  Test_employees 테이블에서 직원이 삭제될 때마다 Test_departments 테이블의 
   -- num_employees 필드를 업데이트하는 트리거를 생성해보자.
   
/*
OLD 및 NEW 키워드는 INSERT, UPDATE 또는 DELETE 작업과 같은 데이터 수정 이벤트
     전후의 열 값을 참조하기 위해 트리거 내에서 사용
OLD: OLD 키워드를 사용하면 행이 업데이트되거나 삭제되기 전에 행의 [원래 값에] 액세스할 수 있다. 
      참조할 기존 행이 필요하므로 UPDATE 및 DELETE 트리거에서만 사용된다.
       UPDATE 트리거에서 OLD.column_name을 사용하면 업데이트되기 전에 
      column_name의 값을 참조할 수 있다.
NEW: NEW 키워드를 사용하면 업데이트되거나 삽입된 행의 [새 값에 액세스]할 수 있다.
     'INSERT' 및 'UPDATE' 트리거에서 사용할 수 있다. 
      INSERT 트리거에서 NEW.column_name은 방금 삽입된 column_name의 값을 제공하며
      UPDATE 트리거에서 업데이트 후 column_name의 새 값을 제공한다. 
*/



DELETE FROM Test_employees WHERE  ID = 1;
SELECT  * FROM  Test_employees;
SELECT  * FROM   Test_departments;



--  Q3) 직원의 이름은 항상 대문자로 저장해야 한다는 규칙을 적용해보자. 
-- 'BEFORE INSERT' 트리거를 생성하여 새 이름을 테이블에 삽입하기 전에 자동으로 대문자로 변환할 수 있다.

INSERT INTO Test_employees (first_name, last_name, dept_id) VALUES
														('John', 'Doe', 4);
SELECT  * FROM  Test_employees;
SELECT  * FROM   Test_departments;