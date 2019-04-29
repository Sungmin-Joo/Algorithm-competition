#include <stdio.h>
#include <math.h>

int main() {
	int n, m, cnt = 1, i, temp, buf, check;
	scanf("%d %d", &n, &m);
	if (n >= 10)
	{
		temp = n;
		while (1)
		{
			temp /= 10;
			cnt++;
			if (temp < 10)
				break;
		}
	}
	temp = 0;
	for (i = 0; i < n; i++)
	{
		temp += cnt;
		if (temp == m)
		{
			printf("%d", n);
			break;
		}
		else if (temp > m)
		{
			temp -= cnt;
			buf = n;
			while (temp != m)
			{
				check = buf / (pow(10.0, cnt - 1));
				printf("%d", check);
				buf = n%(int)(pow(10.0, cnt - 1));
				cnt--;
				temp++;
			}
			break;
		}
		else
			printf("%d", n);
	}
	putchar('\n');

	return 0;
}