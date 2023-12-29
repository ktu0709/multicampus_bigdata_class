CREATE DEFINER=`root`@`localhost` TRIGGER `test_employees_AFTER_DELETE` AFTER DELETE ON `test_employees` FOR EACH ROW BEGIN
update Test_departments
set num_employees = num_employees -1
where id = old.dept_id;
END