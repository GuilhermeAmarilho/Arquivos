package aula14;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class Lista {
	public static void main(String[] args) {
		ArrayList<String> l = new ArrayList();
		l.add("Rafael");
		l.add("Julia");
		l.add("Mikenson");
		l.add("Rafael");
		l.add("Erick");
		Collections.sort(l);
		boolean b = l.remove("Julio");
		//System.out.println(l.toString());
		//System.out.println(b);
		String s = l.set(3, "Fabio");
		//System.out.println(s);
		for (String nome : l) {
			System.out.println(nome.toUpperCase());
		}
		String[] v = {"aaa","bbb","ccc"};
		List<String> l2 = Arrays.asList(v);	
	}
}

// Em outro arquivo

public class ListaDePalavras {
	private ArrayList<String> palavras = new ArrayList<>();
	public void adicionarPalavra(String nomeCompleto) {		
		//FABIO JOSE RODRIGUES PINHEIRO
		//NOME[] = {"FABIO", "JOSE", "RODRIGUES", "PINHEIRO"};
		String[] nome = nomeCompleto.split(" ");
		String primeiroNome = nome[0];
		//String ultimoNome = nome[nome.length-1];	
		this.palavras.add(primeiroNome);
		//this.palavras.add(ultimoNome);			
	}
	public void escreverLista() {
				
		for (String p : palavras) {
			System.out.println(p);
		}
	}
	public int conta(String nome) {
		int qtd = 0;
		
		for (String palavra : palavras) {
			if (palavra.equals(nome))
				qtd++;
		}		
		return qtd;
	}
}