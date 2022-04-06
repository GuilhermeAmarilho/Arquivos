//1 - vêr se é um palindromo (vêr se é igual de tras para frente);
var p,pos1,pos2,let1,let2,soma;
p=prompt("Informe a palavra ou frase: "); 
while	((p.indexOf(" ")!=-1)||(p.indexOf(",")!=-1)||(p.indexOf(".")!=-1)||(p.indexOf("-")!=-1)){
	p=p.replace(" ","");
	p=p.replace(".","");
	p=p.replace("-","");
	p=p.replace(",","");
}
p=p.toLowerCase();
pos1=-1;
pos2=0;
pos2=p.length;
let1="";
let2=""; 
soma=-1;
while	(pos1<=pos2){
	let1=p.charAt(pos1++);	
	let2=p.charAt(pos2--);	
	if	(let1==let2){
		soma++;
	}	
}
if	(soma>=((p.length)/2)) {
	alert("A palavra é uma palíndroma! ");
}	
else	{
	alert("A palavra não é uma palíndroma! ");
}

//2 - codificar uma frase com ela igual 3 letras apos;

var fra,pos,pos1,cod,tam,let,frac;
fra=prompt("Informe a palavra ou frase que deseja codificar (sem acento e sem ç): ");
pos=-1;
pos1=-1;
cod=0;
tam=fra.length;
frac="";
let="";
while	(pos!=tam){
	cod=(fra.charCodeAt(++pos))+3;
	if	(cod>122){
		cod=((cod+97)%122)-1;
	}
	frac+=String.fromCharCode(cod);
}
while	(frac.indexOf("#")!=-1){
	frac=frac.replace("#"," ");
}
frac=frac.toUpperCase();
alert("A frase codificada é: "+frac);


