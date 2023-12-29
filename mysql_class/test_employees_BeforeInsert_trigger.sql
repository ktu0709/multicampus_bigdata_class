CREATE DEFINER=`root`@`localhost` TRIGGER `test_employees_BEFORE_INSERT` BEFORE INSERT ON `test_employees` FOR EACH ROW BEGIN
	set new.first_name = upper(new.first_name);
    set new.last_name = upper(new.last_name);
END