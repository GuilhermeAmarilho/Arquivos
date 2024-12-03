<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/style.css">
        <title>Exercícios em php</title>
    </head>
    <body>
        <header>
            <div class="logo">
                <img src="img/logo_white.png" alt="" class="nav__logo-img">
                <a href="index.php">Amarilho's</a>
            </div>
            <nav>
                <ul>
                    <li><a href="index.php?page=combustivel">Combustível</a></li>
                    <li><a href="index.php?page=ex1">Exercicio 1</a></li>
                    <li><a href="index.php?page=ex2">Exercicio 2</a></li>
                </ul>
            </nav>
        </header>
    <?php
        if (isset($_GET['page'])) {
            if ($_GET['page'] == 'combustivel'){
                include_once('php/view/form_Combustivel.php');
            }
            if ($_GET['page'] == 'ex1'){
                include_once('php/view/form_ex1.php');
            }
            if ($_GET['page'] == 'ex2'){
                include_once('php/view/form_ex2.php');
            }
            if ($_GET['page'] == 'ex3'){
                include_once('php/view/ex3.php');
            }
            if ($_GET['page'] == 'ex4'){
                include_once('php/view/ex4.php');
            }
            if ($_GET['page'] == 'ex5'){
                include_once('php/view/ex5.php');
            }
        }
        else{
            echo('<h1 class="main">Exercícios em PHP</h1>');
        }
    ?>
    </body>
</html>