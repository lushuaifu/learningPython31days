/*随机获取两条数据*/
select * from emp
order by rand()
limit 0,2
/*笛卡尔积*/
select * from emp,dept;
/*内连接*/
select * from emp,dept
where emp.did = dept.id;

select * from dept,emp
where emp.did = dept.id;

select * 
from emp
inner join dept
on emp.did = dept.id;

select * 
from emp left outer join dept
on emp.did = dept.id;

select * 
from dept right outer join emp
on emp.did = dept.id;

select * 
from emp right outer join dept
on emp.did = dept.id;



-- 部门表，员工表
drop table if exists emp;
drop table if exists dept;
create table dept(
	 id int auto_increment primary key,
	 dname varchar(20)
);
create table emp(
	 id int auto_increment primary key,
	 ename varchar(20),
	 did int not null,
	 mgr int, 
	 foreign key(did) references dept(id),
	 foreign key(mgr) references emp(id)
);
insert into dept(dname) values('研发部');
insert into dept(dname) values('人事部');
insert into dept(dname) values('财务部');

insert into emp(ename,did,mgr) values('老王',1,null);
insert into emp(ename,did,mgr) values('老张',1,1);
insert into emp(ename,did,mgr) values('老赵',1,1);
insert into emp(ename,did,mgr) values('小红',2,3);
insert into emp(ename,did,mgr) values('小丽',2,3);

select * from dept;
select * from emp;

/*查询员工额编号，姓名，上级的姓名*/
select * from emp 员工表,emp 上级表
where 员工表.mgr = 上级表.id;

select t1.id,t1.ename,t2.ename
from emp t1,emp t2
where t1.mgr = t2.id;

select t1.id,t1.ename,t2.ename
from emp t1
inner join emp t2
on t1.mgr = t2.id;


select t1.id,t1.ename,t2.ename
from emp t1
left join emp t2
on t1.mgr = t2.id;

select t1.id,t1.ename,t2.ename
from emp t1
right join emp t2
on t1.mgr = t2.id;

drop table if exists scores;
drop table if exists students;
drop table if exists subjects;

create table students(
	id int auto_increment primary key,
	sname varchar(20)
);

create table subjects(
	id int auto_increment primary key,
	stitle varchar(20)
);

/*
create table scores(
	id int auto_increment primary key,
	stuid int,
	subid int,
	score decimal(5,2),
	foreign key(stuid) references students(id),
	foreign key(subid) references subjects(id)
);
*/
create table scores(
	id int auto_increment primary key,
	stuid int,
	subid int,
	score decimal(5,2)
);
alter table scores
add constraint fk_scores_stuid foreign key(stuid)
references students(id) on delete cascade;

alter table scores
add constraint fk_scores_subid foreign key(subid)
references subjects(id) on delete cascade;


insert into students(sname) values('小明');
insert into students(sname) values('小红');
insert into students(sname) values('小丽');
insert into subjects(stitle) values('语文');
insert into subjects(stitle) values('数学');
insert into subjects(stitle) values('英语');

select * from students;
select * from subjects;
select * from scores;

insert into scores(stuid,subid,score) values(1,1,88);
insert into scores(stuid,subid,score) values(1,2,90);
insert into scores(stuid,subid,score) values(2,3,99);
insert into scores(stuid,subid,score) values(3,1,70);


/*查询学生的编号，姓名，科目的名称，成绩*/

select t1.id,t1.sname,t2.stitle,t3.score
from students t1,subjects t2,scores t3
where t3.stuid = t1.id and t3.subid = t2.id;

select t1.id,t1.sname,t2.stitle,t3.score
from scores t3
inner join students t1
on t3.stuid = t1.id 
inner join subjects t2
on t3.subid = t2.id;


select t1.id,t1.sname,t2.stitle,t3.score
from  students t1
inner join scores t3
on t3.stuid = t1.id 
inner join subjects t2
on t3.subid = t2.id;




drop table if exists emp1;
drop table if exists salgrade;
create table emp1(
	 id int auto_increment primary key,
	 sal int
);
create table salgrade(
	 id int auto_increment primary key,
	 low int,
	 high int
);
insert into emp1(sal) values(4000);
insert into emp1(sal) values(5000);
insert into emp1(sal) values(8800);

insert into salgrade(low,high) values(1000,3999);
insert into salgrade(low,high) values(4000,7999);
insert into salgrade(low,high) values(8000,10000);

select * from emp1;
select * from salgrade;

/*查询员工的编号，工资和等级*/
select t1.id,t1.sal,t2.id
from emp1 t1 inner join salgrade t2
on t1.sal between t2.low and t2.high;



/*emp中，查询是经理的人的名字
	1、哪些是经理啊？
	2、再找名字
*/
select ename 
from emp 
where id in(
	select mgr from emp
)



/*查询各学生的语文、数学、英语的成绩*/



select sname,
(select sco.score from scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='语文' and stuid=stu.id) as 语文,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='数学' and stuid=stu.id) as 数学,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='英语' and stuid=stu.id) as 英语
from students stu;

/*函数*/
select ascii('a');
select concat(12,34,'ab','老王');
select length('中a')
select length(ename),ename from emp;
select substring('abc123',2,3);
select trim('  bar   ');
select trim(leading 'x' FROM 'xxxbarxxx');
select trim(both 'x' FROM 'xxxbarxxx');
select trim(trailing 'x' FROM 'xxxbarxxx');
select floor(2.3),ceil(2.3),round(2.3456,2);
select rand();
select year('2016-12-21');


create table t1(
	id int,
	birthday date
);
insert into t1 values(1,'2017-10-20');
insert into t1 values(2,'2017/10/20');
insert into t1 values(3,str_to_date('2017年10月21日','%Y年%m月%d日'));
insert into t1 values('4','2017/10/20');
select * from t1;

/*日期-->字符串*/
select date_format('2017-10-20','%Y年%m月%d日')
/*字符串-->日期*/
select str_to_date('2017年10月20日','%Y年%m月%d日')


select current_date(),now();




/*视图*/
create view myView 
as
select sname,
(select sco.score from scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='语文' and stuid=stu.id) as 语文,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='数学' and stuid=stu.id) as 数学,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='英语' and stuid=stu.id) as 英语
from students stu;


select * from myView;
select sname from myView;


create view myView2
as
select * from emp1;

delete from emp1;
select * from myView2;

drop table if exists bank;
create table bank(
	id int primary key,
	name varchar(20),
	money int 
);
insert into bank values(1,'刘德华',100);
insert into bank values(2,'马德华',1);
select * from bank;
update bank set money = money-10 where id=1;
update bank set money = money+10 where id=2;
select * from bank;
show create table students;

/*事务，一般用来做测试*/
begin;
delete from bank; 
rollback;
commit;

