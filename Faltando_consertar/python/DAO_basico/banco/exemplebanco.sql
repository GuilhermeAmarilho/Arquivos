CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    salario INT NULL,
    PRIMARY KEY(id) 
);

INSERT INTO user (nome,salario) VALUES ("mauricio",10.50),("tamires",25);
DELETE FROM user WHERE id = 2
UPDATE user SET nome = "alan" where id = 5;
SELECT * FROM user LIMIT 10 OFFSET 3;

