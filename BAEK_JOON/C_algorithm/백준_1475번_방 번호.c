#include <stdio.h>
#include <string.h>
int main() {
	int i, c_s = 0, cnt[8] = { 0 }, max = 0;
	char str[8],*ptr;
	scanf("%s", str);
	i = strlen(str);
	ptr = str;
	while (i--)
	{
		if (*ptr == '9' || *ptr == '6')
			c_s++;
		else
			switch (*ptr)
			{
			case '0':
				cnt[0]++;
				break;
			case '1':
				cnt[1]++;
				break;
			case '2':
				cnt[2]++;
				break;
			case '3':
				cnt[3]++;
				break;
			case '4':
				cnt[4]++;
				break;
			case '5':
				cnt[5]++;
				break;
			case '6':
				cnt[6]++;
				break;
			case '8':
				cnt[7]++;
				break;
			default:
				break;
			}
		ptr++;
	}

	for (i = 0; i < 8; i++)
	{
		if (max < cnt[i])
			max = cnt[i];
	}

	cnt[7] = (c_s / 2) + (c_s % 2);
	if (max < cnt[7])
		max = cnt[7];

	printf("%d\n", max);
	return 0;
}