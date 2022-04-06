//crie um menu de pedidos de uma lanchonete usando switch e break onde a pessoa pode pedir mais de alguma coisa


var l1,vl1,l2,vl2,l3,vl3,l4,vl4,p1,vp1,p2,vp2,p3,vp3,p4,vp4,a1,va1,a2,va2,b1,vb1,b2,vb2,b3,vb3,b4,vb4,b5,b6,vb6,b7,vb7,b8,vb8,vo,C,M,Q,B,QB,OU,X,V,V1,Y;

alert("Ola.\nPizzaria e lancheria IFRS.");

//menu


l1="Bauru de frango";
vl1=15;
l2="Bauru de carne";
vl2=16;
l3="Bauru de coração";
vl3=16;
l4="Bauru de salada";
vl4=14;
l5="Bauru tudo(Varios tipos de carnes)";
vl5=22;
l6="Xis tudo(Varios tipos de carnes)";
vl6=13;
l7="Xis filé";
vl7=9.90;
l8="Xis calabresa";
vl8=10.50;


p1="Pizza de calabresa grande";
vp1=46;
p2="Pizza de calabresa media";
vp2=32;
p3="Pizza de mussarela grande";
vp3=42;
p4="Pizza de mussarela media";
vp4=28;
p5="Pizza de strogonoff grande";
vp5=43;
p6="Pizza de strogonoff media";
vp6=29;
p7="Pizza de frango grande";
vp7=39;
p8="Pizza de frango media";
vp8=25;


a1="Porção de fritas 1Kg";
va1=15.5;
a2="Porção de fritas 500 g";
va2=8.5;
a3="Porção de fritas 200 g";
va3=4.5;
a4="Espetinho";
va4=10;
a5="Churrasquinho de porco"
va5=3.5
a6="Churrasquinho de frango"
va6=3
a7="Churrasquinho misto"
va7=4
a8="Lasanha de bloco"
va8=6


b1="Coca-Cola 2.5L";
vb1=4.5;
b2="Pepsi 2.5L";
vb2=4;
b3="Fanta 2,5L";
vb3=4;
b4="Água 2L";
vb4=2.5;
b5="Nada";
b6="Coca-Cola lata";
vb6=1.5;
b7="Pepsi lata";
vb7=1.25;
b8="Coca-Cola 600 ml";
vb8=2.5;
vo=0;
V=vo
V1=vo

alert("Para ajudar você a escolher mostraremos todos as comidas juntas!");


alert("Lanches\n"+l1+"  R$"+ vl1 +"\n"+l2+"  R$"+ vl2 +"\n"+l3+"  R$"+ vl3 +"\n"+l4+"  R$"+ vl4 +"\n"+l5+"  R$"+ vl5 +"\n"+l6+"  R$"+ vl6 +"\n"+l7+"  R$"+ vl7 +"\n"+l8+"  R$"+ vl8 +"\nIr para a proxima pagina pressione OK");


alert("Pizza \n"+p1+"  R$"+ vp1 +"\n"+p2+"  R$"+ vp2 +"\n"+p3+"  R$"+ vp3 +"\n"+p4+"  R$"+ vp4 +"\n"+p5+"  R$"+ vp5 +"\n"+p6+"  R$"+ vp6 +"\n"+p7+"  R$"+ vp7 +"\n"+p8+"  R$"+ vp8 +"\nIr para a proxima pagina pressione OK");


alert("Aperitivos: \n"+a1+"  R$"+ va1 +"\n"+a2+"  R$"+ va2 +"\n"+a3+"  R$"+ va3 +"\n"+a4+"  R$"+ va4 +"\n"+a5+"  R$"+ va5 +"\n"+a6+"  R$"+ va6 +"\n"+a7+"  R$"+ va7 +"\n"+a8+"  R$"+ va8 )


M=parseInt(prompt("Você quer o menu de: \nLanches digite 1 \nPizzas digite 2 \nAperitivos digite 3"));


