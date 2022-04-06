<?php
    $cod = $_POST['cod'];
    $nome = $_POST['nome'];
    $qt = $_POST['qt'];
    $preco = $_POST['preco'];
    $filename = "loja.txt";
    $mode = "a+";   
    $arquivo = fopen($filename, $mode); 
    $quebra="\n";
    if ($arquivo == FALSE) {
        die("Arquivo nao criado");
        $arquivo = fopen($filename,"w+"); 
    }

    if (fwrite($arquivo,($cod.';'.$nome.';'.$qt.';'.$preco).$quebra)) {
        echo "<br/> escrita realizada com sucesso <br/>";
        fclose($arquivo);				
    }


?>