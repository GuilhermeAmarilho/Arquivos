-- Criar tabelas no PostgreSQL

-- Tabela de Tipo de Curso
CREATE TABLE tipocurso (
    idtipocurso SERIAL PRIMARY KEY,
    nome VARCHAR(45)
);

-- Tabela de Curso
CREATE TABLE curso (
    idcurso SERIAL PRIMARY KEY,
    nome VARCHAR(45),
    idtipocurso INT,
    CONSTRAINT fk_tipocurso
        FOREIGN KEY (idtipocurso)
        REFERENCES tipocurso (idtipocurso)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela de Turma
CREATE TABLE turma (
    idturma SERIAL PRIMARY KEY,
    nome VARCHAR(45),
    ano INT,
    idcurso INT,
    CONSTRAINT fk_curso
        FOREIGN KEY (idcurso)
        REFERENCES curso (idcurso)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela de Aluno
CREATE TABLE aluno (
    idaluno SERIAL PRIMARY KEY,
    nome VARCHAR(300),
    email VARCHAR(300),
    data_nascimento TIMESTAMP,
    cpf VARCHAR(15),
    idturma INT,
    CONSTRAINT fk_turma
        FOREIGN KEY (idturma)
        REFERENCES turma (idturma)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela de Disciplina
CREATE TABLE disciplina (
    iddisciplina SERIAL PRIMARY KEY,
    nome VARCHAR(150),
    idturma INT,
    qtdavaliacoes INT,
    CONSTRAINT fk_turma_disciplina
        FOREIGN KEY (idturma)
        REFERENCES turma (idturma)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela de Avaliação
CREATE TABLE avaliacao (
    idavaliacao SERIAL PRIMARY KEY,
    nome VARCHAR(300),
    iddisciplina INT,
    data DATE,
    CONSTRAINT fk_disciplina_avaliacao
        FOREIGN KEY (iddisciplina)
        REFERENCES disciplina (iddisciplina)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela de Nota
CREATE TABLE nota (
    idnota SERIAL PRIMARY KEY,
    idaluno INT,
    idavaliacao INT,
    valor FLOAT,
    CONSTRAINT fk_aluno_nota
        FOREIGN KEY (idaluno)
        REFERENCES aluno (idaluno)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT fk_avaliacao_nota
        FOREIGN KEY (idavaliacao)
        REFERENCES avaliacao (idavaliacao)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- Tabela de Notificação
CREATE TABLE notificacao (
    idnotificacao SERIAL PRIMARY KEY,
    idaluno INT,
    texto VARCHAR(300),
    data_leitura TIMESTAMP,
    CONSTRAINT fk_aluno_notificacao
        FOREIGN KEY (idaluno)
        REFERENCES aluno (idaluno)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

INSERT INTO tipocurso (nome) VALUES ('Tecnológico'), ('Bacharelado'), ('Licenciatura'), ('técnicos de nível médio');
INSERT INTO curso (nome, idtipocurso) VALUES ('Ciência da Computação', 2), ('Engenharia de Software', 2), ('Matemática', 3), ('Técnico em Informática', 1), ('Ciência da Computação', 1);
INSERT INTO turma (nome, ano, idcurso) VALUES ('Turma A', 2024, 1), ('Turma B', 2024, 2), ('Turma C', 2023, 3), ('Turma TI-2024', 2024, 1), ('CC-1-Fase', 2019, 1);
INSERT INTO aluno (nome, email, data_nascimento, cpf, idturma) VALUES ('João Silva', 'joao.silva@example.com', '2000-05-15', '123.456.789-00', 1), ('Maria Oliveira', 'maria.oliveira@example.com', '1999-11-23', '987.654.321-00', 2), ('Carlos Souza', 'carlos.souza@example.com', '2001-02-10', '159.753.486-00', 3), ('Ana Clara', 'ana.clara@example.com', '2000-03-15', '123.456.789-00', 1), ('João Pedro', 'joao.pedro@example.com', '1999-07-22', '987.654.321-00', 1), ('Maria da Silva', 'mariasilva@gmail.com', '1992-09-25', '016.453.123-89', 1);
INSERT INTO disciplina (nome, idturma, qtdavaliacoes) VALUES ('Programação I', 1, 3), ('Engenharia de Requisitos', 2, 2), ('Cálculo Diferencial', 3, 4), ('Banco de Dados 1', 1, 10);
INSERT INTO avaliacao (nome, iddisciplina, data) VALUES ('Prova 1', 1, '2024-03-15'), ('Trabalho 1', 1, '2024-04-10'), ('Prova 2', 2, '2024-05-20'), ('Prova Final', 3, '2024-06-10'), ('Prova Final', 1, CURRENT_DATE);
INSERT INTO nota (idaluno, idavaliacao, valor) VALUES (1, 1, 8.5), (1, 2, 7.0), (2, 3, 9.0), (3, 4, 6.0), (1, 1, 8.7);
INSERT INTO notificacao (idaluno, texto, data_leitura) VALUES (1, 'Sua nota da Prova 1 foi publicada.', '2024-03-16'), (2, 'Sua nota da Prova 2 foi publicada.', '2024-05-21'), (3, 'Sua nota da Prova Final foi publicada.', NULL);
