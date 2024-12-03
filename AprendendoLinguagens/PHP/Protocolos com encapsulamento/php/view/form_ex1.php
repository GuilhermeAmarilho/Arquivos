<?php
    if (isset($_GET['ordem'])){
        if ($_GET['ordem'] == 'crescente'){
            echo '<div class="main"><br><h1 class="main">Lista Crescente</h1><br>';
            for($i = 1; $i <= $_GET['limite']; $i++){
                echo '<p class="main">'.$i.'</p><br>';
            }
            echo '</div><br>';
        }else{
            echo '<div class="main"><br><h1 class="main">Lista Decrescente</h1><br>';
            for($i = $_GET['limite']; $i > 0; $i--){
                echo '<p class="main">'.$i.'</p><br>';
            }
            echo '</div><br>';
        }
    }
    else{
?>
        <form action="php/controller/ex1.php" class="form" method="POST">
            <h1 class="form">Exercício 1</h1>
            <label for="ordem" class="form">Escolha a ordem desejada: </label>
            <select name="ordem">
                <option value="crescente">Crescente</option>
                <option value="decrescente">Decrescente</option>
            </select>
            <label for="valor" class="form">Informe o valor que dejesa ler: </label>
            <input type="number" step="1" name="valor" min="0" class="form" required>
            <button type="submit" class="form">Enviar!</button>
        </form>
<?php
    }
?>