switch (M) {
case 1: C=parseInt(prompt("Nós temos de lanche: \n1-"+l1+"  R$"+ vl1 +"\n2-"+l2+"  R$"+ vl2 +"\n3-"+l3+"  R$"+ vl3 +"\n4-"+l4+"  R$"+ vl4 +"\n5-"+l5+"  "+ vl5 +"\n6-"+l6+"  "+ vl6 +"\n7-"+l7+"  "+ vl7 +"\n8-"+l8+"  "+ vl8 +"\n0- Voltar ao menu anterior"));
		break;
case 2: C=parseInt(prompt("Nós temos de Pizza: \n1-"+p1+"  R$"+ vp1 +"\n2-"+p2+"  R$"+ vp2 +"\n3-"+p3+"  R$"+ vp3 +"\n4-"+p4+"  R$"+ vp4 +"\n5-"+p5+"  R$"+ vp5 +"\n6-"+p6+"  R$"+ vp6 +"\n7-"+p7+"  R$"+ vp7 +"\n8-"+p8+"  R$"+ vp8 +"\n0- Voltar ao menu anterior"));
		break;		
case 3:C=parseInt(prompt("Nós temos de Aperitivos: \n1-"+a1+"  R$"+ va1 +"\n2-"+a2+"  R$"+ va2 +"\n3-"+a3+"  R$"+ va3 +"\n4-"+a4+"  R$"+ va4 +"\n5-"+a5+"  R$"+ va5 +"\n6-"+a6+"  R$"+ va6 +"\n7-"+a7+"  R$"+ va7 +"\n8-"+a8+"  R$"+ va8 +"\n0- Voltar ao menu anterior"));
		break;
default: alert("Digite um menu valido(1,2 ou 3)!");
}


if		(C==0) {
		M=parseInt(prompt("Você quer o menu de: \nLanches digite 1 \nPizzas digite 2 \nAperitivos digite 3"));
		switch (M) {
case 1: C=parseInt(prompt("Nós temos de lanche: \n1-"+l1+"  R$"+ vl1 +"\n2-"+l2+"  R$"+ vl2 +"\n3-"+l3+"  R$"+ vl3 +"\n4-"+l4+"  R$"+ vl4 +"\n5-"+l5+"  R$"+ vl5 +"\n6-"+l6+"  R$"+ vl6 +"\n7-"+l7+"  R$"+ vl7 +"\n8-"+l8+"  R$"+ vl8));
		break;
case 2: C=parseInt(prompt("Nós temos de Pizza: \n1-"+p1+"  R$"+ vp1 +"\n2-"+p2+"  R$"+ vp2 +"\n3-"+p3+"  R$"+ vp3 +"\n4-"+p4+"  R$"+ vp4 +"\n5-"+p5+"  R$"+ vp5 +"\n6-"+p6+"  R$"+ vp6 +"\n7-"+p7+"  R$"+ vp7 +"\n8-"+p8+"  R$"+ vp8));
		break;		
case 3:C=parseInt(prompt("Nós temos de Aperitivos: \n1-"+a1+"  R$"+ va1 +"\n2-"+a2+"  R$"+ va2 +"\n3-"+a3+"  R$"+ va3 +"\n4-"+a4+"  R$"+ va4 +"\n5-"+a5+"  R$"+ va5 +"\n6-"+a6+"  R$"+ va6 +"\n7-"+a7+"  R$"+ va7 +"\n8-"+a8+"  R$"+ va8 ));
		break;
default: alert("Digite um menu valido(1,2 ou 3)!");
}
}


