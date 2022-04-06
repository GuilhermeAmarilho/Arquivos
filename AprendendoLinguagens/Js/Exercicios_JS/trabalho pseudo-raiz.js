//calcular a pseudo-raiz quiadrada de um numero

var parar,n,rma;
parar=0;
while	(parar!=1) {
	n=parseInt(prompt("Informe um numero inteiro numero: "));
	rma=0;
	while	(n%rma!=0){
		rma++;
	}
	while	((rma*rma)<n) {
		rma++;
	}
	
	if	((rma*rma)!=n) {
		rma--;
	}
	while	(n%rma!=0){
	rma--;
	}
	alert("A pseudo-raiz do numero "+n+" é : "+rma);
	parar=parseInt(prompt("se quiser continuar NÃO aperte 1!"));
}