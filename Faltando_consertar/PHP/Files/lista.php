<?php
require_once('pecas.php');
$arquivo = fopen ('loja.txt', 'r');
$itens = array();
while(!feof($arquivo)){
    $linha = fgets($arquivo, 1024);
    $val = explode(";",$linha);
    $a = new Pecas($val[0],$val[1],$val[2],$val[3]);
    if ($a->getnome() !== NULL){
        array_push($itens, $a);
    }   
}
for ($i=0;$i<count($itens);$i++){
    echo $itens[$i]->getcod().' -- '.$itens[$i]->getnome().' -- '.$itens[$i]->getqt().' -- '.$itens[$i]->getpreco().'<br>';
}

fclose($arquivo);
$a = 0;
$m = 0;
for ($i = 0; $i<count($itens); $i++){
    if ($m < $itens[$i]->getpreco()){
        $m = $itens[$i]->getpreco();
        $a = $i;
    }
}
echo '<h2> O produto de maior preço é o '.$itens[$a]->getnome()." que custa R$ ".$itens[$a]->getpreco().'</h2><br><br>';
$a = 0;$m = 0;
for ($i = 0; $i<count($itens); $i++){
    if ($m < $itens[$i]->getqt()){
        $m = $itens[$i]->getqt();
        $a = $i;
    }
}
echo '<h2> O produto de maior quantidade é o '.$itens[$a]->getnome()." que possui ".$itens[$a]->getqt().' unidades</h2><br><br>';
$a = 0;$m = 0;
for ($i = 0; $i<count($itens); $i++){
    if ($m < ($itens[$i]->getqt() * $itens[$i]->getpreco())){
        $m = ($itens[$i]->getqt() * $itens[$i]->getpreco());
        $a = $i;
    }
}
echo '<h2> O produto '.$itens[$a]->getnome()." possui o maior valor bruto, que é R$".$m.'</h2>'; 
?>