-- 创建表
drop table if exists  student;
CREATE  TABLE  student (
	id  INT  PRIMARY KEY  ,
	name  VARCHAR(20)  NOT NULL ,
	sex  VARCHAR(1)  ,
	birth  YEAR,
	department  VARCHAR(20) ,
	address  VARCHAR(50) 
);
drop table if exists score;
CREATE  TABLE  score (
id  INT  PRIMARY KEY  AUTO_INCREMENT ,
stu_id  INT(10)  NOT NULL ,
c_name  VARCHAR(20) ,
grade  INT(10)
);
-- 向student表插入记录的INSERT语句如下：
INSERT INTO student VALUES( 901,'张老大', '男',1985,'计算机系', '北京市海淀区');
INSERT INTO student VALUES( 902,'张老二', '男',1986,'中文系', '北京市昌平区');
INSERT INTO student VALUES( 903,'张三', '女',1990,'中文系', '湖南省永州市');
INSERT INTO student VALUES( 904,'李四', '男',1990,'英语系', '辽宁省阜新市');
INSERT INTO student VALUES( 905,'王五', '女',1991,'英语系', '福建省厦门市');
INSERT INTO student VALUES( 906,'王六', '男',1988,'计算机系', '湖南省衡阳市');
-- 向score表插入记录的INSERT语句如下：
INSERT INTO score VALUES(NULL,901, '计算机',98);
INSERT INTO score VALUES(NULL,901, '英语', 80);
INSERT INTO score VALUES(NULL,902, '计算机',65);
INSERT INTO score VALUES(NULL,902, '中文',88);
INSERT INTO score VALUES(NULL,903, '中文',95);
INSERT INTO score VALUES(NULL,904, '计算机',70);
INSERT INTO score VALUES(NULL,904, '英语',92);
INSERT INTO score VALUES(NULL,905, '英语',94);
INSERT INTO score VALUES(NULL,906, '计算机',90);
INSERT INTO score VALUES(NULL,906, '英语',85);
-- 查询
select * from student;
select * from score;




/*查询*/


-- 查询所有的列
select * from student;
-- 查询部分列
select id,name,sex,birth,department,address from student;
-- 查询列，改别名
select id,name,sex,birth,department 系,address 地址 from student;
-- 去重复
select distinct sex from student;
select distinct sex,birth from student;
-- 条件
select * from student
where id > 900 and sex = '男';

select * from student
where id > 900 or sex = '男';

select * from score
where grade>=70 and grade <=80;

select * from score
where grade between 70 and 80;

select * from score
where grade <> 70;

select * from score
where grade != 70;

select * from score
where c_name='计算机' or c_name='英语';

select * from score
where c_name in ('计算机','英语');

select * from score
where c_name  not in ('计算机','英语');

-- 模糊
select * from student
where name like '王%';


select * from student
where name like '%老%';

select * from student
where name like '张_';

-- null
select * from student 
where sex is null;

select * from student 
where sex is not null;

-- 聚合函数

select sum(grade),max(grade),min(grade),avg(grade) from score;

select * from student;
select count(*) from student;

select count(*) from student
where sex is not null;

select count(sex) from student;



-- 分组  注意：分组之后，只能查询被分组的列和聚合函数
select count(*) from student where sex = '男';
select count(*) from student where sex = '女';

select count(*),sex from student
where sex is not null
group by sex;


select avg(grade),c_name
from score
group by c_name;

/*

	过滤条件有两个：
	1、where		分组之前的条件
	2、having   分组之后的条件

	求平均分超过85以上的科目
	
	1、有一个过滤条件  平均分>85
	2、平均分分组之前，还是之后的
		之后，使用having	

	求及格的,平均分超过85以上的科目
	
	1、有两个过滤条件  科目的平均分>85  分数>=60
	2、平均分分组之前，后(having)				前(where)


*/

select avg(grade),c_name
from score
group by c_name
having avg(grade)>85;

select avg(grade),c_name
from score
where grade>=60
group by c_name
having avg(grade)>85;


-- 排序
select * from score 
order by grade;

select * from score 
order by grade asc;

select * from score  
order by grade desc;


-- 分页 每页显示2条(pageSize)，要4页(pageNow)  limit (pageNow-1)*pageSize,pageSize

select * from score 
order by id
limit 0,3;


select * from score 
order by id
limit 6,2;







