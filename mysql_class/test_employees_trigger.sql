CREATE DEFINER=`root`@`localhost` TRIGGER `test_employees_AFTER_INSERT` AFTER INSERT ON `test_employees` FOR EACH ROW BEGIN
update Test_departments
set num_employees = num_employees +1
where id = new.dept_id;
END