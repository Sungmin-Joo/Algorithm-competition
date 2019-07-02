#include <stdio.h>
int n;
int main()
{
	scanf_s("%d", &n);
	for (int i = 1; i <= 9; i++)
		printf("%d * %d = %d\n", n, i, n*i);
	return 0;
}