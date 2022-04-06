//jogo de advinhação,facil - 3 chances 10 numeros,medio - 10 chances 100 numeros,dificil - 20 chances 500 numeros. Sempre de 1 ate o numero limite ,com dicas!


//{ O jogo em si!
var dif,life,n,dica,STOP,c,condelife,mmc,sla,r,a,b,a1,b1,v,x,abc,n11,n1,n2,jn;
jn=1;

while (jn==1){
	dif=parseInt(prompt("Informe a dificuldade desejada: \n 1 - Fácil \n 2 - Médio \n 3 - Difícil"));
	//{ Variaveis
	life=0;
	n=0;
	dica="";
	STOP=0;
	c=0;
	condelife=0;
	mmc=2
	sla=3;
	r=1;
	a=2;
	b=2;
	a1=1;
	b1=1;
	v=2;
	x=0;
	abc=1;
	n11=n1;
	n1=25;
	n2=0
	//} 
	if	(dif==1){

		n=Math.trunc(Math.random(1,10)*10);
		life=3;
		condelife=life+1;
		
		while	(STOP!=1) {

			if	((n<=1)||(n>=10)) {
				n=Math.trunc(Math.random(1,10)*10); 
			}
			if	((n>=1)||(n<=10)) {
			STOP=1;
			}
		}	
		while ((life!=0)&&(c!=n)){
			alert("Você tem "+(--condelife)+" tentativas!");
			if	(life==3){
					if	(n>5) {
					dica+="Dicas:\né maior que 5";
					}
					if	(n<=5) {
					dica+="Dicas:\né menor ou igual a 5";
					}
			}
			if	(life==1){
				if	(n>5){
					if	(n>=8){
						dica+="\né maior ou igual a 7";
					}
					if	(n<8) {
						dica+="\né menor que 8";
					}
				}
				if	(n<=5) {
					if	(n>2) {
						dica+="\né maior que 2";
					}
					if	(n<3) {
						dica+="\né menor que 3";
					}
				}
			}
			c=parseInt(prompt("Informe sua tentativa: \n"+dica));
			life--;
			if (c!=n){
				alert("Você errou!");
			}
			if	(c==n) {
					alert("Parabens, você acertou!");
			}
		}
		if	(c!=n){
			alert("Você perdeu!, o numero éra: "+n);
		}
	}
	if	(dif==2){
		n=Math.trunc(Math.random(1,10)*100);
		life=10;
		condelife=life+1;
		r=1
		while	(STOP!=1) {
			if	((n<1)||(n>100)) {
				n=Math.trunc(Math.random(1,10)*100); 
			}
			if	((n>=1)||(n<=100)) {
			STOP=1;
			}
		}	
		while	((life!=0)&&(c!=n)){
			alert("Você tem "+(--condelife)+" tentativas!");
			if	(life==7){
				if (n>50){
					dica+="Dicas: \né maior que 50";
				}
				if	(n<=50){
					dica+="Dicas: \né menor ou igual a 50";
				}
			}
			if	(life==5){
				if (n>50){
					if	(n>80){
						dica+="\n é maior que 80";
					}
					if	(n<=80){
						dica+="\n é menor ou igual que 80";
					}	
				}
				if	(n<=50){
					if	(n>30){
						dica+="\n é maior que 30";
					}
					if	(n<=30){
						dica+="\n é menor ou igual que 30";
					}	
				}	
			}
			if	(life==3){
				if (n>50){
					if	(n>80){
						if	(n>90){
							dica+="\n é maior que 90";
						}
						if	(n<=90){
							dica+="\n é menor ou igual que 90";
						}
					}
					if	(n<=80){
						if	(n>65){
							dica+="\n é maior que 65";
						}
						if	(n<=65){
							dica+="\n é menor ou igual que 65";
						}
					}	
				}
				if (n<=50){
					if	(n>30){
						if	(n>40){
							dica+="\n é maior que 40";
						}
						if	(n<=40){
							dica+="\n é menor ou igual que 40";
						}
					}
					if	(n<=30){
						if	(n>15){
							dica+="\n é maior que 15";
						}						
					}	
						if	(n<=15){
							dica+="\n é menor ou igual que15";
						}
				}
			}
			if	(life==1){
				while	(n%mmc!=0){
				mmc++;
				}	
				dica+="\nseu menor multiplo é: "+mmc;		
			}
			c=parseInt(prompt("Informe seu chute: \n"+dica));
			life--;
			if (c!=n){
				alert("Você errou!");
			}
			if	(c==n) {
					alert("Parabens, você acertou!");
			}
		}
		if (c!=n){
		alert("Você perdeu!, o numero éra: "+n);
		}
	}
	if	(dif==3){
		n=Math.trunc(Math.random(1,10)*500);
		life=20;
		condelife=life+1;
		mmc=2;
		while	(STOP!=1) {
			if	((n<1)||(n>100)) {
				n=Math.trunc(Math.random(1,10)*100); 
			}
			if	((n>=1)||(n<=100)) {
				STOP=1;
			}
		}	
		while	((life!=0)&&(c!=n)){
			alert("Você tem "+(--condelife)+" tentativas!");
			if (life==15){
				if	(n>250){
					dica+="Dicas: \né maior que 250";
				}
				if	(n<=250){
					dica+="Dicas: \né menor ou igual que 250";
				}
			}
			if (life==12){
				if	(n<=250){
					if	(n>125){
					dica+="\né maior que 125";
					}
					if(n<=125){
						dica+="\né menor ou igual que 125";
					}
				}
				if	(n>250){
					if	(n>375){
						dica+="\né maior que 375";
					}
					if	(n<=375){
						dica+="\né menor ou igual que 375";
					}
				}
			}
			if (life==9){
				if	(n<=250){
					if	(n>125){
						if	(n>200){
							dica+="\né maior que 200";
						}
						if	(n<=200){
							dica+="\né menor ou igual que 200";
						}
					}
					if(n<=125){
						if	(n>75){
							dica+="\né maior que 75";
						}
						if	(n<=75){
							dica+="\né menor ou igual que 75";
						}
					}
				}
				if	(n>250){
					if	(n>375){
						if	(n>450){
							dica+="\né maior que 450";
						}
						if	(n<=450){
							dica+="\né menor ou igual que 450";
						}
					}
					if	(n<=375){
						if	(n>300){
							dica+="\né maior que 300";
						}
						if	(n<=300){
							dica+="\né menor ou igual que 300";
						}
					}
				}
			}
			if (life==6){
				dica+="\né a raiz quadrada de: "+(n*n)+"\n";
			}
			if	(life==3){
				while	(n%mmc!=0){
				mmc++;
				}	
				dica+="seu menor multiplo é: "+mmc+"\n";		
			}
			if (life==1){
				n2=n;
				n1=25;
				if(n1==n2){
					n1=20;
				}
				a=2;
				b=2;
				a1=1;
				b1=1;
				v=2;
				x=0;
				abc=1;
				n11=n1;
				if	((n1%n2==0)||(n2%n1==0)){
					if	(n1>n2){
						dica+="O mmc de "+n1+" e o numero que você procura é: "+n1;
						x++;
					}	
					if	(n1<n2){
						dica+="O mmc de "+n1+" e o numero que você procura é: "+n2;
						x++;
					}
					if	(n1==n2){
						dica+="O mmc de "+n1+" e o numero que você procura é: "+n1;
						x++;
					}
				}
				if	(x==0) {
					if	(n1!=n2) {
						while (n1%a!=0) {
								a++;
						}
						while (n2%b!=0) {
								b++;
						}
						if	(a!=b) {
							dica+="O mmc de "+n1+" e o numero que você procura é: "+(n1*n2);
							x++;
						}
					}
				}
				if	(x==0) {
					if	(n1!=n2) {
						while (n1%a!=0) {
								a++;
						}
						while (n2%b!=0) {
								b++;
						}
						if	(a==b) {
							n1=n1/a;
							n2=n2/a;
							abc=a;
							while ((n1>1)&&(n2>1)){
								while (n1%a!=0) {
										a++;
								}
								while (n2%b!=0) {
										b++;
								}
								if(a==b){
									abc*=a;
								}
								if(a!=b){
									abc=abc*a*b;
								}
								n1/=a;
								n2/=b;
							}
							dica+="O mmc de "+n11+" e o numero que você procura é: "+abc;
						}
					}
				}
			}
			c=parseInt(prompt("Informe sua tentativa: "+"\n"+dica));
			life--;
			if	(c==n){
				alert("Você acertou!");
			}
			if	(c!=n){
				alert("Você errou!")
			}
		}
		if (c!=n){
		alert("Você perdeu!, o numero éra: "+n);
		}
	}
	//}
	jn=parseInt(prompt("Você quer jogar de novo: \n 1 - Sim! \n 2 - Não!"));
}