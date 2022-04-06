//{	Exercícios
//1 - O tempo de vôo até o progetil atingir o solo. 
//2 - A altura maxima que o progetil atinge	
//}
var t,vo,v,ho,h,vox,voy,rad,g;
g=9.81;
vox=0;
voy=0;
t=0;
h=0;
v=0;
ho=parseInt(prompt("A que altura do chão esta o estilingue (em metros ):  "));
vo=parseInt(prompt("Informe a velocidade de lançamento (em m/s): "));
rad=parseInt(prompt("Qual a angulação que o objeto será lançado ( em radianos )\n Exemplos:\n 0.78 rad vale aproximadamente 45º\n 1.57 rad vale aproximadamente 90º\n 6.29 rad vale aproximadamente 360º:  "));
//{ exercicio 1 
a=g/2
voy=vo*Math.sin(rad)
b=voy;
c=ho;
t1=(-b-Math.sqrt((b*b)+(-4*(-a)*c)))/(-g)
t2=(-b+Math.sqrt((b*b)+(-4*(-a)*c)))/(-g)
if	(t1!=t2){
	if	(t1>=0){
		t=t1;
	}
	if	(t2>=0){
		alt=t2;
	}
}
else{
	t=t1
}
t1=Math.trunc(t)
t2=(Math.trunc((t-t1)*100))/100
t=t1+t2
alert("O tempo ate o objeto atingir o solo é de: "+t)
//}
//{ exercicio 2
t=voy/g;
vox=vo*Math.cos(rad);
h=vox*t+5;
h1=Math.trunc(h);
h2=((Math.trunc((h-h1)*100))/100);
h=h1+h2;
alert("A altura maxima atingida pelo objeto é : "+h);
//}