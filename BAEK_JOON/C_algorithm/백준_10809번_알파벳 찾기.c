#include <stdio.h>
#include <string.h>

int main(void) {
	char str[101], num[26];
	int i, len, t;
	
	scanf("%[^\n]s",str);
	len = strlen(str);

	for (i = 0; i < 26; i++)
		num[i] = -1;

	for (i = 0; i < len; i++)
	{
		t = *(str + i) - 0x61;
		if(num[t] == -1)
			num[t] = i;
	}

	for (i = 0; i < 25; i++)
		printf("%d ", num[i]);

	printf("%d", num[25]);
	return 0;
}