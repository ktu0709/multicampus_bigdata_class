use my_emp;

-- Q1)
select bk_idx, isbn, title, rent_cnt 
from book 
where rent_cnt >= 20; 
 
-- Q2)
select bk_idx, isbn, title, reg_date 
from book 
where reg_date > '2020-06-20'; 

-- Q3)
SELECT bk_idx, isbn, title, rent_cnt 
from book
where category = 'B001'
  and rent_cnt = 8;
  
-- Q4)
select bk_idx, isbn, title, author 
from book 
where AUTHOR like '%혜민%'; 
 
-- Q5)
select title 
from book 
where TITLE like '%소설%'; 

-- Q6)
select bk_idx , isbn , title, author, rent_cnt
from book 
where reg_date < '2020-04-15'
and   rent_cnt <= 10;

-- Q7)
select bk_idx , isbn , title, author, rent_cnt
from book 
where title like '나는%';

-- Q8)
select category , 
		avg(rent_cnt) as '평균 대출건수', 
        sum(rent_cnt) as '총 대출건수'
from book 
group by category;

-- Q9)
select bk_idx , isbn , title, author, rent_cnt 
from book 
order by rent_cnt desc
limit 5;

-- Q10)
select bk_idx , isbn , title, author, reg_date 
from book
where category = 'B002'
order by reg_date desc;

-- Q11)
select user_id,
		password,
        email,
        grade,
        tell,
        is_leave
from member
where grade = 'ROLE_USER'
order by user_id;

-- Q12)
select user_id,
		password,
        email,
        grade,
        tell,
        is_leave
from member
where grade = 'ROLE_ADMIN'
and   is_leave = 0;


-- Q13)
select 
        grade
from member
group by grade;


-- Q14)
select user_id,
		password,
        email,
        grade,
        tell,
        is_leave
from member
where grade = 'ROLE_USER'
  and tell like '%9';
  
-- Q15)
select 
        email
from member
where grade = 'ROLE_ADMIN'
and   is_leave = 0  
order by email;

-- Q16)
select 
      user_id,
		password,
        email,
        grade,
        tell,
        is_leave
from member
where grade = 'ROLE_USER'
and   tell like '___-4%' 
and   user_id like '%E'
order by email;

-- Q17)
select bd_idx,
	   user_id,
       reg_date,
       title,
       content,
       #view_count,
       is_del
from board
where content like '%철학%'
  or  title like '%철학%';
  
-- Q18)
select bd_idx,
	   user_id,
       reg_date,
       title,
       content,
       #view_count,
       is_del
from board
order by view_count desc
limit 10;


-- Q20)
select bd_idx,
	   user_id,
       reg_date,
       title,
       content,
       #view_count,
       is_del
from board 
where view_count  >= 30
and   user_id = 'Socrates';

-- Q21)
select bk_idx , 
	   title , 
       author , 
       category,
       case when category like 'B0%' then '문학'
			when category like 'B1%' then '전문서적' end as '대분류'
 from book;
 
 -- Q23)
 select *
 from rent_book
 where state = 'RE01';
 
-- Q24)
 select title
 from rent_master
 where rent_book_cnt >= 2;
 
 -- Q25)
 select bk_idx,
		isbn,
        title,
        reg_date
 from book 
 where reg_date between '2020-06-25' and '2020-06-30';
  
-- Q26)
 select *
 from member_info
 where year(leave_date) = 2023
   and month(leave_date) = 11
;