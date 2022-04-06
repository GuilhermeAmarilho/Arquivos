<?php
require_once('back/clienteDAO.php');    
require_once('back/cliente.php');
$cod = $_POST['cod'];
$cli = new Cliente($_POST['nome'],$_POST['email'],$_POST['cpf']);
$cdao = new ClienteDAO();

//se o cod existe então é um UPDATE, senão é um INSERT
if($cod!==null){
    $cli->setCod(intval($cod));
    $cdao->alterar($cli);
}
else{
    $cdao->inserir($cli);
}
//redireciona para o listar.php
header("Location: listar.php");

?>