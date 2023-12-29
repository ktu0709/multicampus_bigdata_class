DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PR06_selectAll`()
BEGIN
select * 
from emp_test;

END$$
DELIMITER ;
