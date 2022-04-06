<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>documento</title>
</head>
<body>
    <form action="submit.php" method="post">
        <label for="cod">Informe o codigo:</label>  
        <input type="text" name="cod"><br>
        <label for="nome">Informe o nome:</label>  
        <input type="text" name="nome"><br>
        <label for="qt">Informe a quantidade:</label>  
        <input type="text" name="qt"><br>
        <label for="preco">Informe o preço:</label>  
        <input type="text" name="preco"><br>
        <button type="submit">enviar</button>
    </form>
    <a href="lista.php">Leitura de arquivos</a>
</body>
</html>