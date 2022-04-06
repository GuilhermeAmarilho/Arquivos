<?php 
require_once('inc/header.php');
require_once('back/clienteDAO.php');    
require_once('back/cliente.php');    
$cdao = new ClienteDAO();
$listCli = $cdao->listar(20,0);
?>

  <h2>Listagem de Clientes</h2>
  <table class="table table-sm table-responsive-sm table-hover">
    <thead class="thead-dark">
        <tr>
            <th scope="col">Código</th>
            <th scope="col">Nome</th>
            <th scope="col">CPF</th>
            <th scope="col">E-mail</th>
            <th scope="col">Opções</th>
    </tr>
  </thead>
  <tbody>
    <?php  
        foreach($listCli as $cliente){
    ?>
    <tr>
      <td> <?php echo $cliente->getCod(); ?> </td>
      <td> <?php echo $cliente->getNome(); ?> </td>
      <td> <?php echo $cliente->getCpf(); ?> </td>
      <td> <?php echo $cliente->getEmail(); ?> </td>
      <td> 
      	<a href="cadastro.php?cod=<?php echo $cliente->getCod(); ?>" class="btn btn-sm btn-warning">
          Editar?</a>				
        <a href="excluir.php?cod=<?php echo $cliente->getCod(); ?>" class="btn btn-sm btn-danger"> 					
          Excluir?</a>
      </td>
    </tr>
    <?php } ?>
  </tbody>
</table>
<a href="cadastro.php" class="btn btn-secondary active" role="button" aria-pressed="true">Inserir Cliente</a>



<?php include_once("inc/footer.php");?>






