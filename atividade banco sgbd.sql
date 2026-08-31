create database yahoo;
use yahoo;

create user 'jose' identified by '123123';
create user 'joaquim' identified by '123123';
create user 'josefino' identified by '123123';
create user 'josue' identified by '123123';
create user 'joca' identified by '123123';   

create role 'equipe_dev';
create role 'equipe_infra';

grant create   , insert  , update  , delete , select , create view
on yahoo.* to 'equipe_dev';
	
grant create, insert, update, delete, select, create view, drop
on yahoo.* to 'equipe_infra';

grant 'equipe_dev' to 'jose';
grant 'equipe_dev' to 'joca';
grant 'equipe_dev' to 'josue';

grant 'equipe_infra' to 'joaquim';
grant 'equipe_infra' to 'josefino';