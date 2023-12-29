CREATE DEFINER=`root`@`localhost` TRIGGER `emp_test_BEFORE_INSERT` BEFORE INSERT ON `emp_test` FOR EACH ROW BEGIN
set new.change_date = now();
END