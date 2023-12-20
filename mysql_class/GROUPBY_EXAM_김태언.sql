use my_exam;

-- Q1)
create table my_report(
name varchar(10),
color varchar(10),
sales int
);

-- Q2)
insert into my_report values('shoes','Red',5200);
insert into my_report values('Wallet','White',3800);
insert into my_report values('shoes','Red',5100);
insert into my_report values('shoes','Black',4600);
insert into my_report values('Wallet','Black',3900);
insert into my_report values('Wallet','White',4000);
insert into my_report values('shoes','Red',5200);

-- Q3)
select name , sum(sales) 
from my_report  
group by name;

-- Q4)
select name, color , sum(sales) 
from my_report  
group by name, color;

-- Q5)
select name, sum(sales)
from my_report  
group by name with rollup;

-- Q6)
select name, color , sum(sales) 
from my_report  
group by name, color;

-- 7)
select name, color , sum(sales) 
from my_report  
group by name, color with rollup;

-- 8)
select name as 'NAME',
		avg(sales) as 'average'
  from my_report 
  where sales >= 150
  group by name
  having avg(sales) >= 200
  