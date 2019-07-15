#include <stdio.h>
#include <string.h>
int main(void) {
	char buff[101];
	int i, j;

	gets(buff);
	for (i = 0; i < strlen(buff); i++)
	{
		if (*(buff + i) >= 0x41 && *(buff + i) <= 0x5A)
		{
			if (*(buff + i) + 13 > 0x5A)
				*(buff + i) -= 0x1A;
			*(buff + i) += 13;
		}
		else if (*(buff + i) >= 0x61 && *(buff + i) <= 0x7A)
		{
			if (*(buff + i) + 13 > 0x7A)
				*(buff + i) -= 0x1A;
			*(buff + i) += 13;
		}
	}
	
	printf("%s", buff);
	return 0;
}