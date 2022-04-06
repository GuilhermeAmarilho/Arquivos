CREATE TABLE pessoa(
    id SERIAL UNIQUE,
    nome varchar(50) NOT NULL,
    idade int NOT NULL,
    CONSTRAINT nomepessoa PRIMARY KEY(nome)
);

insert into pessoa(nome, idade) values ('guilherme',13),('lucas',5),('lorrana',10);
select * from pessoa;