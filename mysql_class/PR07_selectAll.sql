DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PR07_selectAll`()
BEGIN
declare finished int default false;

declare v_empno int;
declare v_ename varchar(100);
declare v_sal decimal(10,2);
declare v_grade varchar(100);

declare emp_cursor cursor for  select empno,ename,sal from emp_test;
declare continue handler for not found set finished  = True;

-- 1.커서 열기
open emp_cursor;

-- 2 Fetch를 사용해서 테이블의 모든 행을 탐색
	read_loop : loop
		fetch emp_cursor into v_empno,v_ename,v_sal;
        if finished then 
			leave read_loop;
		end if;
        set v_grade = case
					  when v_sal < 2000 then 'LOW'
                      when v_sal between 2000 and 3000 then 'middle'
					  else 'HiGH'
        end;
        
        select v_empno, v_ename , v_sal,v_grade;
end loop;
-- 각행의 추출한 데이터와 급여 등급을 
-- case when then을 이용해서 급여 등굽을 설정
-- 3 커서 닫기
close emp_cursor;
END$$
DELIMITER ;
