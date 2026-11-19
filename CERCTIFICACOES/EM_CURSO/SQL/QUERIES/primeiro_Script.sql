-- Criar uma nova base se dados
CREATE  database my_db;

-- Usar/focar a base de dados
USE my_db;

-- Criar uma nova tabela
create table my_table(
	first_name varchar(20),
	age int,
);

-- Alter da tabela, adicionar nova coluna
alter table my_table
add employed BINARY;

-- Alterar tabela, alter coluna
alter TABLE my_table 
ALTER COLUMN first_name varchar(25);

-- Alterar tabela, eliminiar coluna
alter table my_table
drop column employed;

-- Truncar tabela, limpar dados
truncate table my_table;

-- Selecionar, visualizar conteudo
select * from my_table;

drop table my_table;

use master;

drop database my_db;
