#include <stdio.h>
#define sp putchar(' ')
#define st putchar('*')
#define en putchar('\n')
#define I i = 0
#define P i++
int main(void) {
	int n, i, j;
	scanf("%d", &n);
	for (j = 1; j < n; j++) {
		if (j == 1) {
			for (I; i < n; P) st;
			for (I; i < 2 * n - 3; P) sp;
			for (I; i < n; P) st; en;
		}
		else {
			for (I; i < j - 1; P) sp; st;
			for (I; i < n - 2; P) sp; st;
			for (I; i < 2 * (n - j + 1) - 3; P)	sp;	st;
			for (I; i < n - 2; P) sp; st; en;
		}
	}
	for (I; i < n - 1; P) sp; st;
	for (I; i < n - 2; P) sp; st;
	for (I; i < n - 2; P) sp; st; en;
	for (j = n - 1; j >= 1; j--) {
		if (j == 1) {
			for (I; i < n; P) st;
			for (I; i < 2 * n - 3; P) sp;
			for (I; i < n; P) st; en;
		}
		else {
			for (I; i < j - 1; P) sp; st;
			for (I; i < n - 2; P) sp; st;
			for (I; i < 2 * (n - j + 1) - 3; P) sp; st;
			for (I; i < n - 2; P) sp; st; en;
		}
	}
	return 0;
}