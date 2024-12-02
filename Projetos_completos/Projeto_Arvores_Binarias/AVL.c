#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo {
  int dado, altura;
  struct Nodo *direita;
  struct Nodo *esquerda;
} Nodo;

// prototipação
Nodo *insere(Nodo *, int);
Nodo *remover(Nodo *, int);
Nodo *removerAoEncontrar(Nodo *, int);
Nodo *criarNodo(int);
void preOrdem(Nodo *);
void emOrdem(Nodo *);
void posOrdem(Nodo *);
Nodo *rotaDDir(Nodo *);
Nodo *rotaDEsq(Nodo *);
Nodo *rotaEsqDir(Nodo *);
Nodo *rotaDirEsq(Nodo *);

// Descobre a altura de um elemento da arvore com base na altura de deus filhoss
int altura(Nodo *raiz) {
  int alt_esq, alt_dir;
  if (raiz == NULL)
    return 0;
  // Verifica a altura da subarvore a esquerda
  if (raiz->esquerda == NULL)
    alt_esq = 0;
  // Caso possua filho a esquerda
  else
    alt_esq = 1 + raiz->esquerda->altura;
  // Verifica a altura da subarvore a direita
  if (raiz->direita == NULL)
    alt_dir = 0;
  // Caso possua filho a direita
  else 
    alt_dir = 1 + raiz->direita->altura;
  // Define qual é maior 
  if (alt_esq > alt_dir)
    return alt_esq;
  return alt_dir;
}

// rotacao simples direita
Nodo *rotaDir(Nodo *raiz) {
  Nodo *aux = raiz->esquerda;
  raiz->esquerda = aux->direita;
  aux->direita = raiz;
  // Define as novas alturas
  raiz->altura = altura(raiz);
  aux->altura = altura(aux);
  return aux;
}

// rotacao simples esquerda
Nodo *rotaEsq(Nodo *raiz) {
  Nodo *aux = raiz->direita;
  raiz->direita = aux->esquerda;
  aux->esquerda = raiz;
  // Define as novas alturas
  raiz->altura = altura(raiz);
  aux->altura = altura(aux);
  return aux;
}

// rotacao esq-direita
Nodo *rotaEsqDir(Nodo *raiz) {
  raiz->esquerda = rotaEsq(raiz->esquerda);
  raiz = rotaDir(raiz);
  return raiz;
}

// rota dir-esq
Nodo *rotaDirEsq(Nodo *raiz) {
  raiz->direita = rotaDir(raiz->direita);
  raiz = rotaEsq(raiz);
  return raiz;
}

int fatorBal(Nodo *raiz) {
  int alt_esq, alt_dir;
  if (raiz == NULL)
    return 0;
  // Definindo altura para a esquerda
  if (raiz->esquerda == NULL)
    alt_esq = 0;
  // Caso exista filho a esquerda 
  else {
    alt_esq = 1 + raiz->esquerda->altura;
  }
  // Definindo altura para a direita  
  if (raiz->direita == NULL)
    alt_dir = 0;
  // Caso exista filho a direita 
  else {
    alt_dir = 1 + raiz->direita->altura;
  }
  return (alt_esq - alt_dir);
}

Nodo *insere(Nodo *raiz, int valor) {
  if (raiz == NULL) {
    raiz = criarNodo(valor);
  } else {
    // Avança para a direita
    if (valor > raiz->dado) {
      // Segue avançando até conseguir chegar
      raiz->direita = insere(raiz->direita, valor);
      // Caso encontre um desbalanceamento no meio do caminho
      if (fatorBal(raiz) == -2) {
        // Caso filho sem cotovelo
        if (valor > raiz->direita->dado)
          raiz = rotaEsq(raiz);
        // Caso filho com cotovelo
        else
          raiz = rotaDirEsq(raiz);
      }
    } else {
    // Avança para a esquerda
      if (valor <= raiz->dado) {
        // Segue avançando até conseguir chegar
        raiz->esquerda = insere(raiz->esquerda, valor);
        // Caso encontre um desbalanceamento no meio do caminho
        if (fatorBal(raiz) == 2) {
          // Caso filho sem cotovelo
          if (valor < raiz->esquerda->dado)
            raiz = rotaDir(raiz);
          // Caso filho com cotovelo
          else
            raiz = rotaEsqDir(raiz);
        }
      }
    }
  }
  // Redefine a altura
  raiz->altura = altura(raiz);
  return raiz;
}