if		(M==1) {
		if		(C>=1&&C<=8) {
				if		(C==1){
						Q=parseInt(prompt("Quantos "+l1+" você deseja:"));
						V=vl1*Q
				}
				if		(C==2){
						Q=parseInt(prompt("Quantos "+l2+" você deseja:"));
						V=vl2*Q
				}
				if		(C==3){
						Q=parseInt(prompt("Quantos "+l3+" você deseja:"));
						V=vl3*Q
				}
				if		(C==4){
						Q=parseInt(prompt("Quantos "+l4+" você deseja:"));
						V=vl4*Q
				}
				if		(C==5){
						Q=parseInt(prompt("Quantos "+l5+" você deseja:"));
						V=vl5*Q
				}
				if		(C==6){
						Q=parseInt(prompt("Quantos "+l6+" você deseja:"));
						V=vl6*Q
				}
				if		(C==7){
						Q=parseInt(prompt("Quantos "+l7+" você deseja:"));
						V=vl7*Q
				}
				if		(C==8){
						Q=parseInt(prompt("Quantos "+l8+" você deseja:"));
						V=vl8*Q
				}
			
				
		}
		else {
				alert("Escolha um valor valido!");
		}
}	
	
	
if		(M==2) {
		if		(C>=1&&C<=8) {
				if		(C==1){
						Q=parseInt(prompt("Quantos "+p1+" você deseja:"));
						V=vp1*Q
				}
				if		(C==2){
						Q=parseInt(prompt("Quantos "+p2+" você deseja:"));
						V=vp2*Q
				}
				if		(C==3){
						Q=parseInt(prompt("Quantos "+p3+" você deseja:"));
						V=vp3*Q
				}
				if		(C==4){
						Q=parseInt(prompt("Quantos "+p4+" você deseja:"));
						V=vp4*Q
				}
				if		(C==5){
						Q=parseInt(prompt("Quantos "+p5+" você deseja:"));
						V=vp5*Q
				}
				if		(C==6){
						Q=parseInt(prompt("Quantos "+p6+" você deseja:"));
						V=vp6*Q
				}
				if		(C==7){
						Q=parseInt(prompt("Quantos "+p7+" você deseja:"));
						V=vp7*Q
				}
				if		(C==8){
						Q=parseInt(prompt("Quantos "+p8+" você deseja:"));
						V=vp8*Q
				}
		}
		else {
				alert("Escolha um valor valido!");
		}		
}


if		(M==3) {
		if		(C>=1&&C<=8) {
				if		(C==1){
						Q=parseInt(prompt("Quantos "+a1+" você deseja:"));
						V=va1*Q
				}
				if		(C==2){
						Q=parseInt(prompt("Quantos "+a2+" você deseja:"));
						V=va2*Q
				}
				if		(C==3){
						Q=parseInt(prompt("Quantos "+a3+" você deseja:"));
						V=va3*Q
				}
				if		(C==4){
						Q=parseInt(prompt("Quantos "+a4+" você deseja:"));
						V=va4*Q
				}
				if		(C==5){
						Q=parseInt(prompt("Quantos "+a5+" você deseja:"));
						V=va5*Q
				}
				if		(C==6){
						Q=parseInt(prompt("Quantos "+a6+" você deseja:"));
						V=va6*Q
				}
				if		(C==7){
						Q=parseInt(prompt("Quantos "+a7+" você deseja:"));
						V=va7*Q
				}
				if		(C==8){
						Q=parseInt(prompt("Quantos "+a8+" você deseja:"));
						V=va8*Q
				}
		}
		else {
				alert("Escolha um valor valido!");
		}
}


V1=0


