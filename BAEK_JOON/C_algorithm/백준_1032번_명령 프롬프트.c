#include <stdio.h>
#include <string.h>

int main(void) {
	int n, i, j;
	char input[50][51], ans[51], index = 0;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		scanf("%s", input[i]);

	for (i = 0; i < strlen(input[0]) ; i++)
	{
		ans[index] = input[0][i];
		for (j = 1; j < n; j++)
		{
			if (ans[index] != input[j][i])
			{
				ans[index] = '?';
				break;
			}
		}
		index++;
	}
	ans[i] = '\0';
	printf("%s\n", ans);
	
	return 0;
}