Nodo *removerAoEncontrar(Nodo *nodo, int dado) {
  // se nodo for folha
  if (nodo->esquerda == NULL && nodo->direita == NULL) {
    free(nodo);
    nodo = NULL;
  } else {
    // O nodo possui subarvore somenta à direita
    if (nodo->esquerda == NULL) {
      Nodo *temp = nodo; // Nodo temporário que aponta para o elemento atual
      nodo = nodo->direita;
      free(temp);
    } else {
      // O nodo possui subarvore somenta à esquerda
      if (nodo->direita == NULL) {
        Nodo *temp = nodo; // Nodo temporário que aponta para o elemento atual
        nodo = nodo->esquerda;
        free(temp);
      } 
      // O nodo possui duas subarvores
      else { 
        Nodo *sae = nodo->esquerda;
          while (sae->direita != NULL) {
            sae = sae->direita;
          }
          // trocando valor do nodo a ser removido com o nodo encontrado
          nodo->dado = sae->dado;
          sae->dado = dado;        
          // removendo o ultimo nodo à direita da subarvore da esquerda
          nodo->esquerda = remover(nodo->esquerda, dado);
          return nodo;
      }
    }
  }
  return nodo;
}

Nodo *remover(Nodo *nodo, int dado) {
  if (nodo == NULL) 
    return NULL;
  // Avança para a direita
  if (nodo->dado > dado) {
    // Segue avançando até conseguir achar
    nodo->esquerda = remover(nodo->esquerda, dado);
    // Caso encontre um desbalanceamento no meio do caminho
    if (fatorBal(nodo) == 2) {
      // Caso filho sem cotovelo
      if (dado < nodo->esquerda->dado)
        nodo = rotaDir(nodo);
      // Caso filho com cotovelo
      else
        nodo = rotaEsqDir(nodo);
    }
  } else {
    // Avança para a esquerda
    if (nodo->dado < dado) {
    // Segue avançando até conseguir achar      
      nodo->direita = remover(nodo->direita, dado);
      // Caso encontre um desbalanceamento no meio do caminho
      if (fatorBal(nodo) == -2) {
        // Caso filho sem cotovelo
        if (dado > nodo->direita->dado)
          nodo = rotaEsq(nodo);
        // Caso filho com cotovelo
        else
          nodo = rotaDirEsq(nodo);
      }
    } else { // Ao encontrar o elemento
      nodo = removerAoEncontrar(nodo, dado);
    }
  }
  return nodo;
}

Nodo *criarNodo(int dado) {
  Nodo *nodo = (Nodo *)malloc(sizeof(Nodo));
  nodo->dado = dado;
  nodo->altura = 0;
  nodo->direita = NULL;
  nodo->esquerda = NULL;
  return nodo;
}

void preOrdem(Nodo *nodo) {
  printf("%i ", nodo->dado);
  if (nodo->esquerda != NULL) {
    preOrdem(nodo->esquerda);
  }
  if (nodo->direita != NULL) {
    preOrdem(nodo->direita);
  }
}

void emOrdem(Nodo *nodo) {
  if (nodo->esquerda != NULL) {
    emOrdem(nodo->esquerda);
  }
  printf("%i ", nodo->dado);
  if (nodo->direita != NULL) {
    emOrdem(nodo->direita);
  }
}

void posOrdem(Nodo *nodo) {
  if (nodo->esquerda != NULL) {
    posOrdem(nodo->esquerda);
  }
  if (nodo->direita != NULL) {
    posOrdem(nodo->direita);
  }
  printf("%i ", nodo->dado);
}

int main(void) {
  Nodo *raiz = criarNodo(15);
  raiz = insere(raiz, 25);
  raiz = insere(raiz, 35);
  raiz = insere(raiz, 45);
  raiz = insere(raiz, 65);
  raiz = insere(raiz, 55);
  raiz = insere(raiz, 44);
  raiz = insere(raiz, 34);
  raiz = insere(raiz, 24);
  raiz = insere(raiz, 10);
  raiz = insere(raiz, 15);
  raiz = remover(raiz, 25);
  raiz = remover(raiz, 35);
  raiz = remover(raiz, 15);
  raiz = insere(raiz, 42);
  raiz = insere(raiz, 40);
  raiz = insere(raiz, 43);
  raiz = remover(raiz, 44);
  raiz = insere(raiz, 60);
  raiz = insere(raiz, 70);
  raiz = insere(raiz, 50);
  raiz = insere(raiz, 67);
  raiz = insere(raiz, 64);
  raiz = remover(raiz, 65);

  printf("PreOrdem\n");
  preOrdem(raiz);
  printf("\n42 24 10 15 34 40 60 45 43 55 50 67 64 70");
  printf("\nvalidação");
  return 0;
}
