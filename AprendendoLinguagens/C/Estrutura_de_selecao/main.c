#include <stdio.h>

int ex1(){
	int maior, medio, menor, cont;
	maior = menor = medio = cont = 0;
	while (cont < 3){
		cont = cont + 1;
		printf("\nInsira o %i numero: ",cont);	
		scanf("%i",&menor);
		if (menor > medio){
			if(menor > maior){
				medio = maior;
				maior = menor;
			}else{
				medio = menor;
			}
		}
	}
	maior = maior + medio;
	printf("\nA soma dos dois valores é: %i",maior);
	return 0;
}
int ex2(){
	int maior, medio, menor, cont, aux;
	maior = menor = medio = cont = 0;
	while (cont < 3){
		cont = cont + 1;
		printf("\nInsira o %i numero: ",cont);	
		scanf("%i",&menor);
		if (menor > medio){
			if(menor > maior){
        aux = menor;
        menor = medio;
				medio = maior;
				maior = aux;
			}else{
				aux = menor;
        menor = medio;
        medio = aux;
			}
		}
	}
	printf("\nA ordem dos valores é 1º: %i, 2º: %i, 3º: %i",menor, medio, maior);
	return 0;
}
int ex3(){
  char nome[61];
  float atual, reaj;
  int porcentagem;
  printf("\nDigite seu nome: ");
  scanf("%s",nome);
  printf("\nInforme seu salário atual: ");
  scanf("%f",&atual);
  if (atual <= 300){
    porcentagem = 10;
  } else{
    if(atual <= 600){
      porcentagem = 11;
    } else{
      if(atual <= 900){
        porcentagem = 12;
      }else{
        if(atual <= 1500){
          porcentagem = 6;
        } else{
          if(atual <= 2000){
            porcentagem = 3;
          }else{
            porcentagem = 0;
          }
        }
      }
    }
  }
  reaj = atual + (atual*porcentagem/100);
  printf("\nO seu nome é: %s", nome);
  printf("\nO seu antigo salario é: %.2f",atual);
  printf("\nO reajuste foi de: %i",porcentagem);
  printf("\nO seu novo salario será de: %.2f",reaj);
	return 0;
}
int ex4(){
  char cpf[14];
  int dep, renda, minimo;
  float ali;
  printf("\nDigite seu cpf: ");
  scanf("%s",cpf);
  printf("\nInforme sua renda: ");
  scanf("%i",&renda);
  printf("\nInforme o atual salario minimo: ");
  scanf("%i",&minimo);
  printf("\nQuantos dependentes você tem? ");
  scanf("%i",&dep);
  switch (dep){
    case (0):
      dep = 0;
    case (1):
      dep = 5;
      break;
    case (2):
      dep = 10;
      break;
    case (3):
      dep = 15;
      break;
    default:
      dep = 15;
      break;
  }
  renda = renda + (renda*dep/100);
  if(renda <= (2*minimo)){
    ali = 0;
  }else{
    if(renda < (3*minimo)){  
      ali = renda*5/100;
    }else{
      if(renda < (5*minimo)){
        ali = renda*10/100;
      }else{
        if(renda <= (7*minimo)){
          ali = renda*15/100;
        }else{
          ali = renda*20/100;
        }
      }
    }
  }
  printf("\ncpf: %s\nValor da aliquota: %.2f",cpf,ali);
}
int ex5(){
  int cont = 1;
  while (cont <= 1000){
    if (cont%10 == 0){
      printf("\n%i",cont);
    }
    cont = cont + 1;
  }
}
int ex6(){
  int numero, limite, cont = 0, resultado;
  printf("Informe o número que deseja saber a tabuada: ");
  scanf("%i",&numero);
  printf("\nInforme o número limitador: ");
  scanf("%i",&limite);
  while (cont <= limite){
    resultado = cont * numero;
    printf("\n%i x %i = %i",numero,cont,resultado);
    cont = cont + 1;
  }
}
int ex7(){
  int negativos = 0, valor = 1, cont = 0;
  while ((valor != 0) && (cont < 5)){
    printf("Informe o número para cadastro: ");
    scanf("%i",&valor);
    if(valor<0){
      negativos = negativos + 1;
    }
    cont = cont + 1;
  }
  printf("Ao total foram cadastrados: %i",negativos);
}
int ex8(){
  int cont, aux=0;
  float total = 1;
  printf("Informe N: ");
  scanf("%i",&cont);
  while (aux < cont){
    aux ++;
    total = total + (float)1/aux;
  }
  printf("final E = %.2f",total);
}
int ex9 (void){
  int i = 1, n;
  float fat, result;
  printf("Digite um numero:\n");
  scanf("%d", &n);
  result = 1.0;
  fat = 1.0;
  while(i<=n){
    fat = fat * i;
    result = result + 1.0/fat;
    i++;
  }
  printf("O valor de E é: %f\n", result);
  return 0;
}
int ex10 (void){
  int ano = 0 ;
  float joao = 1.5, cj = 0.02, ze = 1.1, cz = 0.03;
  while (joao > ze){
    joao += cj;
    ze += cz;
    ano ++;
  }
  printf("\ndemorará %i anos para que zé chegue a altura de joão", ano);
  return 0;
}
int ex11 (void){
  int a1, n, r, aux = 1 ;
  printf("\nInforme quantos termos há na sua PA: ");
  scanf("%i",&n);
  printf("\nInforme o termo a1 de sua PA: ");
  scanf("%i",&a1);
  printf("\nInforme a razão de sua PA: ");
  scanf("%i",&r);
  printf("\na1 = %i",a1);
  while (aux < n){
    printf("\na%i = %i",aux,(a1 + aux*r));
    aux++;
  }
  return 0;
}
int ex12 (void){
  int c1 = 0, c2 = 0, c3 = 0, c4 = 0, n = 0, b = 0, v = 1;
  while (v != 0){
    printf("\nEm quem você irá votar? ");
    scanf("%i",&v);
    switch (v){
      case 1: c1++; break;
      case 2: c2++; break;
      case 3: c3++; break;
      case 4: c4++; break;
      case 5: n++; break;
      case 6: b++; break;
    }
  }
  printf("\n%i votos no candidato 1",c1);
  printf("\n%i votos no candidato 2",c2);
  printf("\n%i votos no candidato 3",c3);
  printf("\n%i votos no candidato 4",c4);
  printf("\n%i votos nulos",n);
  printf("\n%i votos em branco\n",b);
  return 0;
}
int main (void){
  printf("Hello");
}