<?php

class Cliente{
    private $cod;
    private $nome;
    private $email;
    private $cpf;

    public function Cliente($nome, $email, $cpf){
        $this->nome = $nome;
        $this->email = $email;
        $this->cpf = $cpf;
    }
    public function getCod(){
        return $this->cod;
    }
    public function getNome(){
        return $this->nome;
    }
    public function getCpf(){
        return $this->cpf;
    }
    public function getEmail(){
        return $this->email;
    }
    public function setEmail($email){
        $this->email = $email;
    }
    public function setCpf($cpf){
        $this->cpf = $cpf;
    }
    public function setNome($nome){
        $this->nome = $nome;
    }
    public function setCod($cod){
        $this->cod = $cod;
    }
}

?>