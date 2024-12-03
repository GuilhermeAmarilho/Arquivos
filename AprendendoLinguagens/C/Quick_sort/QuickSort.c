#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#define MAXVALUE 10000
#define SIZEVETOR 10
#define MAX 10

void quick_sort(int *a, int left, int right);

int main (int argc, char** argv) {
	int i, vet[MAX];
	for (i = 0; i < MAX; i++) {
		printf("Digite um valor: ");
		scanf("%d", &vet[i]);
	}
	quick_sort(vet, 0, MAX - 1);
	printf("\n\nValores ordenados\n");
	for (i = 0; i < MAX; i++) {
		printf("%dn", vet[i]);
	}
	system("pause");
	return 0;
}
void quick_sort (int *a, int left, int right) {
	int i, j, x, y;
	i = left;
	j = right;
	x = a[(left + right) / 2];
	while (i <= j) {
		while (a[i] < x && i < right) {
			i++;
		}
		while (a[j] > x && j > left) {
			j--;
		}
		if (i <= j) {
			y = a[i];
			a[i] = a[j];
			a[j] = y;
			i++;
			j--;
		}
	}
	if (j > left) {
		quick_sort(a, left, j);
	}
	if (i < right) {
		quick_sort(a, i, right);
	}
}