#include <stdio.h>
int main() {
	int n,m=0,a,b;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d %d", &a, &b);
		if (a >= 1 && a <= 21)
		{
			if (a == 1)
				m = 5000000;
			else if (a <= 3)
				m = 3000000;
			else if (a <= 6)
				m = 2000000;
			else if (a <= 10)
				m = 500000;
			else if (a <= 15)
				m = 300000;
			else if (a <= 21)
				m = 100000;
		}
		else
			m = 0;

		if (b >= 1 && b <= 31)
		{
			if (b == 1)
				m += 5120000;
			else if (b <= 3)
				m += 2560000;
			else if (b <= 7)
				m += 1280000;
			else if (b <= 15)
				m += 640000;
			else if (b <= 31)
				m += 320000;
		}
		printf("%d\n", m);
	}
}