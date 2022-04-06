create table pessoa(
	codigo serial,
	nome varchar(150) not null,
	salario numeric(7,2) not null,
	sexo varchar(1) not null check ((sexo = 'F') or (sexo = 'M')),
	num_filhos int not null,
	biografia varchar(50000) not null,
	senha varchar(32) not null,
	login varchar(100) not null,
	constraint codigopk primary key (codigo)
)

insert into pessoa(nome,salario,sexo,num_filhos,biografia,senha,login) values ('lorrana', 150.25, 'F',3,'biografia de testes testados', MD5('LOLO'), 'lorrana123');