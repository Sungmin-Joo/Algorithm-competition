#include <stdio.h>
int main(){
	int i, j, c = 0;

	char buf[9];
	for (i = 0; i < 8; i++)
	{
		scanf("%s", buf);
		//while (getchar() != '\n');
		for (j = 0; j < 8; j++)
		{
			if (buf[j] == 'F')
			{
				if (i % 2 == 0 && j % 2 == 0)
					c++;
				else if (i % 2 == 1 && j % 2 == 1)
					c++;
			}
		}
	}
	printf("%d", c);
	return 0;
}