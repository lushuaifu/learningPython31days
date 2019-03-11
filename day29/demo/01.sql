select * from t_student;
insert into t_student values(2,'呵呵呵呵呵呵呵呵呵呵','123456789',NOW())
delete from t_student where id = 1;
select version();
select NOW();


/*创建数据库*/
create database myDatabase charset=utf8;
/*选择数据库*/
use python01;
/*删除数据库*/
drop database myDatabase;
/*查看目前选择的数据库*/
select database();
/*创建表*/
create table Dog(
	id int auto_increment primary key,
	name varchar(20),
);
insert into Dog(id,name) values(1,'老王');
insert into Dog values(2,'老张');
insert into Dog values(30,'老赵');
insert into Dog(name) values('老王');
insert into Dog(name) values('老张');
/*查询所有的列的内容*/
select * from Dog;
/*查部分列*/
select name,id from Dog;
/*新增*/
alter table Dog add brand varchar(20);
/*修改*/
alter table Dog modify brand varchar(10);
/*删除*/
alter table Dog drop column brand;
/*描述表结构*/
desc Dog;
/*删除表*/
drop table Dog;
/*改名字*/
rename table Cat to Dog;
/*查看建表语句*/
show create table Dog;
/*插入*/
drop table Cat;
create table Cat(
	id int auto_increment primary key,
	name varchar(20) not null, 
  color varchar(2),
	sex bit
);
insert into Cat(id,name,color,sex) values(1,'老王','黑',1);
insert into Cat values(2,'老王','黑',1);
insert into Cat(name,color,sex) values('老王','黑',1);
insert into Cat(name,sex) values('老王',0);
insert into Cat(sex) values(0);
select * from Cat;

