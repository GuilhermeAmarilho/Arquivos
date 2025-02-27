#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int entradas(){
    printf("Ola, mundo!");
    printf("\n%i", 123);
    printf("\n%f", 4.56);
    printf("\nresultado: %i", 7 < 8);
    printf("\n%c", 'z');
    printf("\nBom dia, %s!\n", "usuario");
    printf("\n#%i", ((2 + 2 == 4) && (3 < 5)));
    return 0;
}
// Calcule a área A de um círculo de raio r=2, e apresente a medida na tela. Use uma variável auxiliar pi. A fórmula da área é A = π r2.
float aula_07_01_exercicio_01(){
    int raio;
    printf("Informe o raio do circulo: \n");
    scanf("%i", &raio);
    float pi = M_PI;
    float area = (raio * raio * pi);
    printf("A area do circulo de raio %i eh: %f", raio, area);
    return area;
}
// Escolha alguma temperatura em graus Celsius e atribua à variável C. Apresente esta convertida em Fahrenheit, usando a fórmula de conversão F = (9 * C + 160) / 5.
int aula_07_01_exercicio_02(){
    float c;
    printf("Informe a temperatura em oC: \n");
    scanf("%f", &c);
    printf("A temperatura de %.2f oC, equivale a %.2f oF", c, ((9*c + 160)/5));
    return 0;
}
// Leia um número inteiro i e indique se ele está fora do intervalo fechado [1, 10]
int aula_09_01_exercicio_01(){
    int value;
    while(1){
        printf("Informe o valor que deseja testar:\n-1 Para sair!\nSua resposta: ");
        scanf("%i", &value);
        if (value == -1){
            return 1;
        }else{
            if (value >= 0 && value <= 10){
                printf("O valor %i esta entre [0, 10]\n", value);
            }else{
                printf("O valor %i nao esta entre [0, 10]\n", value);
            }
        }
        printf("\n");
    }
}
// Leia dois valores inteiros a e b, então apresente os valores em ordem crescente
int aula_09_01_exercicio_02(){
    int a, b;
    printf("Informe o primeiro valor: ");
    scanf("%i", &a);
    printf("\nInforme o segundo valor: ");
    scanf("%i", &b);
    if(a > b){
        printf("\nA sequencia correta eh: %i, %i", a, b);
    }else{
        printf("\nA sequencia correta eh: %i, %i", b, a);
    }
    return 0;
}
// Leia um número real n e indique se ele é zero, positivo ou negativo
int aula_09_01_exercicio_03(){
    int a;
    printf("Informe o valor: ");
    scanf("%i", &a);
    if(a == 0){
        printf("\nO valor %i eh 0", a);
    }else{
        if(a > 0){
            printf("\nO valor %i eh maior que 0", a);
        }else{
            printf("\nO valor %i eh menor que 0", a);
        }
    }
    return 0;
}
int arrays(){
    char s[10] = "abcd";
    for (int i = 0; s[i] != '\0'; i++) {
        // Lendo como caractere
        printf("%c", s[i]);
        // retornara: a, b, c, d
    }
    printf("\n");
    char s1[10] = "abcd";
    printf("%s\n", s1);
    // retorna abcd
    char t[10];
    printf("Informe uma string com max 9 caracteres");
    fgets(t, 10, stdin);
    // Le a string completa de no maximo 9 caracteres
    printf("%s\n", t);
    int len = strlen("teste");
    printf("\nTamanho de \'teste\': %i", len);
    // retorna 5
    int comp = strcmp("bola", "dado");
    printf("\nComparando bola e dado: %i", comp);
    // retorna 0 (False)
    return 0;
}
// Escreva um programa que leia um número inteiro N e exiba os N primeiros números pares (faça usando o for). Exemplo: Entrada: 5 → Saída: 2 4 6 8 10.
int aula_14_01_exercicio_01(){
    int valor;
    printf("Informe o valor limitante: ");
    scanf("%i", &valor);
    for (int i = 1; i <= valor; i++){
        printf("%i\n", i*2);
    }   
    return 0;
}
// Leia 10 números inteiros e armazene em um vetor. Depois, mostre apenas os números pares.
int aula_14_01_exercicio_02(){
    int numeros[10], aux;
    for (int i = 0; i < 10; i++){
        printf("Informe o %i numero: ", (i+1));
        scanf("%i", &aux);
        numeros[i] = aux;
        printf("\n");
    }
    printf("\nOs Numeros pares sao:\n");
    for (int i = 0; i < 10; i++) {
        if (numeros[i] % 2 == 0) {
            printf("%d ", numeros[i]);
        }
    }
    return 0;
}
// Crie um programa que leia dois vetores de 5 elementos cada e exiba a soma dos elementos correspondentes.
int aula_14_01_exercicio_03(){
    int vetor1[5], vetor2[5], soma[5];
    for (int i = 0; i < 5; i++){
        printf("Informe o %i valor do 1 vetor: ", i+1);
        scanf("%i", &vetor1[i]);
        printf("Informe o %i valor do 2 vetor: ", i+1);
        scanf("%i", &vetor2[i]);
        printf("\n");
        soma[i] = vetor1[i] + vetor2[i];
    }
    for (int i = 0; i < 5; i++){
        printf("\n%i elemento: soma de %i + %i = %i", i+1, vetor1[i], vetor2[i], soma[i]);
    }
    return 0;
}
// Leia uma string e conte quantas vogais (a, e, i, o, u) ela possui.
int aula_14_01_exercicio_04(){
    char str[100];
    int count = 0;
    char c;
    printf("Digite uma string: ");
    // Coloca como limite 100 para não dar overflow
    fgets(str, sizeof(str), stdin);
    // Tirando o '\n' do final da string 
    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }
    for (size_t i = 0; i < strlen(str); i++) {
        c = tolower(str[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    printf("\nA string %s contem %d vogais!\n", str, count);
    return 0;
}
// Crie um programa que leia duas strings e informe se são iguais ou diferentes.
int aula_14_01_exercicio_05(){
    char str1[100], str2[100];
    printf("Digite a primeira string: ");
    fgets(str1, sizeof(str1), stdin);
    printf("Digite a segunda string: ");
    fgets(str2, sizeof(str2), stdin);
    // Remove o '\n' ao final das strings, se presente
    str1[strcspn(str1, "\n")] = '\0';
    str2[strcspn(str2, "\n")] = '\0';
    if (strcmp(str1, str2) == 0) {
        printf("As strings sao iguais.\n");
    } else {
        printf("As strings sao diferentes.\n");
    }
    return 0;
}
// Faça um procedimento linha() que recebe um parâmetro inteiro n e imprime na tela uma linha composta de n caracteres '#'. Teste este procedimento.
void linha(int size) {
    for (int i = 0; i < size; i++) {
        printf("#");
    }
    printf("\n");
}
int aula_16_01_exercicio_01() {
    int tam;
    printf("Informe a quantidade de # que deseja imprimir: ");
    scanf("%i", &tam);
    linha(tam);
    return 0;
}
// Faça um procedimento chamado quadrado(), que recebe um parâmetro inteiro n com o lado do quadrado a ser impresso, composto por caracteres '#'. Esse procedimento deve chamar o procedimento linha(). Teste este procedimento.
void quadrado(int n) {
    for (int i = 0; i < n; i++) {
        linha(n);
    }
}
int aula_16_01_exercicio_02() {
    int lado;
    printf("Informe o tamanho do lado do quadrado: ");
    scanf("%d", &lado);
    quadrado(lado);
    return 0;
}
// Faça um procedimento que recebe um char contendo uma letra e mostra se ela é vogal ou não (pode ser consoante ou qualquer outro caractere).
void verificaVogal(char letra) {
    letra = tolower(letra);
    if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') {
        printf("O caractere '%c' é uma vogal.\n", letra);
    } else {
        printf("O caractere '%c' não é uma vogal.\n", letra);
    }
}
int aula_16_01_exercicio_03() {
    char letra;
    printf("Digite um caractere: ");
    scanf(" %c", &letra);
    verificaVogal(letra);
    return 0;
}
// Escreva uma função que converta uma letra maiúscula em minúscula e vice-versa, se o caractere for uma letra. Caso contrário, o caractere deve ser mantido inalterado.
char converteLetra(char letra) {
    if (letra >= 'a' && letra <= 'z') {
        return letra - 32;
    } else if (letra >= 'A' && letra <= 'Z') {
        return letra + 32;
    }
    return letra;
}
int aula_16_01_exercicio_04() {
    char caractere;
    printf("Digite um caractere: ");
    scanf(" %c", &caractere);
    char convertido = converteLetra(caractere);
    printf("Caractere convertido: %c\n", convertido);
    return 0;
}
// Crie uma função que incrementa (adiciona 1) a uma variável inteira. 
void incrementa(int *valor) {
    (*valor)++;
}
int aula_21_01_exercicio_01() {
    int numero = 5;
    printf("Valor antes do incremento: %d\n", numero);
    incrementa(&numero);
    printf("Valor após o incremento: %d\n", numero);
    return 0;
}
// Crie uma função que ordena 3 números (sem usar vetores).
void ordena(int *a, int *b, int *c) {
    int temp;
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if (*a > *c) {
        temp = *a;
        *a = *c;
        *c = temp;
    }
    if (*b > *c) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
}
int aula_21_01_exercicio_02() {
    int x, y, z;
    printf("Digite 3 números: ");
    scanf("%d %d %d", &x, &y, &z);
    ordena(&x, &y, &z);
    printf("Números ordenados: %d %d %d\n", x, y, z);
    return 0;
}
// Crie uma função que ordena 3 números (usando vetores).
void ordena(int vetor[]) {
    int temp;
    for (int i = 0; i < 2; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (vetor[i] > vetor[j]) {
                temp = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = temp;
            }
        }
    }
}
int aula_21_01_exercicio_03() {
    int numeros[3];
    printf("Digite 3 números: ");
    for (int i = 0; i < 3; i++) {
        scanf("%d", &numeros[i]);
    }
    ordena(numeros);
    printf("Números ordenados: ");
    for (int i = 0; i < 3; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");
    return 0;
}
// Faça uma função que recebe um vetor de inteiros (tamanho passado por parâmetro) e transforme todos os elementos para o seu respectivo quadrado.
void quadradoVetor(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor[i] = vetor[i] * vetor[i];
    }
}
int aula_21_01_exercicio_04() {
    int tamanho;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);
    int vetor[tamanho];
    printf("Digite os elementos do vetor:\n");
    for (int i = 0; i < tamanho; i++) {
        scanf("%d", &vetor[i]);
    }
    quadradoVetor(vetor, tamanho);
    printf("Vetor com os elementos elevados ao quadrado:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
    return 0;
}
// Faça uma função que receba uma string e transforme todas as letras minúsculas para maiúsculas
void transformaMaiusculas(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = toupper(str[i]);
        }
    }
}
int aula_21_01_exercicio_05() {
    char string[100];
    printf("Digite uma string: ");
    fgets(string, sizeof(string), stdin);
    string[strcspn(string, "\n")] = '\0';
    transformaMaiusculas(string);
    printf("String em maiúsculas: %s\n", string);
    return 0;
}
// Faça uma função que receba três vetores. Ao final, o primeiro vetor deve ter a soma dos dois outro vetores.
void somaVetores(int vetor1[], int vetor2[], int vetor3[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor1[i] = vetor2[i] + vetor3[i];
    }
}
int aula_21_01_exercicio_06() {
    int tamanho;
    printf("Digite o tamanho dos vetores: ");
    scanf("%d", &tamanho);
    int vetor1[tamanho], vetor2[tamanho], vetor3[tamanho];
    printf("Digite os elementos do vetor 2:\n");
    for (int i = 0; i < tamanho; i++) {
        scanf("%d", &vetor2[i]);
    }
    printf("Digite os elementos do vetor 3:\n");
    for (int i = 0; i < tamanho; i++) {
        scanf("%d", &vetor3[i]);
    }
    somaVetores(vetor1, vetor2, vetor3, tamanho);
    printf("Vetor 1 (soma dos vetores 2 e 3):\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor1[i]);
    }
    printf("\n");
    return 0;
}
// Use alocação dinâmica para construir a string resultante para a concatenação das strings “copa” e “cabana”. Não esqueça do terminador.
char* concatena(const char* str1, const char* str2) {
    int tamanho = strlen(str1) + strlen(str2) + 1;
    char* resultado = (char*)malloc(tamanho * sizeof(char));
    if (resultado == NULL) {
        printf("Erro de alocação de memória.\n");
        exit(1);
    }
    strcpy(resultado, str1);
    strcat(resultado, str2);
    return resultado;
}
int aula_21_01_exercicio_07() {
    const char* str1 = "copa";
    const char* str2 = "cabana";
    char* resultado = concatena(str1, str2);
    printf("Resultado da concatenação: %s\n", resultado);
    free(resultado);
    return 0;
}
// Crie uma função que recebe uma string e que devolve uma nova string, alocada dinamicamente, com todas as vogais removidas. Teste esta função passando duas strings distintas.
char* removeVogais(const char* str) {
    int tamanho = strlen(str);
    char* novaString = (char*)malloc((tamanho + 1) * sizeof(char));
    if (novaString == NULL) {
        printf("Erro de alocação de memória.\n");
        exit(1);
    }
    int j = 0;
    for (int i = 0; i < tamanho; i++) {
        char c = tolower(str[i]);
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
            novaString[j++] = str[i];
        }
    }
    novaString[j] = '\0';
    return novaString;
}
int aula_21_01_exercicio_08() {
    char str1[] = "Copacabana";
    char str2[] = "Hello World";
    char* resultado1 = removeVogais(str1);
    char* resultado2 = removeVogais(str2);
    printf("String original: %s -> Sem vogais: %s\n", str1, resultado1);
    printf("String original: %s -> Sem vogais: %s\n", str2, resultado2);
    free(resultado1);
    free(resultado2);
    return 0;
}

int main() {
    aula_16_01_exercicio_04();
    return 0;
}