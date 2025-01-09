<?php
    //Escreva um programa que peça ao utilizador um nome e um número inteiro (entre 1 e 20). Deverá mostrar esse nome um número de vezes igual a esse valor inteiro.
    $qt = $_POST['qt'];
    $nome = $_POST['nome'];
    echo '<script>window.location = "//localhost:8080/index.php?page=ex2&nome='.$nome.'&qt='.$qt.'"</script>';
?>