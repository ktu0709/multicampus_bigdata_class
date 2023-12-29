DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PR02_DEL`(in empno_in int)
BEGIN
delete from emp_test
where empno  = empno_in;
END$$
DELIMITER ;
