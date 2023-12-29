DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PR04_select`(in m_ename varchar(100))
BEGIN
select * 
from emp_test
where ename = m_ename;

END$$
DELIMITER ;
