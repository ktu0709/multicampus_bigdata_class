use my_emp;
create table emp_test
as 
select * from emp

select * from emp_test

call new_procedure()
call PR02_DEL(1)
call PB03_UPDATE(1,100.0)
call PR04_select('FORD')

set @ename = '1'
call PR04_select(@ename)

-- set @mcount = 0 
set @mcount = null

PR05_count(@mcount)
select @mcount

-- Q7
call PR06_selectAll()
call PR07_selectAll()
