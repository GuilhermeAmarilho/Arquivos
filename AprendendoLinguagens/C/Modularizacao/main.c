#include<stdio.h>
void escrita(char adicional[60], int vector[12], int limit){
  int i;
  printf("\n %s ",adicional);
  for (i = 0; i < limit ; i++){
    if(vector[i] == 0 && vector[i + 1] == 0){
      i = limit;
    }
    else{
      if(limit - 1 == i){
        printf("%i",vector[i]);
      }
      else{
        printf("%i, ",vector[i]);
      }
    }
  }
}
int ex1(){
  int n[12], x[12], y[12], i, j, auxx = 0, auxy = 0;
  for (i=0;i<12;i++){
	  printf("\nEscreva um número inteiro: ");
    scanf("%i",&n[i]);
    if((n[i]%2 == 0) && (n[i]%3 == 0)){
      x[auxx] = n[i];
      auxx++;
    }
    if((n[i]%2 == 1) && (n[i]%5 == 0)){
      y[auxy] = n[i];
      auxy++;
    }
  }
  escrita("Lista inicial:", n, 12);
  escrita("Lista de pares divisores de 3: ", x, 12);
  escrita("Lista de impares divisores de 5: ", y, 12);
  return 0;
}

void inversora(int vector[10]){
  int aux[10], i;
  for (i = 0;i<10;i++){
    aux[i] = vector[9 - i]; 
  } 
  escrita("O formato da lista é: ", aux, 10);
};
int ex2(){
  int dados[10], i, j, d;
  for (i=0;i<10;i++){
    printf("Informe sua idade: ");
    scanf("%i",&dados[i]);
    i++;
    printf("Informe sua altura: ");
    scanf("%i",&dados[i]);
  }
  inversora(dados);
  return 0;
}

void somaLinha(int matriz[5][5], int linha){
  int x, soma;
  for(x = 0; x <= 4; x++){
		soma = soma + matriz[linha][x];
	}
	printf("\n%i é o resultado da soma da linha %i", soma, linha);
}
void somaColuna(int matriz[5][5], int coluna){
  int i, soma;
  for(i = 0; i <= 4; i++){
		soma = soma + matriz[i][coluna];
  }
  printf("\n%i é o resultado da soma da linha %i", soma, coluna);
}
void somaDiagPrincipal(int matriz[5][5]){
  int i, x, soma;
  for(i = 0; i <= 4; i++){
		for(x = 0; x <= 4; x++){
		  if(i == x){	
			soma = soma + matriz[i][x];
		  }
		}	
	}
  printf("\n%i é o resultado da soma diagonal principal", soma);
}
void somaDiagSecundaria(int matriz[5][5]){
  int i, x, soma;
  for(i = 0; i <= 4; i++){
		for(x = 0; x <= 4; x++){
      if(i + x == 4){
        soma = soma + matriz[i][x];
      }
    }
  }
  printf("\n%i é o resultado da soma diagonal secundaria", soma);
}
void somaTotal(int matriz[5][5]){
  int i, x, soma;
  for(i = 0; i <= 4; i++){//soma de todos os elementos da matriz
		for(x = 0; x <= 4; x++){
    	soma = soma + matriz[i][x];
    }
  }
  printf("\n%i é o resultado da soma total da matriz", soma);
}
void leituraMatriz(int matriz[5][5]){
  int i, x;
  printf("\n");
  for(i = 0; i <= 4; i++){ 
    printf("\n");
		for(x = 0; x <= 4; x++){
	    printf("[ %i ] ", matriz[i][x]);
	  }
	}
}
int ex3(){
	int i, x, m[5][5], soma, soma2, somad, somas = 0, somat;
	for(i = 0; i <= 4; i++){ 
		for(x = 0; x <= 4; x++){
	    printf("Digite o %i valor para a linha %i matriz M: ",(x+1), (i+1));
	    scanf("%i", &m[i][x]);
	  }
	}
	somaLinha(m, 4);
	somaColuna(m, 2);
  somaDiagPrincipal(m);
  somaDiagSecundaria(m);
  somaTotal(m);
  leituraMatriz(m);
  return 0;
}

int comparador(int gab[3],int nota[3]){
  int i, acerto = 0;
  for (i=0;i<3;i++){
    if(gab[i] == nota[i]){
      acerto++;
    }
  } 
  return acerto;
}
void acertos(int nota[10]){
  int i;
  for(i=0;i<10;i++){
    printf("O %iº candidato obteve %i porcento de acertos na prova",i,nota[i]);
  }
}
int ex4(){
	int i, x, gabarito[10], m[10][10], notas[10];  
  for (i=0;i<10;i++){
    printf("Informe o gabarito da %iª questão: ",(i+1));
    scanf("%i", &gabarito[i]);
  }//pega o gabarito
	for(i = 0; i < 10; i++){
    for(x = 0; x < 10; x++){
	    printf("Digite a %i resposta da prova do %iº aluno: ",(x+1), (i+1));
	    scanf("%i", &m[i][x]);
	  }
    notas[i] = comparador(gabarito, m[i]);
  }
  acertos(notas);
  return 0;
}

void distanciometro(int cidade1, int cidade2, int matriz[7][7]){
  printf("O tempo que um avião demora para percorrer de %i até %i é de %i horas.",cidade1,cidade2,matriz[cidade1][cidade2]);
}
void criaTabela(int m[7][7]){
  int i,x;
  for(i = 0; i < 7; i++){ 
		for(x = 0; x < 7; x++){
	    printf("[ %i ] ", m[i][x]);
	  }
    printf("\n");
	}
}
int ex5(){
	int i, x, d[7][7], cidade1 = 0, cidade2 = 1; 
  d[0] = {0,2,11,6,15,11,1};
  d[0][0] = 0;d[0][1] = 2;d[0][2] = 11;d[0][3] = 6;d[0][4] = 15;d[0][5] = 11;d[0][6] = 1;
  d[1][0] = 2;d[1][1] = 0;d[1][2] =  7;d[1][3] = 12;d[1][4] = 4;d[1][5] = 2;d[1][6] = 15;
  d[2][0] = 11;d[2][1] = 7;d[2][2] = 0;d[2][3] = 11;d[2][4] = 8;d[2][5] = 3;d[2][6] = 13;
  d[3][0] = 6;d[3][1] = 12;d[3][2] = 11;d[3][3] = 0;d[3][4] = 10;d[3][5] = 2;d[3][6] = 1;
  d[4][0] = 15;d[4][1] = 4;d[4][2] = 8;d[4][3] = 10;d[4][4] = 0;d[4][5] = 5;d[4][6] = 13;
  d[5][0] = 11;d[5][1] = 2;d[5][2] = 3;d[5][3] = 2;d[5][4] = 5;d[5][5] = 0; d[5][6] = 14;
  d[6][0] = 1;d[6][1] = 15;d[6][2] = 13;d[6][3] = 1;d[6][4] = 13;d[6][5]= 14;d[6][6] = 0;
  while (cidade1 != cidade2){
    printf("\nInforme qual a primeira cidade: ");
    scanf("%i",&cidade1);
    printf("\nInforme qual a primeira cidade: ");
    scanf("%i",&cidade2);
    distanciometro(cidade1, cidade2, d)    
  } 
  criaTabela(d);
  return 0;
}

int main(){
  ex1();
  ex2();
  ex3();
  ex4();
  ex5();
  return 0;
}