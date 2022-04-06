//My game!
var  PJC1,PJP1,x,P,D,T2;
alert("Ola jovem padawan, Nesse game iremos testar sua sorte, sua sabedoria e sua nerdisse. E então diremos se você está pronto para se tornar um Jedi!")
n=prompt("Comece informando seu nome: ")

//{ 1ª fase.

alert("1ª fase, nesta fase iremos ver se você tem sorte no Jokenpo")
alert("1ª partida!")
PJP1=parseInt(prompt("Escolha sua jogada: \n 1 - Tesoura\n 2 - Papel\n 3 - Pedra"))
PJC1=Math.trunc(Math.random(1,3)*10)
x=1;
P=0;
D=0;
T2=0;
while	(x!=0) {
	if	((PJC1!=1) || (PJC1!=2) || (PJC1!=3)) {
		PJC1=Math.trunc(Math.random(1.0,3.0)*10);
		if	((PJC1==1) || (PJC1==2) || (PJC1==3)) {
			x=0;
		}
	}
	else {
		x=0;
	}
}
if	(PJP1==1) {
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você perdeu a 1ª partida!");	
			P+=0;
		}
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você empatou a 1ª partida!");
			P+=0.5;
		}
}
if	(PJP1==2) {
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você perdeu a 2ª partida!");
			P+=0;
		}
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você empatou a 3ª partida!");
			P+=0.5;
		}
}
if	(PJP1==3) {
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você perdeu a 2ª partida!");
			P+=0;
		}
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você empatou a 3ª partida!");	
			P+=0.5;
		}
}

alert("2ª partida!");

PJP1=parseInt(prompt("Escolha sua jogada: \n 1 - Tesoura\n 2 - Papel\n 3 - Pedra"))


//{ 
PJC1=Math.trunc(Math.random(1,3)*10)
x=1
while	(x!=0) {
	if	((PJC1!=1) || (PJC1!=2) || (PJC1!=3)) {
		PJC1=Math.trunc(Math.random(1.0,3.0)*10);
		if	((PJC1==1) || (PJC1==2) || (PJC1==3)) {
			x=0;
		}
	}
	else {
		x=0;
	}
}
if	(PJP1==1) {
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você perdeu a 1ª partida!");	
			P+=0;
		}
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você empatou a 1ª partida!");
			P+=0.5;
		}
}
if	(PJP1==2) {
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você perdeu a 1ª partida!");
			P+=0;
		}
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você empatou a 1ª partida!");
			P+=0.5;
		}
}
if	(PJP1==3) {
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você perdeu a 1ª partida!");
			P+=0;
		}
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você empatou a 1ª partida!");	
			P+=0.5;
		}
}

alert("3ª partida!");

