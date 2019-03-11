/*如果存在t_person，删除*/
drop table if exists t_person;
/*创建表*/
create table t_person(
	id bigint  primary key auto_increment,
	name varchar(20) not null,
	sex bit not null,
	location varchar(100) default '地址不详',
	idcard char(18) unique,
  isvalid bit default 1
);
/*插入数据*/
insert into t_person(name,sex,location,idcard) values('老王',1,'隔壁的','111111111111111111');
insert into t_person(name,sex,idcard) values('老张',1,'111111111111111112');
insert into t_person(name,sex) values('老赵',1);
/*查询*/
select * from t_person;
/*修改*/
update t_person 
set name = '刘邦' 
where id = 2;

update t_person
set name = '项羽',location = '楚国下相'
where id = 1;

update 
	t_person
set 
	name = '项羽',
	location = '楚国下相'
where 
	id = 1;
/*删除*/
delete from t_person
where id = 3

update t_person
set isvalid = 0
where id = 3

select * from t_person
where isvalid=0;

