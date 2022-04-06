<?php
class Pecas{
    private $cod;
    private $nome;
    private $qt;
    private $preco; 
    public function Pecas($cod,$nome,$qt,$preco){
        $this->cod = $cod;
        $this->nome = $nome; 
        $this->qt = floatval($qt);
        $this->preco = floatval($preco);
    }
    public function setcod($cod){
        $this->cod = $cod;
    }
    public function setnome($nome){
        $this->nome = $nome;
    }
    public function setqt($qt){
        $this->qt = floatval($qt);
    }
    public function setpreco($preco){
        $this->preco = floatval($preco);
    }
    public function getcod(){
        return $this->cod;
    }
    public function getnome(){
        return $this->nome;
    }
    public function getqt(){
        return $this->qt;
    }
    public function getpreco(){
        return $this->preco;
    }
}
?>