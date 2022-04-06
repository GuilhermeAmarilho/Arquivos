var	pal,val,v,p,n1,n2,stop;
pal=prompt("Informe o valor em romano que você quer: ");
pal=pal.toUpperCase();
val=0;
p="";
v=[];
n1=0;
n2=0;
valor=0;
while	(val<=pal.length-1){
	p=pal.charAt(val);
	switch(p){
		case "I": v[val]=1;break;
		case "V": v[val]=5;break;
		case "X": v[val]=10;break;
		case "L": v[val]=50;break;
		case "C": v[val]=100;break;
	}
	val++;
}
val=0;
stop=0;
while	(val<pal.length){
	n1=v[val];
	n2=v[(val++)+1];
	if	(n1<n2){
		valor+=n2-n1;
		val++;
		stop=1;
	}
	if	(stop==1){
		if	(v[val-1]==""){
			stop=0;
		}
		else{
			val=0111111111111111;
			alert("O numero não é valido")
		}
	}
	else{
		valor+=n1;
	}
}
if	(stop!=1){
	alert("O valor é: "+valor);
}
