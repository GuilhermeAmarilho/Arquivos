<?php
    require_once("funcionario.php");
    require_once("departamento.php");
    $d = new DateTime("09/20/1962");
    $p1 = new Funcionario("Antenor",$d,5000);
    $p2 = new Funcionario("João",new DateTime("09/20/1980"),3000);
    $p3 = new Funcionario("Julio Chefinho",new DateTime("11/10/1980"),3500);
    $p4 = new Funcionario("Hugo Boss",new DateTime("07/11/1985"),8000);
    $p5 = new Funcionario("Maria",new DateTime("12/20/1986"),7500);
    
    $depto1 = new Departamento("TI");
    $depto2 = new Departamento("Gestao");
     
    $depto1->alocaFuncionario($p1);
    $depto1->alocaFuncionario($p2);
    $depto1->alocaFuncionario($p3);
    $depto1->setGerente($p1);
    
    $depto2->alocaFuncionario($p4);
    $depto2->alocaFuncionario($p5);
    echo $depto2->setGerente($p1);
    echo $depto2->setGerente($p4);
    

    echo $depto1;
    echo $depto2."\n---------------------------------------------\n";
    $depto1->desalocaFuncionario($p1);
    $p1->recebeAumento(1987);
    $depto2->alocaFuncionario($p1);
    echo $depto1;
    echo $depto2;
?>