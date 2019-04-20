#include <stdio.h>

void main() {
	int i, j, n;

	scanf("%d", &n);

	for (i = 1; i <= 2 * n - 1; i++)
	{
		if (i <= n)
		{
			for (j = 0; j < n - i; j++)
				putchar(' ');
			for (j = 0; j < (2 * i) - 1; j++)
				putchar('*');
		}
		else
		{
			for (j = 0; j < i - n; j++)
				putchar(' ');
			for (j = 0; j < ((2 * n) - 1) - 2 * (i - n); j++)
				putchar('*');
		}
		putchar('\n');
	}
}