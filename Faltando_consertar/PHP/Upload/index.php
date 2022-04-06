<html>
<head>
   <title>Basic Upload</title>
</head>
<body>
   <form action="#" method="POST" enctype="multipart/form-data">
      <input type="file" name="fileUpload">
      <input type="submit" value="Enviar">
   </form>
</body>
</html>

<?php
    $nome = "gui";
    if(isset($_FILES['fileUpload'])){    
      date_default_timezone_set("Brazil/East"); //Definindo timezone padrão

      $ext = explode(".",$_FILES['fileUpload']['name']);
      $name = $nome.".".date("Y-m-d-H-i-s").".".$ext[1]; //Definindo um novo nome para o arquivo
      $dir = 'C:\Users\guiam\Documents\info\upload\up/'; //Diretório para uploads
      move_uploaded_file($_FILES['fileUpload']['tmp_name'], $dir.$name); //Fazer upload do arquivo
   }
?>