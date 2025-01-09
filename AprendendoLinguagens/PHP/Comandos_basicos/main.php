<?php 
    print('Olá Mundo!');
    $nome = "Guilherme";
    $sobrenome = 'Amarilho';
    $nomeCompleto = $nome . " " . $sobrenome;
    echo $nomeCompleto; 
    $nota1 = 8;
    $nota2 = 7;
    echo $nota1 + $nota2, '<br>';
    echo $nota1 - $nota2, '<br>';
    echo $nota1 * $nota2, '<br>';
    echo $nota1 / $nota2, '<br>';
    try {
        echo $nota1 / 0, '<br>';
    } catch (\DivisionByZeroError $th) {
        echo "Não pode dividir por zero!<br />";
    }
    echo $nota1 ** $nota2, '<br />';
    echo $nota1 % $nota2, '<br />';
    $n1 = 5.5;
    $n2 = 2.5465;
    var_dump($n1 + $n2);
    $cores = ['azul', 'verde', 5, ['rosa', 'vermelho']];
    print_r(value: $cores);
    echo '<br />';
    echo $cores[1];
    echo '<br />';
    echo sizeof(value: $cores);
    echo '<br />';
    echo count(value: $cores);
    for($i=0; $i < sizeof(value: $cores); $i++){
        $type = gettype(value: $cores[$i]);
        if ($type == 'array') {
            foreach ($cores[$i] as $chave => $valor) {
                echo $chave;
                echo ' - ';
                print_r(value: $valor);
                echo ' - ';
                echo gettype(value: $valor);
                echo '<br />';
            }
        } else {
            echo $i;
            echo ' - ';
            print_r(value: $cores[$i]);
            echo ' - ';
            echo gettype(value: $cores[$i]);
            echo '<br />';
        }
    }
?>