PJP1=parseInt(prompt("Escolha sua jogada: \n 1 - Tesoura\n 2 - Papel\n 3 - Pedra"))
PJC1=Math.trunc(Math.random(1,3)*10)
x=1
while	(x!=0) {
	if	((PJC1!=1) || (PJC1!=2) || (PJC1!=3)) {
		PJC1=Math.trunc(Math.random(1.0,3.0)*10);
		if	((PJC1==1) || (PJC1==2) || (PJC1==3)) {
			x=0;
		}
	}
	else {
		x=0;
	}
}
if	(PJP1==1) {
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você ganhou a 1ª partida!");
			P++;
		}
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você perdeu a 1ª partida!");	
			P+=0;
		}
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você empatou a 1ª partida!");
			P+=0.5;
		}
}
if	(PJP1==2) {
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você ganhou a 2ª partida!");
			P++;
		}
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você perdeu a 2ª partida!");
			P+=0;
		}
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você empatou a 2ª partida!");
			P+=0.5;
		}
}
if	(PJP1==3) {
		if	(PJC1==1){
			alert("Seu adversario escolheu: Tesoura");
			alert("você ganhou a 3ª partida!");
			P++;
		}
		if	(PJC1==2){
			alert("Seu adversario escolheu: Papel");
			alert("você perdeu a 3ª partida!");
			P+=0;
		}
		if	(PJC1==3){
			alert("Seu adversario escolheu: Pedra");
			alert("você empatou a 3ª partida!");	
			P+=0.5;
		}
}
alert("Sua pontuação foi: "+ P);
if	(P>=2){
	alert("Você passou para a proxima fase!");
	T2=1;
}
else{
	alert("Você rodou!");
	T2=0;
}
if	(T2==0){
	T2=parseInt(prompt("Você deseja recomeçar o jogo:\n1 - Sim! \n2 - Não!"));
	if	(T2==1){
		while	(P<2){
			alert("1ª partida!")
			PJP1=parseInt(prompt("Escolha sua jogada: \n 1 - Tesoura\n 2 - Papel\n 3 - Pedra"))
			PJC1=Math.trunc(Math.random(1,3)*10)
			x=1
			P=0
			while	(x!=0) {
				if	((PJC1!=1) || (PJC1!=2) || (PJC1!=3)) {
					PJC1=Math.trunc(Math.random(1.0,3.0)*10);
					if	((PJC1==1) || (PJC1==2) || (PJC1==3)) {
						x=0;
					}
				}
				else {
					x=0;
				}
			}
			if	(PJP1==1) {
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você perdeu a 1ª partida!");	
						P+=0;
					}
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você empatou a 1ª partida!");
						P+=0.5;
					}
			}
			if	(PJP1==2) {
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você perdeu a 1ª partida!");
						P+=0;
					}
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você empatou a 1ª partida!");
						P+=0.5;
					}
			}
			if	(PJP1==3) {
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você perdeu a 1ª partida!");
						P+=0;
					}
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você empatou a 1ª partida!");	
						P+=0.5;
					}
			}

			alert("2ª partida!");

			PJP1=parseInt(prompt("Escolha sua jogada: \n 1 - Tesoura\n 2 - Papel\n 3 - Pedra"))
			PJC1=Math.trunc(Math.random(1,3)*10)
			x=1
			while	(x!=0) {
				if	((PJC1!=1) || (PJC1!=2) || (PJC1!=3)) {
					PJC1=Math.trunc(Math.random(1.0,3.0)*10);
					if	((PJC1==1) || (PJC1==2) || (PJC1==3)) {
						x=0;
					}
				}
				else {
					x=0;
				}
			}
			if	(PJP1==1) {
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você perdeu a 1ª partida!");	
						P+=0;
					}
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você empatou a 1ª partida!");
						P+=0.5;
					}
			}
			if	(PJP1==2) {
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você perdeu a 1ª partida!");
						P+=0;
					}
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você empatou a 1ª partida!");
						P+=0.5;
					}
			}
			if	(PJP1==3) {
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você perdeu a 1ª partida!");
						P+=0;
					}
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você empatou a 1ª partida!");	
						P+=0.5;
					}
			}

			alert("3ª partida!");

			PJP1=parseInt(prompt("Escolha sua jogada: \n 1 - Tesoura\n 2 - Papel\n 3 - Pedra"))
			PJC1=Math.trunc(Math.random(1,3)*10)
			x=1
			while	(x!=0) {
				if	((PJC1!=1) || (PJC1!=2) || (PJC1!=3)) {
					PJC1=Math.trunc(Math.random(1.0,3.0)*10);
					if	((PJC1==1) || (PJC1==2) || (PJC1==3)) {
						x=0;
					}
				}
				else {
					x=0;
				}
			}
			if	(PJP1==1) {
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você ganhou a 1ª partida!");
						P++;
					}
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você perdeu a 1ª partida!");	
						P+=0;
					}
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você empatou a 1ª partida!");
						P+=0.5;
					}
			}
			if	(PJP1==2) {
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você ganhou a 2ª partida!");
						P++;
					}
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você perdeu a 2ª partida!");
						P+=0;
					}
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você empatou a 2ª partida!");
						P+=0.5;
					}
			}
			if	(PJP1==3) {
					if	(PJC1==1){
						alert("Seu adversario escolheu: Tesoura");
						alert("você ganhou a 3ª partida!");
						P++;
					}
					if	(PJC1==2){
						alert("Seu adversario escolheu: Papel");
						alert("você perdeu a 3ª partida!");
						P+=0;
					}
					if	(PJC1==3){
						alert("Seu adversario escolheu: Pedra");
						alert("você empatou a 3ª partida!");	
						P+=0.5;
					}
			}
			alert("Sua pontuação foi:"+ P);
			if	(P>=2){
				alert("Você passou para a proxima fase!");
				T2=1;
			}
			else{
				alert("Você rodou!");
				T2=0;
			}
		}
	}
	else {
		alert("Obrigado por jogar!");
		D=1
	}
}
//}

