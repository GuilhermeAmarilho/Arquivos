//faça um programa que calcule o salário líquido dos funcionários de uma empresa. O salário líquido é composto por descontos e adicionais, seguindo as seguintes regras: Descontos: Salário bruto < 800,00 – não realizar nenhum desconto; 800,00 <= Salário bruto <=1600,00 – descontar 8% de Imposto de Renda e 5% de encargos. Salário bruto > 1600,00 – descontar 15% de Imposto de Renda e 7% de encargos. Adicionais: Caso o funcionário tenha trabalhado mais de 160 horas no mês, divida o seu salário bruto por 160 (representa horas trabalhadas) e calcule 50% de adicional nas horas que excederem a 160. O usuário deverá digitar o salário bruto e o número de horas trabalhadas no mês de cada funcionário, e deverá receber como resultado o salário líquido. Para finalizar o programa o usuário deverá digitar 0 no salário bruto, ao finalizar o programa exibir o total geral dos salários líquidos.
#include <cstdio>
int exx (void){
  int horas;
  float bruto = 1, impostorenda, encargos, auxiliar, totalsalarios = 0; 
  do{
    impostorenda = 0.0;
    encargos = 0.0;
    auxiliar = 0;
    printf("\nInforme seu salário bruto: (0 para sair) ");
    scanf("%f",&bruto);
    if(bruto != 0){
      printf("\nInforme quantas horas você trabalhou esse mês: ");
      scanf("%i",&horas);
    }
    if(bruto > 1600) {
      encargos = bruto*7/100;
      impostorenda = bruto*15/100;
    }else{
      if(bruto >= 800){
        encargos = bruto*5/100;
        impostorenda = bruto*8/100;
      }
    }if(horas >= 160){
      auxiliar = horas/160 * (horas - 160);
    }
    bruto = bruto + auxiliar - encargos - impostorenda;
    printf("\nSeu salário liquido é de: %.2f\n foram descontados %.2f de imposto de renda e %.2f de encargos.",bruto, impostorenda, encargos);
    totalsalarios += bruto;
  }while (bruto != 0);
  printf("O total de salários calculados foi de: %.2f", totalsalarios);
  return 0;
}

//Faça um programa que receba duas notas de 6 alunos calcule e imprima: A média entre essas 2 notas de cada aluno. A mensagem de acordo com a tabela abaixo. O total de alunos aprovados e o total de alunos reprovados; A média geral do Programa, isto é, a média entre as médias dos alunos. 

int exx1 (void){
  int nota1, nota2, aprovados = 0, recuperacao = 0, reprovados = 0, contador;
  float media, mediatotal; 
  for (contador = 0; contador < 6; contador++){
    \
    printf("\nInforme sua primeira nota: ");
    scanf("%i",&nota1);
    printf("\nInforme sua segunda nota: ");
    scanf("%i",&nota2);
    media = (nota1 + nota2) / 2;
    if(media>=7){
      aprovados++;
      printf("Você está aprovado!\nSua média foi de: %.2f",media);
    }else{
      if(media>5){
        recuperacao++;
        printf("Você está em recuperação!\nSua média foi de: %.2f",media);
      }else{
        reprovados++;
        printf("Você está reprovado!\nSua média foi de: %.2f",media);
      }
    }
    mediatotal += media;
  }
  printf("\nO total de alunos aprovados foi: %i",aprovados);
  printf("\nO total de alunos em recuperação foi: %i",recuperacao);
  printf("\nO total de alunos reprovados foi: %i",reprovados);
  printf("\nA média total do programa foi: %.2f",mediatotal);
  return 0;
}

// Exercicios feitos na furg

// Escreva um programa que leia um número inteiro N e exiba os N primeiros números pares (faça usando o for).
int ex1(void) {
    int valor, i = 0;
    printf("\nInforme o valor desejado: ");
    scanf("%i", &valor);

    for (int repeticao = 0; repeticao < valor; i++) {
        if (i % 2 == 0) {
            printf("%i ", i);
            repeticao++;
        }
    }
    return 0;
}

// Leia 10 números inteiros e armazene em um vetor. Depois, mostre apenas os números pares.
int ex2(void) {
    int numeros[10];

    printf("Informe 10 números inteiros:\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &numeros[i]);
    }
    // Exibir os números pares
    printf("Números pares:\n");
    for (int i = 0; i < 10; i++) {
        if (numeros[i] % 2 == 0) {
            printf("%d ", numeros[i]);
        }
    }
    return 0;
}

// Crie um programa que leia dois vetores de 5 elementos cada e exiba a soma dos elementos correspondentes.
int ex3(){
    int vetor1[5], vetor2[5], soma[5];
    printf("Informe 5 elementos para o primeiro vetor:\n");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &vetor1[i]);
    }
    printf("Informe 5 elementos para o segundo vetor:\n");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &vetor2[i]);
    }
    printf("Soma dos elementos correspondentes:\n");
    for (int i = 0; i < 5; i++) {
        soma[i] = vetor1[i] + vetor2[i];
        printf("%d ", soma[i]);
    }
    return 0;
}
// Leia uma string e conte quantas vogais (a, e, i, o, u) ela possui.
int main(void) {
    char str[100];
    int contador = 0;
    printf("Informe uma string: ");
    fgets(str, sizeof(str), stdin);

    // Contagem das vogais
    for (int i = 0; i < strlen(str); i++) {
        // Verifica se o caractere é uma vogal (maiúscula ou minúscula)
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
            str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U') {
            contador++;
        }
    }

    // Exibindo o resultado
    printf("A string possui %d vogais.\n", contador);

    return 0;
}

// Crie um programa que leia duas strings e informe se são iguais ou diferentes

