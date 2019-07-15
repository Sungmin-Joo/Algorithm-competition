#include <stdio.h>
#include <string.h>
int main(void) {
	char buff[81];
	int n, i, j, scr, flag, sum;

	scanf("%d",&n);

	for (i = 0; i < n; i++)
	{
		scr = 1;
		flag = 0;
		sum = 0;
		scanf("%s", buff);
		for (j = 0; j < strlen(buff); j++)
		{
			if (buff[j] == 'O')
			{
				if (flag)
					sum += ++scr;
				else
				{
					flag = 1;
					sum += scr;
				}
			}
			else
			{
				flag = 0;
				scr = 1;
			}
		}
		printf("%d\n", sum);
	}
	return 0;
}