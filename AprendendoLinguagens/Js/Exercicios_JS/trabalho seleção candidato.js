//{ Variaveis
var gp1,gp2,gp3,gp4,gp5,gp6,gp7,gp8,gp9,gp10,gp11,gp12,gp13,gp14,gp15,gm1,gm2,gm3,gm4,gm5,gm6,gm7,gm8,gm9,gm10,gm11,gm12,gm13,gm14,gm15,gce1,gce2,gce3,gce4,gce5,gce6,gce7,gce8,gce9,gce10,gce11,gce12,gce13,gce14,gce15,gce16,gce17,gce18,gce19,gce20,rp1,rp2,rp3,rp4,rp5,rp6,rp7,rp8,rp9,rp10,rp11,rp12,rp13,rp14,rp15,rm1,rm2,rm3,rm4,rm5,rm6,rm7,rm8,rm9,rm10,rm11,rm12,rm13,rm14,rm15,rce1,rce2,rce3,rce4,rce5,rce6,rce7,rce8,rce9,rce10,rce11,rce12,rce13,rce14,rce15,rce16,rce17,rce18,rce19,rce20,
//}
//{ parte 2
nome="";
np=0;
nm=0;
nce=0;
nf=0;
np1=0;
nm1=0;
nce1=0;
nf1=0;
candpas1="Não"
np2=0;
nm2=0;
nce2=0;
nf2=0;
candpas2="Não"
np3=0;
nm3=0;
nce3=0;
nf3=0;
candpas3="Não"
ac1=0;
ac2=0;
ac3=0;
err1=0;
err2=0;
err3=0;
//}
//{	parte 2
gp1=parseInt(prompt("Informe a resposta da questão nº 1 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp2=parseInt(prompt("Informe a resposta da questão nº 2 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp3=parseInt(prompt("Informe a resposta da questão nº 3 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp4=parseInt(prompt("Informe a resposta da questão nº 4 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp5=parseInt(prompt("Informe a resposta da questão nº 5 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp6=parseInt(prompt("Informe a resposta da questão nº 6 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp7=parseInt(prompt("Informe a resposta da questão nº 7 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp8=parseInt(prompt("Informe a resposta da questão nº 8 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp9=parseInt(prompt("Informe a resposta da questão nº 9 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp10=parseInt(prompt("Informe a resposta da questão nº 10 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp11=parseInt(prompt("Informe a resposta da questão nº 11 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp12=parseInt(prompt("Informe a resposta da questão nº 12 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp13=parseInt(prompt("Informe a resposta da questão nº 13 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp14=parseInt(prompt("Informe a resposta da questão nº 14 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gp15=parseInt(prompt("Informe a resposta da questão nº 15 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));	
gm1=parseInt(prompt("Informe a resposta da questão nº 1 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm2=parseInt(prompt("Informe a resposta da questão nº 2 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm3=parseInt(prompt("Informe a resposta da questão nº 3 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm4=parseInt(prompt("Informe a resposta da questão nº 4 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm5=parseInt(prompt("Informe a resposta da questão nº 5 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm6=parseInt(prompt("Informe a resposta da questão nº 6 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm7=parseInt(prompt("Informe a resposta da questão nº 7 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm8=parseInt(prompt("Informe a resposta da questão nº 8 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm9=parseInt(prompt("Informe a resposta da questão nº 9 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm10=parseInt(prompt("Informe a resposta da questão nº 10 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm11=parseInt(prompt("Informe a resposta da questão nº 11 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm12=parseInt(prompt("Informe a resposta da questão nº 12 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm13=parseInt(prompt("Informe a resposta da questão nº 13 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm14=parseInt(prompt("Informe a resposta da questão nº 14 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gm15=parseInt(prompt("Informe a resposta da questão nº 15 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));	
gce1=parseInt(prompt("Informe a resposta da questão nº 1 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce2=parseInt(prompt("Informe a resposta da questão nº 2 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce3=parseInt(prompt("Informe a resposta da questão nº 3 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce4=parseInt(prompt("Informe a resposta da questão nº 4 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce5=parseInt(prompt("Informe a resposta da questão nº 5 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce6=parseInt(prompt("Informe a resposta da questão nº 6 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce7=parseInt(prompt("Informe a resposta da questão nº 7 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce8=parseInt(prompt("Informe a resposta da questão nº 8 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce9=parseInt(prompt("Informe a resposta da questão nº 9 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce10=parseInt(prompt("Informe a resposta da questão nº 10 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce11=parseInt(prompt("Informe a resposta da questão nº 11 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce12=parseInt(prompt("Informe a resposta da questão nº 12 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce13=parseInt(prompt("Informe a resposta da questão nº 13 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce14=parseInt(prompt("Informe a resposta da questão nº 14 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce15=parseInt(prompt("Informe a resposta da questão nº 15 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce16=parseInt(prompt("Informe a resposta da questão nº 16 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce17=parseInt(prompt("Informe a resposta da questão nº 17 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce18=parseInt(prompt("Informe a resposta da questão nº 18 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce19=parseInt(prompt("Informe a resposta da questão nº 19 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
gce20=parseInt(prompt("Informe a resposta da questão nº 20 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E"));
//}
//{ parte 3
while	(j!=2) {
	j=prompt(" : ")
	np=0;
	nm=0;
	nce=0;
	nf=0;
	nome=prompt("Informe seu nome: ");
	//{ respostas
	rp1=parseInt(prompt("Informe sua  resposta para a questão nº 1 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp2=parseInt(prompt("Informe sua  resposta para a questão nº 2 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp3=parseInt(prompt("Informe sua  resposta para a questão nº 3 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp4=parseInt(prompt("Informe sua  resposta para a questão nº 4 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp5=parseInt(prompt("Informe sua  resposta para a questão nº 5 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp6=parseInt(prompt("Informe sua  resposta para a questão nº 6 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp7=parseInt(prompt("Informe sua  resposta para a questão nº 7 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp8=parseInt(prompt("Informe sua  resposta para a questão nº 8 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp9=parseInt(prompt("Informe sua  resposta para a questão nº 9 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp10=parseInt(prompt("Informe sua  resposta para a questão nº 10 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp11=parseInt(prompt("Informe sua  resposta para a questão nº 11 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp12=parseInt(prompt("Informe sua  resposta para a questão nº 12 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp13=parseInt(prompt("Informe sua  resposta para a questão nº 13 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp14=parseInt(prompt("Informe sua  resposta para a questão nº 14 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rp15=parseInt(prompt("Informe sua  resposta para a questão nº 15 da prova de português:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));		
	rm1=parseInt(prompt("Informe sua  resposta para a questão nº 1 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm2=parseInt(prompt("Informe sua  resposta para a questão nº 2 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm3=parseInt(prompt("Informe sua  resposta para a questão nº 3 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm4=parseInt(prompt("Informe sua  resposta para a questão nº 4 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm5=parseInt(prompt("Informe sua  resposta para a questão nº 5 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm6=parseInt(prompt("Informe sua  resposta para a questão nº 6 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm7=parseInt(prompt("Informe sua  resposta para a questão nº 7 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm8=parseInt(prompt("Informe sua  resposta para a questão nº 8 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm9=parseInt(prompt("Informe sua  resposta para a questão nº 9 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm10=parseInt(prompt("Informe sua  resposta para a questão nº 10 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm11=parseInt(prompt("Informe sua  resposta para a questão nº 11 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm12=parseInt(prompt("Informe sua  resposta para a questão nº 12 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm13=parseInt(prompt("Informe sua  resposta para a questão nº 13 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm14=parseInt(prompt("Informe sua  resposta para a questão nº 14 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rm15=parseInt(prompt("Informe sua  resposta para a questão nº 15 da prova de Matemática:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));	
	rce1=parseInt(prompt("Informe sua  resposta para a questão nº 1 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce2=parseInt(prompt("Informe sua  resposta para a questão nº 2 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce3=parseInt(prompt("Informe sua  resposta para a questão nº 3 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce4=parseInt(prompt("Informe sua  resposta para a questão nº 4 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce5=parseInt(prompt("Informe sua  resposta para a questão nº 5 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce6=parseInt(prompt("Informe sua  resposta para a questão nº 6 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce8=parseInt(prompt("Informe sua  resposta para a questão nº 8 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce9=parseInt(prompt("Informe sua  resposta para a questão nº 9 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce10=parseInt(prompt("Informe sua  resposta para a questão nº 10 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce11=parseInt(prompt("Informe sua  resposta para a questão nº 11 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce12=parseInt(prompt("Informe sua  resposta para a questão nº 12 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce13=parseInt(prompt("Informe sua  resposta para a questão nº 13 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce14=parseInt(prompt("Informe sua  resposta para a questão nº 14 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce15=parseInt(prompt("Informe sua  resposta para a questão nº 15 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce16=parseInt(prompt("Informe sua  resposta para a questão nº 16 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce17=parseInt(prompt("Informe sua  resposta para a questão nº 17 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce18=parseInt(prompt("Informe sua  resposta para a questão nº 18 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce19=parseInt(prompt("Informe sua  resposta para a questão nº 19 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	rce20=parseInt(prompt("Informe sua  resposta para a questão nº 20 da prova de Conhecimentos Gerais:\n 1 - A\n 2 - B\n 3 - C\n 4 - D\n 5 - E\n 6 - Não Sei!"));
	//}
	//{	Notas
	//{ nota de portugues 1
	if	(rp1==gp1) {
		ac1++;
	}
	if	((rp1!=gp1)&&(rp1!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 2
	if	(rp2==gp2) {
		ac1++;
	}
	if	((rp2!=gp2)&&(rp2!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 3
	if	(rp3==gp3) {
		ac1++;
	}
	if	((rp3!=gp3)&&(rp3!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 4
	if	(rp4==gp4) {
		ac1++;
	}
	if	((rp4!=gp4)&&(rp4!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 5
	if	(rp5==gp5) {
		ac1++;
	}
	if	((rp5!=gp5)&&(rp5!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 6
	if	(rp6==gp6) {
		ac1++;
	}
	if	((rp6!=gp6)&&(rp6!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 7
	if	(rp7==gp7) {
		ac1++;
	}
	if	((rp7!=gp7)&&(rp7!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 8
	if	(rp8==gp8) {
		ac1++;
	}
	if	((rp8!=gp8)&&(rp8!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 9
	if	(rp9==gp9) {
		ac1++;
	}
	if	((rp9!=gp9)&&(rp9!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 10
	if	(rp10==gp10) {
		ac1++;
	}
	if	((rp10!=gp10)&&(rp10!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 11
	if	(rp11==gp11) {
		ac1++;
	}
	if	((rp11!=gp11)&&(rp11!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 12
	if	(rp12==gp12) {
		ac1++;
	}
	if	((rp12!=gp12)&&(rp12!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 13
	if	(rp13==gp13) {
		ac1++;
	}
	if	((rp13!=gp13)&&(rp13!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 14
	if	(rp14==gp14) {
		ac1++;
	}
	if	((rp14!=gp14)&&(rp14!=6)){
		err1++;
	}
	//}	
	//{ nota de portugues 15
	if	(rp15==gp15) {
		ac1++;
	}
	if	((rp15!=gp15)&&(rp15!=6)){
		err1++;
	}
	//}
	//{	nota de matematica 1
	if	(rm1==gm1){
		ac2++;
	}	
	if	((rm1!=gm1)%%(rm1!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 2
	if	(rm2==gm2){
		ac2++;
	}	
	if	((rm2!=gm2)%%(rm2!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 3
	if	(rm3==gm3){
		ac2++;
	}	
	if	((rm3!=gm3)%%(rm3!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 4
	if	(rm4==gm4){
		ac2++;
	}	
	if	((rm4!=gm4)%%(rm4!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 5
	if	(rm5==gm5){
		ac2++;
	}	
	if	((rm5!=gm5)%%(rm5!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 6
	if	(rm6==gm6){
		ac2++;
	}	
	if	((rm6!=gm6)%%(rm6!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 7
	if	(rm7==gm7){
		ac2++;
	}	
	if	((rm7!=gm7)%%(rm7!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 8
	if	(rm8==gm8){
		ac2++;
	}	
	if	((rm8!=gm8)%%(rm8!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 9
	if	(rm9==gm9){
		ac2++;
	}	
	if	((rm9!=gm9)%%(rm9!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 10
	if	(rm10==gm10){
		ac2++;
	}	
	if	((rm10!=gm10)%%(rm10!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 11
	if	(rm11==gm11){
		ac2++;
	}	
	if	((rm11!=gm11)%%(rm11!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 12 
	if	(rm12==gm12){
		ac2++;
	}	
	if	((rm12!=gm12)%%(rm12!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 13
	if	(rm13==gm13){
		ac2++;
	}	
	if	((rm13!=gm13)%%(rm13!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 14 
	if	(rm14==gm14){
		ac2++;
	}	
	if	((rm14!=gm14)%%(rm14!=6)){
		err2++;
	}
	//}	
	//{	nota de matematica 15
	if	(rm15==gm15){
		ac2++;
	}	
	if	((rm15!=gm15)%%(rm15!=6)){
		err2++;
	}
	//}	
	//{ nota de conhecimentos especificos 1
	if	(rce1==gce1){
		ac3++;
	}	
	if	((rce1!=gce1))&&(rce1!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 2
	if	(rce2==gce2){
		ac3++;
	}	
	if	((rce2!=gce2))&&(rce2!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 3
	if	(rce3==gce3){
		ac3++;
	}	
	if	((rce3!=gce3))&&(rce3!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 4
	if	(rce4==gce4){
		ac3++;
	}	
	if	((rce4!=gce4))&&(rce4!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 5
	if	(rce5==gce5){
		ac3++;
	}	
	if	((rce5!=gce5))&&(rce5!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 6
	if	(rce6==gce6){
		ac3++;
	}	
	if	((rce6!=gce6))&&(rce6!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 7
	if	(rce7==gce7){
		ac3++;
	}	
	if	((rce7!=gce7))&&(rce7!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 8
	if	(rce8==gce8){
		ac3++;
	}	
	if	((rce8!=gce8))&&(rce8!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 9
	if	(rce9==gce9){
		ac3++;
	}	
	if	((rce9!=gce9))&&(rce9!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 10
	if	(rce10==gce10){
		ac3++;
	}	
	if	((rce10!=gce10))&&(rce10!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 11
	if	(rce11==gce11){
		ac3++;
	}	
	if	((rce11!=gce11))&&(rce11!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 12
	if	(rce12==gce12){
		ac3++;
	}	
	if	((rce12!=gce12))&&(rce12!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 13
	if	(rce13==gce13){
		ac3++;
	}	
	if	((rce13!=gce13))&&(rce13!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 14
	if	(rce14==gce14){
		ac3++;
	}	
	if	((rce14!=gce14))&&(rce14!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 15
	if	(rce15==gce15){
		ac3++;
	}	
	if	((rce15!=gce15))&&(rce15!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 16
	if	(rce16==gce16){
		ac3++;
	}	
	if	((rce16!=gce16))&&(rce16!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 17
	if	(rce17==gce17){
		ac3++;
	}	
	if	((rce17!=gce17))&&(rce17!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 18
	if	(rce18==gce18){
		ac3++;
	}	
	if	((rce18!=gce18))&&(rce18!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 19
	if	(rce19==gce19){
		ac3++;
	}	
	if	((rce19!=gce19))&&(rce19!=6)){
		err3++;
	}
	//}	
	//{ nota de conhecimentos especificos 20
	if	(rce20==gce20){
		ac3++;
	}	
	if	((rce20!=gce20))&&(rce20!=6)){
		err3++;
	}
	//}
	//}
	np=10*(ac1-(0.2*err1))/15
	nm=10*(ac2-(0.2*err2))/15
	nce=10*(ac3-(0.2*err3))/20
	nf=(2*np+2*nm+6*nce)/10
	if	(nce>6){
		if	(nm>6){
			if	(np>6){
				var	capto;
				capto=1;
			}
			else{
				var	capto;
				capto=0;
			}
		}
		else{
			var	capto;
			capto=0;
		}
	}
	else{
	var	capto;
	capto=0;
	}
}
//}