//{ 2ª fase.

alert("2ª fase, nesta fase iremos ver seu conhecimento em filmes,jogos e animes");

alert("1ª partida!");

PQ=parseInt(prompt("Qual destas empresas foi uma das desenvolvedoras do jogo Counter-Strike:	\n 1 -	Mojang Specifications. \n 2 - Valve Corporation. \n 3 - Activision Blizzard \n 4 - Ubisoft. "));
P2=0;

if (PQ==2){
	alert("Acertou mizeravi!");
	P2+=1;
}
else	{
	alert("Errou!");
	P2+=0;
}

alert("2ª Partida!"); 	

PQ=parseInt(prompt("Qual o nome do ator que interpreta o personagem \"Spock\" na série Star Trek original \n 1 - Leonard Nimoy \n 2 - Johnny Depp \n 3 - Stan Lee \n 4 - Chris Pine"));  

if (PQ==1){
	alert("Acertou mizeravi!");
	P2+=1;
}
else	{
	alert("Errou!");
	P2+=0;
}

alert("3ª Partida!"); 	

PQ=parseInt(prompt("Qual foi o 1º pokemon que Ash capiturou em sua jornada: \n 1 - Pikachu. \n 2 - Butterfree. \n 3 - Caterpie. \n 4 - Bulbasaur"))

if (PQ==3){
	alert("Acertou mizeravi!");
	P2+=1;
}
else	{
	alert("Errou!");
	P2+=0;
}

if	(P2>=2){
	alert("Parabens passou para a proxima fase!");
}
else	{
	alert("Você rodou!");
	RQ=parseInt(prompt("Quer recomeçar o quiz:\n1 - Sim! \n 2 - Não" ));
	if	(RQ==1){
		P2=0
		
		alert("1ª partida!");

		PQ=parseInt(prompt("Qual canal com melhor conteudo do Youtube \n1 - Pewdiepie \n2 - 5 minutos \n3 - Canal Canalha \n4 - Amarilho_BR"));
		if (PQ==4){
			alert("Acertou mizeravi!");
			P2+=1;
		}
		else	{
			alert("Errou!");
			P2+=0;
		}
		alert("2ª partida!");

		PQ=parseInt(prompt("Qual o filme de maior bilheteria: \n 1 - Avatar \n 2 - Titanic \n 3 - Filme do Pelé \n 4 - Guerra Civil"));
		if (PQ==1){
			alert("Acertou mizeravi!");
			P2+=1;
		}
		else	{
			alert("Errou!");
			P2+=0;
		}
		alert("3ª partida!");
		
		PQ=parseInt(prompt("Qual a carta mais rara em Yu-Gi-Oh \n 1 - Dragão Branco de Olhos Azuis \n 2 - Exodia \n 3 - Mago Negro \n 4 - Prassodia")); 
		if (PQ==2){
			alert("Acertou mizeravi!");
			P2+=1;
		}
		else	{
			alert("Errou!");
			P2+=0;
		}
		if	(P2>=2){
			alert("Parabens passou para a proxima fase!");
		}
	}
}

//}