package aula14;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
public class Estados {
	private HashMap<String, String> estados;	
	public Estados() {
		this.estados = new HashMap<>();
	}
	public boolean inserirEstado(String sigla, String estado) {
		
		if (!estados.containsKey(sigla)) {
			this.estados.put(sigla, estado);
			return true;
		}else
			return false;		
	}
	public String getEstado(String sigla) {
		return this.estados.get(sigla);
	}
	public void imprimir() {
		for(Entry<String, String> estado: this.estados.entrySet()) {
			System.out.println(estado.getKey() + " - " + estado.getValue());
		}
	}
	public String getSigla(String e) {		
		for(Entry<String, String> estado: this.estados.entrySet()) {		
			if (e.equals(estado.getValue()))
				return estado.getKey();			
		}	
		return null;
	}	
}

// Em outro arquivo 

public class TesteEstados {
	public static void main(String[] args) {
		Estados est = new Estados();
		est.inserirEstado("AC", "Acre");
		est.inserirEstado("AL", "Alagoas");
		est.inserirEstado("BA", "Bahia");
		est.inserirEstado("PR", "Paraná");
		est.inserirEstado("SC", "Santa Catarina");
		est.inserirEstado("RS", "Rio Grande do Sul");
		est.inserirEstado("PA", "Pará");
		est.imprimir();		
		System.out.println(est.getSigla("Alagoas"));
	}
}

