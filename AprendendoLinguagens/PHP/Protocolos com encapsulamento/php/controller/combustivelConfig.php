<?php
    class Combustivel{
        private float $preco;
        private float $kmLitro;
        public function __construct(float $preco, float $kmlitro){
            $this->preco = $preco;
            $this->kmLitro = $kmlitro;
        }
        public function getPreco() : float { 
            return $this->preco;
        }
        public function getKmLitro() : float { 
            return $this->kmLitro;
        }
    }
    class Gasolina extends Combustivel{
        public function __toString() :String{
            return "Gasolina";
        }
    }
    class Alcool extends Combustivel{
        public function __toString() :String{
            return "Alcool";
        }
    }
    $gasolina = new Gasolina($_POST['gasolinaValor'], $_POST['gasolinaRendimento']);
    $alcool = new Alcool($_POST['alcoolValor'], $_POST['alcoolRendimento']);
    $rendimento = $alcool->getKmLitro() / $gasolina->getKmLitro();
    $diferencaPreco =  $alcool->getPreco() / $gasolina->getPreco();
    if($rendimento >=  $diferencaPreco){
        echo '<script>window.location = "//localhost:8080/index.php?page=combustivel&tipo=1"</script>';
    }else{
        echo '<script>window.location = "//localhost:8080/index.php?page=combustivel&tipo=2"</script>';
    }
?>