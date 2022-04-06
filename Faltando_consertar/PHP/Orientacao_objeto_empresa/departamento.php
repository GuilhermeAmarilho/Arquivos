<?php
class Departamento{
    private $nome;
    private $gerente;
    private $funcionarios;
    public function Departamento($nome){
        $this->nome = $nome;
        $this->funcionarios = array();
    }
    public function getNome(){
        return $this->nome;
    }
    public function setNome($nome){
        $this->nome = $nome;
    }
    public function getGerente(){
        return $this->gerente;
    }
    public function setGerente($func){
        $pos =array_search($func, $this->funcionarios, true);
        if($pos!==false){
            $this->gerente = $func;
            return true;
        }
        return false;
    }
    public function alocaFuncionario($func){
        $pos =array_search($func, $this->funcionarios, true);
        if($pos===false) array_push($this->funcionarios, $func);
    }
    public function getFuncionario($pos){
        if(array_key_exists($pos,$this->funcionarios) ) 
        return $this->funcionarios[$pos];
    }
    public function desalocaFuncionario($func){
        $pos =array_search($func, $this->funcionarios, true);
        if($pos!==NULL) {
            if($this->gerente === $func) $this->gerente = NULL; 
            array_splice($this->funcionarios,$pos,1);
        }
    }
    public function __toString(){
        $var = "Nome: ". $this->nome."\n";
        $var .= "Gerente, ".$this->gerente."\nLista funcs:\n";
        foreach($this->funcionarios as $func){
            $var.=$func."\n";
        }
        return $var;
    }
}

?>