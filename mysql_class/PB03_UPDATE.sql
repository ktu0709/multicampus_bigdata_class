DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PB03_UPDATE`(in m_no int , in m_sal decimal(7,2) )
BEGIN
 update emp_test
 set sal = m_sal
 where empno - m_no;

END$$
DELIMITER ;
