<?php
    if (isset($_GET['tipo'])){
        if ($_GET['tipo'] == 1){
            echo '<h1 class="main">É mais vantajoso escolher o alcool.</h1>';
        }elseif ($_GET['tipo'] == 2){
            echo '<h1 class="main">É mais vantajoso escolher o gasolina.</h1>';
        }
    }
    else{
?>
    <form action="php/controller/combustivelConfig.php" class="form" method="POST">
        <h1 class="form">Dados dos combustiveis</h1>
        <label for="gasolinaValor" class="form">Informe o valor da gasolina</label>
        <input type="number" step=".01" name="gasolinaValor" required class="form">
        <label for="gasolinaRendimento" class="form">Informe o rendimento da gasolina</label>
        <input type="number" step=".01" name="gasolinaRendimento" required class="form">
        <label for="alcoolValor" class="form">Informe o valor do alcool</label>
        <input type="number" step=".01" name="alcoolValor" required class="form">
        <label for="alcoolRendimento" class="form">Informe o rendimento do alcool</label>
        <input type="number" step=".01" name="alcoolRendimento" required class="form">   
        <button type="submit" class="form">Enviar!</button>
    </form>
<?php } ?>