#include <stdio.h>
int main() {
	int n,i,a,b,c,cnt = 0;
	scanf("%d", &n);
	if (n < 100)
		cnt = n;
	else
	{
		for (i = 100; i <= n; i++)
		{
			a = i % 10;
			b = (i % 100) / 10;
			c = i / 100;
			if ((c - b) == (b - a))
				cnt++;
		}
		cnt += 99;
	}
	printf("%d", cnt);
	return 0;
}