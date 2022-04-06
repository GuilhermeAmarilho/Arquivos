<?php 
require_once('inc/header.php');
require_once('back/clienteDAO.php');    
require_once('back/cliente.php');
$cod = isset($_GET['cod']);

if($cod){
  $cod = $_GET['cod'];
  $cdao = new ClienteDAO();
  $cli = $cdao->buscar(intval($cod));
}
?>
<h2>Cadastro Clientes</h2>

<form action="cadastrar.php" method="post">

  <div class="form-group">
    <label for="nome">Nome</label>
    <input type="text" class="form-control form-control-sm" id="nome" name="nome" 
    value="<?php if($cod) echo $cli->getNome();?>" >
  </div>
  <div class="form-group">
    <label for="email">Endereço de email</label>
    <input type="email" class="form-control form-control-sm" id="email" name="email" placeholder="nome@exemplo.com" 
    value="<?php if($cod) echo $cli->getEmail();?>">
  </div>
  <div class="form-group">
    <label for="cpf">CPF</label>
    <input type="text" class="form-control form-control-sm" id="cpf" name="cpf" placeholder="XXX.XXX.XXX-XX" 
    value="<?php if($cod) echo $cli->getCpf();?>">
  </div>
    <?php if($cod){ ?>
    <input type="hidden" name="cod" value="<?php echo $cli->getCod();?>">
    <?php } ?>
  <div class="form-group">
    <button type="submit" class="btn btn-sm btn-primary" >enviar</button>
    <button type="reset" class="btn btn-sm btn-secondary" >limpar</button>  </div>
</form>

<?php include_once("inc/footer.php");?>