if		(M==1) {
		V1=0
		OU=prompt("Você gostaria de mais um lanche:\n1-Sim\n2-Não")
		if		(OU==1){
				V1=0
				X=parseInt(prompt("1-"+l1+"  R$"+ vl1 +"\n2-"+l2+"  R$"+ vl2 +"\n3-"+l3+"  R$"+ vl3 +"\n4-"+l4+"  R$"+ vl4 +"\n5-"+l5+"  R$"+ vl5 +"\n6-"+l6+"  R$"+ vl6 +"\n7-"+l7+"  R$"+ vl7 +"\n8-"+l8+"  R$"+ vl8));
				if		(X==1){
						Q=parseInt(prompt("Quantos "+l1+" você deseja:"));
						V1=vl1*Q
				}
				if		(X==2){
						Q=parseInt(prompt("Quantos "+l2+" você deseja:"));
						V1=vl2*Q
				}
				if		(X==3){
						Q=parseInt(prompt("Quantos "+l3+" você deseja:"));
						V1=vl3*Q
				}
				if		(X==4){
						Q=parseInt(prompt("Quantos "+l4+" você deseja:"));
						V1=vl4*Q
				}
				if		(X==5){
						Q=parseInt(prompt("Quantos "+l5+" você deseja:"));
						V1=vl5*Q
				}
				if		(X==6){
						Q=parseInt(prompt("Quantos "+l6+" você deseja:"));
						V1=vl6*Q
				}
				if		(X==7){
						Q=parseInt(prompt("Quantos "+l7+" você deseja:"));
						V1=vl7*Q
				}
				if		(X==8){
						Q=parseInt(prompt("Quantos "+l8+" você deseja:"));
						V1=vl8*Q
				}
		}
		else {
				Y=prompt("Você talvez gostaria então de uma \n1-Pizza\n2-Aperitivo\n0-Nenhum")
				if 		(Y==1){
						X==parseInt(prompt("1-"+p1+"  R$"+ vp1 +"\n2-"+p2+"  R$"+ vp2 +"\n3-"+p3+"  R$"+ vp3 +"\n4-"+p4+"  R$"+ vp4 +"\n5-"+p5+"  R$"+ vp5 +"\n6-"+p6+"  R$"+ vp6 +"\n7-"+p7+"  R$"+ vp7 +"\n8-"+p8+"  R$"+ vp8));
						if		(X==1){
								Q=parseInt(prompt("Quantos "+p1+" você deseja:"));
								V1=vp1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+p2+" você deseja:"));
								V1=vp2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+p3+" você deseja:"));
								V1=vp3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+p4+" você deseja:"));
								V1=vp4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+p5+" você deseja:"));
								V=vp5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+p6+" você deseja:"));
								V1=vp6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+p7+" você deseja:"));
								V1=vp7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+p8+" você deseja:"));
								V1=vp8*Q
						}
				}
				if 		(Y==2){
						X==parseInt(prompt("1-"+a1+"  R$"+ va1 +"\n2-"+a2+"  R$"+ va2 +"\n3-"+a3+"  R$"+ va3 +"\n4-"+a4+"  R$"+ va4 +"\n5-"+a5+"  R$"+ va5 +"\n6-"+a6+"  R$"+ va6 +"\n7-"+a7+"  R$"+ va7 +"\n8-"+a8+"  R$"+ va8 ));
						if		(X==1){
								Q=parseInt(prompt("Quantos "+a1+" você deseja:"));
								V1=va1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+a2+" você deseja:"));
								V1=va2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+a3+" você deseja:"));
								V1=va3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+a4+" você deseja:"));
								V1=va4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+a5+" você deseja:"));
								V1=va5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+a6+" você deseja:"));
								V1=va6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+a7+" você deseja:"));
								V1=va7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+a8+" você deseja:"));
								V1=va8*Q
						}
				}
				
		}
}


