<?php
    if (isset($_GET['nome'])){
        echo '<h1 class="main">Resultado do ex2</h1>';
        echo '<br>';
        for ($i = 0; $i < $_GET['qt']; $i++) { 
            echo '<p class="main">'.$_GET['nome'].'</p>';
            echo '<br>';
        }
    }else{
?>
        <form action="php/controller/ex2.php" class="form" method="POST">
            <h1 class="form">Exercício 2</h1>
            <label for="nome" class="form">Informe o nome desejado: </label>
            <input type="text" name="nome" class="form" required>
            <label for="qt" class="form">Informe a quantidade desejada: </label>
            <input type="number" step="1" min="0" name="qt" required class="form">
            <button type="submit" class="form">Enviar!</button>
        </form>
<?php
    }
?>