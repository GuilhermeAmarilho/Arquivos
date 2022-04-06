

<?php
    
    require_once('clienteDAO.php');    
    require_once('cliente.php');    
    
    $cdao = new ClienteDAO();
    $listCli = $cdao->listar(5,0);

    foreach($listCli as $cliente){
        echo $cliente->getNome();
    }
//    var_dump($listCli);

?>