if		(M==2) {
		V1=0
		OU=prompt("Você gostaria de mais uma Pizza:\n1-Sim\n2-Não")
		if		(OU==1){
				X==parseInt(prompt("1-"+p1+"  R$"+ vp1 +"\n2-"+p2+"  R$"+ vp2 +"\n3-"+p3+"  R$"+ vp3 +"\n4-"+p4+"  R$"+ vp4 +"\n5-"+p5+"  R$"+ vp5 +"\n6-"+p6+"  R$"+ vp6 +"\n7-"+p7+"  R$"+ vp7 +"\n8-"+p8+"  R$"+ vp8));
				if		(X==1){
						Q=parseInt(prompt("Quantos "+p1+" você deseja:"));
						V1=vp1*Q
				}
				if		(X==2){
						Q=parseInt(prompt("Quantos "+p2+" você deseja:"));
						V1=vp2*Q
				}
				if		(X==3){
						Q=parseInt(prompt("Quantos "+p3+" você deseja:"));
						V1=vp3*Q
				}
				if		(X==4){
						Q=parseInt(prompt("Quantos "+p4+" você deseja:"));
						V1=vp4*Q
				}
				if		(X==5){
						Q=parseInt(prompt("Quantos "+p5+" você deseja:"));
						V=vp5*Q
				}
				if		(X==6){
						Q=parseInt(prompt("Quantos "+p6+" você deseja:"));
						V1=vp6*Q
				}
				if		(X==7){
						Q=parseInt(prompt("Quantos "+p7+" você deseja:"));
						V1=vp7*Q
				}
				if		(X==8){
						Q=parseInt(prompt("Quantos "+p8+" você deseja:"));
						V1=vp8*Q
				}
		}
		else {
				Y=prompt("Você talvez gostaria então de um \n1-Lanche\n2-Aperitivo\n0-Nenhum")
				if		(Y==1){
						X=parseInt(prompt("1-"+l1+"  R$"+ vl1 +"\n2-"+l2+"  R$"+ vl2 +"\n3-"+l3+"  R$"+ vl3 +"\n4-"+l4+"  R$"+ vl4 +"\n5-"+l5+"  R$"+ vl5 +"\n6-"+l6+"  R$"+ vl6 +"\n7-"+l7+"  R$"+ vl7 +"\n8-"+l8+"  R$"+ vl8));
						if		(X==1){
								Q=parseInt(prompt("Quantos "+l1+" você deseja:"));
								V1=vl1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+l2+" você deseja:"));
								V1=vl2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+l3+" você deseja:"));
								V1=vl3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+l4+" você deseja:"));
								V1=vl4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+l5+" você deseja:"));
								V1=vl5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+l6+" você deseja:"));
								V1=vl6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+l7+" você deseja:"));
								V1=vl7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+l8+" você deseja:"));
								V1=vl8*Q
						}
				}
				}
				if 		(Y==2){
						X==parseInt(prompt("1-"+a1+"  R$"+ va1 +"\n2-"+a2+"  R$"+ va2 +"\n3-"+a3+"  R$"+ va3 +"\n4-"+a4+"  R$"+ va4 +"\n5-"+a5+"  R$"+ va5 +"\n6-"+a6+"  R$"+ va6 +"\n7-"+a7+"  R$"+ va7 +"\n8-"+a8+"  R$"+ va8 ));
						if		(X==1){
								Q=parseInt(prompt("Quantos "+a1+" você deseja:"));
								V1=va1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+a2+" você deseja:"));
								V1=va2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+a3+" você deseja:"));
								V1=va3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+a4+" você deseja:"));
								V1=va4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+a5+" você deseja:"));
								V1=va5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+a6+" você deseja:"));
								V1=va6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+a7+" você deseja:"));
								V1=va7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+a8+" você deseja:"));
								V1=va8*Q
						}
				}
}


