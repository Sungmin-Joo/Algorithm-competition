#include <stdio.h>

int main(void) {
	int n, i, j, buf;
	int *p;
	scanf("%d", &n);
	
	p = (int *)malloc(sizeof(int) * n);
	
	for (i = 0; i < n; i++)
		scanf("%d", (p+i));
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n - 1; j++)
		{
			if (*(p + j) > *(p + j + 1))
			{
				buf = *(p + j);
				*(p + j) = *(p + j + 1);
				*(p + j + 1) = buf;
			}
		}
	}
		
	buf = 0;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j <= i; j++)
			buf += *(p + j);

	}

	printf("%d", buf);

	free(p);
	return 0;
}