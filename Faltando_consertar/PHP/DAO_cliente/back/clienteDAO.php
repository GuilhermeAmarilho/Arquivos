<?php

class ClienteDAO{

	private function criaConexao(){
		$scon="port=5432 dbname=loja user=postgres password=postgres";
		return pg_connect($scon);
	}

	public function listar($limit, $offset){
		$conn = $this->criaConexao();
		$sql = "SELECT * FROM cliente LIMIT $1 OFFSET $2";
		$res = pg_query_params($conn, $sql, array($limit, $offset));
		
		$listCli = array();
		while($linha = pg_fetch_assoc($res)){
			$cli = new Cliente($linha['nome'],$linha['email'],$linha['cpf']);
			$cli->setCod(intval($linha['codcliente']));
			array_push($listCli,$cli);
		}
		pg_close($conn);
		return $listCli;
	}

	public function buscar($cod){
		$conn = $this->criaConexao();
		$sql = "SELECT * FROM cliente WHERE codcliente = $1";
		$res = pg_query_params($conn, $sql, array($cod));
		$linha = pg_fetch_assoc($res);
		$cli = new Cliente($linha['nome'],$linha['email'],$linha['cpf']);
		$cli->setCod(intval($linha['codcliente']));
		pg_close($conn);
		return $cli;
	} 

	public function inserir($cli){
		$conn = $this->criaConexao();
		$sql2 ="INSERT INTO cliente (nome, cpf, email) VALUES ($1,$2,$3)"; 
		$vetor = array($cli->getNome(), $cli->getCpf(), $cli->getEmail());
		
		pg_query_params($conn, $sql2, $vetor);

		pg_close($conn);
	}

	public function deletar($cod){
		$conn = $this->criaConexao();
		$sql = "DELETE FROM cliente WHERE codcliente = $1";
		$res = pg_query_params($conn, $sql, array($cod));
		pg_close($conn);
	}
	public function alterar($cli){
		$conn = $this->criaConexao();
		$sql="UPDATE Cliente SET nome = $1, cpf = $2, 
		  email = $3 WHERE codcliente = $4 ";
		$vet = array($cli->getNome(), 
		  $cli->getCpf(), $cli->getEmail(), $cli->getCod());
		$res = pg_query_params($conn, $sql, 
		$vet);
		
	}
}
?>
