<?php
class Funcionario{
    private $nome;
    private $dataNasc;
    private $salario;
    public function Funcionario($nome, $dataNasc, $salario){
        $this->nome=$nome;
        $this->dataNasc = $dataNasc;
        $this->salario = $salario;
    }
    public function getSalario(){
        return $this->salario;
    }
    public function getDataNascimento(){
        return $this->dataNasc;
    }
    public function getNome(){
        return $this->nome;
    }
    public function setNome($nome){
        $this->nome = $nome;
    }
    public function recebeAumento($val){
        if($val>0) $this->salario+=$val;
    }
    public function getIdade(){
        $agora = new DateTime();
        $diferenca = $agora->diff($this->dataNasc); 
        return $diferenca->y." anos";
    }
    public function __toString(){
        return "Nome: ".$this->nome." ".$this->getIdade()." salario:".$this->salario;
    }
}
?>
