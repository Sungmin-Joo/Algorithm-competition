#include <stdio.h>
#include <string.h>
int count[26] = { 0 };
int main() {
	char str[1000000],flag = 0,*ptr;
	int len,i,max=0,index=0;
	scanf("%s", str);
	len = strlen(str);
	ptr = str;
	for(i =0 ; i < len; i++)
	{
		if (*ptr >= 97 && *ptr <= 122)
			count[(int)(*ptr - 97)]++;
		else
			count[(int)(*ptr - 65)]++;
		ptr++;
	}
	for (i = 0; i < 26; i++)
	{
		if (count[i] == max)
		{
			flag = 1;
		}
		else if (count[i] > max)
		{
			max = count[i];
			index = i;
			flag = 0;
		}
	}

	if (flag)
		putchar('?');
	else
		putchar(index+65);
	return 0;
}