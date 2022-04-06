<?php
require_once('back/clienteDAO.php');    
$cod = $_GET['cod'];
$cdao = new ClienteDAO();

//se o cod existe então é um UPDATE, senão é um INSERT
if($cod!==null)    $cdao->deletar($cod);


//redireciona para o listar.php
header("Location: listar.php");

?>