if		(M==3) {
		V1=0
		OU=prompt("Você gostaria de mais um aperitivo:\n1-Sim\n2-Não")
		if		(OU==1){
				X==parseInt(prompt("1-"+a1+"  R$"+ va1 +"\n2-"+a2+"  R$"+ va2 +"\n3-"+a3+"  R$"+ va3 +"\n4-"+a4+"  R$"+ va4 +"\n5-"+a5+"  R$"+ va5 +"\n6-"+a6+"  R$"+ va6 +"\n7-"+a7+"  R$"+ va7 +"\n8-"+a8+"  R$"+ va8 ));
				if		(X==1){
								Q=parseInt(prompt("Quantos "+a1+" você deseja:"));
								V1=va1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+a2+" você deseja:"));
								V1=va2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+a3+" você deseja:"));
								V1=va3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+a4+" você deseja:"));
								V1=va4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+a5+" você deseja:"));
								V1=va5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+a6+" você deseja:"));
								V1=va6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+a7+" você deseja:"));
								V1=va7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+a8+" você deseja:"));
								V1=va8*Q
						}
		}
		else {
				Y=prompt("Você talvez gostaria então de um \n1-Lanche\n2-Pizza\n0-Nenhum")
				if		(Y==1){
						X=parseInt(prompt("1-"+l1+"  R$"+ vl1 +"\n2-"+l2+"  R$"+ vl2 +"\n3-"+l3+"  R$"+ vl3 +"\n4-"+l4+"  R$"+ vl4 +"\n5-"+l5+"  R$"+ vl5 +"\n6-"+l6+"  R$"+ vl6 +"\n7-"+l7+"  R$"+ vl7 +"\n8-"+l8+"  R$"+ vl8));
						if		(X==1){
								Q=parseInt(prompt("Quantos "+l1+" você deseja:"));
								V1=vl1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+l2+" você deseja:"));
								V1=vl2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+l3+" você deseja:"));
								V1=vl3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+l4+" você deseja:"));
								V1=vl4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+l5+" você deseja:"));
								V1=vl5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+l6+" você deseja:"));
								V1=vl6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+l7+" você deseja:"));
								V1=vl7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+l8+" você deseja:"));
								V1=vl8*Q
						}
				}
				if 		(Y==2){
						X==parseInt(prompt("1-"+p1+"  R$"+ vp1 +"\n2-"+p2+"  R$"+ vp2 +"\n3-"+p3+"  R$"+ vp3 +"\n4-"+p4+"  R$"+ vp4 +"\n5-"+p5+"  R$"+ vp5 +"\n6-"+p6+"  R$"+ vp6 +"\n7-"+p7+"  R$"+ vp7 +"\n8-"+p8+"  R$"+ vp8));
						if		(X==1){
								Q=parseInt(prompt("Quantos "+p1+" você deseja:"));
								V1=vp1*Q
						}
						if		(X==2){
								Q=parseInt(prompt("Quantos "+p2+" você deseja:"));
								V1=vp2*Q
						}
						if		(X==3){
								Q=parseInt(prompt("Quantos "+p3+" você deseja:"));
								V1=vp3*Q
						}
						if		(X==4){
								Q=parseInt(prompt("Quantos "+p4+" você deseja:"));
								V1=vp4*Q
						}
						if		(X==5){
								Q=parseInt(prompt("Quantos "+p5+" você deseja:"));
								V=vp5*Q
						}
						if		(X==6){
								Q=parseInt(prompt("Quantos "+p6+" você deseja:"));
								V1=vp6*Q
						}
						if		(X==7){
								Q=parseInt(prompt("Quantos "+p7+" você deseja:"));
								V1=vp7*Q
						}
						if		(X==8){
								Q=parseInt(prompt("Quantos "+p8+" você deseja:"));
								V1=vp8*Q
						}
				}
			}
}


B=parseInt(prompt("Você quer beber algo:\n1-"+b1+"   R$"+vb1+"\n2-"+b2+"   R$"+vb2+"\n3-"+b3+"   R$"+vb3+"\n4-"+b4+"   R$"+vb4+"\n5-"+b5+"\n6-"+b6+"   R$"+vb6+"\n7-"+b7+"   R$"+vb7+"\n8-"+b8+"   R$"+vb8+"R$ digite 8"));


if		(B>=1&&B<=8) {
		if	(B==1) {
			QB=parseInt(prompt("Quantas "+b1+" você deseja:"));
			VF=V+(vb1*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
		if	(B==2) {
			QB=parseInt(prompt("Quantas "+b2+" você deseja:"));
			VF=V+(vb2*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
		if	(B==3) {
			QB=parseInt(prompt("Quantas "+b3+" você deseja:"));
			VF=V+(vb3*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
		if	(B==4) {
			QB=parseInt(prompt("Quantas "+b4+" você deseja:"));
			VF=V+(vb4*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
		if	(B==5) {
			VF=V+V1;
			alert("Você deve pagar: R$"+V);
		}
		if	(B==6) {
			QB=parseInt(prompt("Quantas "+b6+" você deseja:"));
			VF=V+(vb6*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
		if	(B==7) {
			QB=parseInt(prompt("Quantas "+b7+" você deseja:"));
			VF=V+(vb7*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
		if	(B==8) {
			QB=parseInt(prompt("Quantas "+b8+" você deseja:"));
			VF=V+(vb8*QB)+V1;
			alert("Você deve pagar: R$"+VF);
		}
}
else {
		V=V+V1
		alert("Você deve pagar: R$"+V);
}


alert("Obrigado por comprar na Pizzaria e lancheria IFRS.");