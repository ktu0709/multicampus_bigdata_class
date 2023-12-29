DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `p`()
BEGIN
declare v int default 1;
CASE v
      WHEN 2 THEN SELECT v;
      WHEN 3 THEN SELECT 0;
      ELSE
        BEGIN
        END;
    END CASE;
END$$
DELIMITER ;
