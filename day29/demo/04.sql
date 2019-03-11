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

delete from students where id = 3;
delete from scores where stuid = 1;

delete from students where id = 1;

/*查询学生的编号，姓名，学生的成绩
	1、查询的内容，是在同一个表中吗？  不是 2个表
	2、这两个表怎么关联呢？						 主外键
*/
-- 笛卡尔积 				  线性代数
select t1.id,t1.sname,t2.score 
from students t1,scores t2
where t1.	id = t2.stuid;	  







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
	 did int,
	 foreign key(did) references dept(id)
);

insert into dept(dname) values('研发部');
insert into dept(dname) values('人事部');
insert into dept(dname) values('财务部');

insert into emp(ename,did) values('老王',1);
insert into emp(ename,did) values('老张',1);
insert into emp(ename,did) values('老赵',1);
insert into emp(ename,did) values('小红',2);
insert into emp(ename,did) values('小丽',2);

select * from dept;
select * from emp;

-- 
/*员工的编号，姓名，部门名字
	1、查询的内容，是在同一个表中吗？  不是 2个表
	2、这两个表怎么关联呢？						 主外键
*/
select emp.id,ename,dname
from emp,dept
where emp.did = dept.id;
