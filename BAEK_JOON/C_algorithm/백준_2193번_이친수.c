#include <stdio.h>
#define ull unsigned long long

ull fibo(ull n)
{
	ull temp,i,fi[2] = { 1, 1 };
	if (n <= 2)
		return fi[n - 1];
	else
	{
		for (i = 0; i < n - 2 ; i++)
		{
			temp = fi[1];
			fi[1] = fi[0] + fi[1];
			fi[0] = temp;
		}
		return fi[1];

	}
}
int main() {
	ull n;
	scanf("%d", &n);
	printf("%llu\n",fibo(n));
	return 0;
}