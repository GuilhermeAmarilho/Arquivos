CREATE TABLE usuario(
	login varchar(250) unique not null,
	nome varchar(200) not null,
	altura float not null,
	idade  integer not null,
	email varchar(500) not null,
	senha varchar(500) not null,
	CONSTRAINT loginpk PRIMARY KEY (login)
);
INSERT INTO usuario (login,nome,altura,idade,email,senha) values ('amarilho' , 'guilherme pereira', 1.79, 16, 'guiamarilho1@gmail.com', md5('12344321')), ('guilherme' , 'guilherme amarilho', 1.82, 18,'guiamarilho1@outlook.com', md5('wukong'));
select * from usuario;