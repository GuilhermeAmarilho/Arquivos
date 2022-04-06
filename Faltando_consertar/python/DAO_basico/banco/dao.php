<?php
    require_once("medicamento.php");
    class MedicamentoDAO{
        public function criaConexao(){
            $dbhost = "localhost";
            $dbuser = "admin";
            $dbpass = "admin";
            $db = "banco";
            $conn = mysqli_connect($dbhost,$dbuser,$dbpass,$db);
            if (!$conn) {
                die("Connection failed: " . mysqli_connect_error());
            }
            return $conn;
        }
        public function inserir($med){
            $mysqli = $this->criaConexao();
            $script = "INSERT INTO medicamento (nome,fabricante,controlado,quantidade,preco) VALUES (?, ?, ?, ?, ?)";
            $sql = $mysqli->prepare($script);
            $a = array();
            $a = [$med->getNome(),$med->getFabricante(),$med->getControlado(),$med->getQuantidade(),$med->getPreco()];
            $sql->bind_param('sssid', $a[0],$a[1],$a[2],$a[3],$a[4]);
            $sql->execute();
            mysqli_close($mysql);
        }
        public function remover($cod){
            $mysqli = $this->criaConexao();
            $script = "DELETE from medicamento where cod = (?)";
            $sql = $mysqli->prepare($script);
            $sql->bind_param('i',$cod);
            $sql->execute();
            mysqli_close($mysql);
        }
        public function buscar($tipo,$str){
            $mysqli = $this->criaConexao();
            if($tipo == 1 ){ //busca pelo nome
                $script = "Select * from medicamento where nome like ?";
                $sql = $mysqli->prepare($script);
                $sql->bind_param('s',"%".$str."%");
                $sql->execute();
            }
            if($tipo == 2 ){ //busca pelo fabricante
                $script = "Select * from medicamento where fabricante like ?";
                $sql = $mysqli->prepare($script);
                $sql->bind_param('s',"%".$str."%");
                $sql->execute();
            }
            if($tipo == 3 ){ //busca pelo controlado
                $script = "Select * from medicamento where controlado = ?";
                $sql = $mysqli->prepare($script);
                $sql->bind_param('s',$str);
                $sql->execute();
            }
            if($tipo == 4 ){ //busca pelo id
                $script = "Select * from medicamento where id = ?";
                $sql = $mysqli->prepare($script);
                $sql->bind_param('s',$str);
                $sql->execute();
            }
            return 
            mysqli_close($mysql);
        } 
    }
    $a = new Medicamento("cardio","HP farmaco","S",150,85.2);
    $b = new MedicamentoDAO();
    $b->buscar(2,"MfSB");

?>