<?php
    //  Escreva um programa para imprimir os números inteiros entre 1 e 10 na mesma linha, primeiro em ordem crescente e depois em ordem decrescente.  
    $ordem = $_POST['ordem'];
    $valor = $_POST['valor'];
    echo '<script>window.location = "//localhost:8080/index.php?page=ex1&ordem='.$ordem.'&limite='.$valor.'"</script>';
?>