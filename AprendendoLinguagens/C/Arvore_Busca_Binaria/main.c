#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo {
  int dado;
  struct Nodo *direita;
  struct Nodo *esquerda;
} Nodo;

// prototipação
Nodo *insere(Nodo *, int);
Nodo *remover(Nodo *, int);
Nodo *criarNodo(int);
void preOrdem(Nodo *);
void emOrdem(Nodo *);
void posOrdem(Nodo *);

Nodo *insere(Nodo *nodo, int dado) {
  Nodo *novoNodo = criarNodo(dado);
  if (nodo != NULL) {
    if (nodo->dado > novoNodo->dado)
      nodo->esquerda = insere(nodo->esquerda, dado);
    else if (nodo->dado <= novoNodo->dado)
      nodo->direita = insere(nodo->direita, dado);
  } else
    nodo = novoNodo;
  return nodo;
}

Nodo *remover(Nodo *raiz, int chave) {
  if (raiz == NULL) {
    printf("Valor nao encontrado!\n");
    return NULL;
  } else {
    // procura o no a remover
    if (raiz->dado == chave) {
      // no sem filhos
      if (raiz->esquerda == NULL && raiz->direita == NULL) {
        free(raiz);
        return NULL;
      } else {
        // no que possui 2 filhos
        if (raiz->esquerda != NULL && raiz->direita != NULL) {
          Nodo *aux = raiz->esquerda;
          while (aux->direita != NULL)
            aux = aux->direita;
          // Elemento mai a direita da subarvore a esquerda
          raiz->dado = aux->dado;
          aux->dado = chave;
          // Passa o elemento a esquerda para a pseudoraiz
          raiz->esquerda = remover(raiz->esquerda, chave);
          return raiz;
        }
        // no que possui 1 filho
        else {
          Nodo *aux;
          if (raiz->esquerda != NULL)
            aux = raiz->esquerda;
          else
            aux = raiz->direita;
          free(raiz);
          return aux;
        }
      }
    } else {
      if (chave < raiz->dado)
        raiz->esquerda = remover(raiz->esquerda, chave);
      else
        raiz->direita = remover(raiz->direita, chave);
      return raiz;
    }
  }
}

Nodo *criarNodo(int dado) {
  Nodo *nodo = (Nodo *)malloc(sizeof(Nodo));
  nodo->dado = dado;
  nodo->direita = NULL;
  nodo->esquerda = NULL;

  return nodo;
}

void preOrdem(Nodo *nodo) { // Profundidade - Sempre esquerda
  printf("%i ", nodo->dado);
  // Verifica a existencia dos filhos, caso sim, imprime eles
  if (nodo->esquerda != NULL)
    preOrdem(nodo->esquerda);
  if (nodo->direita != NULL)
    preOrdem(nodo->direita);
}

void emOrdem(Nodo *nodo) { // Simétrica - ordem crescente
  if (nodo->esquerda != NULL)
    emOrdem(nodo->esquerda);
  printf("%i ", nodo->dado);
  if (nodo->direita != NULL)
    emOrdem(nodo->direita);
}

void posOrdem(Nodo *nodo) { // Largura - primeiro as pontas - Esq
  if (nodo->esquerda != NULL)
    posOrdem(nodo->esquerda);
  if (nodo->direita != NULL)
    posOrdem(nodo->direita);
  printf("%i ", nodo->dado);
}

int main(void) {
  Nodo *raiz = criarNodo(15);
  insere(raiz, 25);
  insere(raiz, 35);
  insere(raiz, 45);
  insere(raiz, 65);
  insere(raiz, 55);
  insere(raiz, 44);
  insere(raiz, 34);
  insere(raiz, 24);
  insere(raiz, 10);
  insere(raiz, 15);
  raiz = remover(raiz, 25);
  raiz = remover(raiz, 35);
  raiz = remover(raiz, 15);
  insere(raiz, 42);
  insere(raiz, 40);
  insere(raiz, 43);
  raiz = remover(raiz, 44);
  insere(raiz, 60);
  insere(raiz, 70);
  insere(raiz, 50);
  insere(raiz, 67);
  insere(raiz, 64);
  raiz = remover(raiz, 65);
  printf("Impressão\n");
  preOrdem(raiz);
  printf("\n10 24 15 34 45 42 40 43 64 55 50 60 70 67");
  printf("\nBase de teste");
}
