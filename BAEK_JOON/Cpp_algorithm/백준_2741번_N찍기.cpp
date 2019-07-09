#include<stdio.h>
int n;
int main() {
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++)
		printf("%d\n", i);
	return 0;
}