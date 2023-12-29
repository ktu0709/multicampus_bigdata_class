DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PR01_insert`()
BEGIN
insert into emp_test(empno,ename) values(1,1);
END$$
DELIMITER ;
