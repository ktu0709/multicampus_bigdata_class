DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PR05_count`(out mcount int)
BEGIN

select count(*) into mcount
 from emp_test;

END$$
DELIMITER ;
