#include <stdio.h>
#define lln long long
int main(void) {
	lln  n, i, sum;
	scanf("%lld", &n);
	sum = 5;
	for (i = 2; i <= n; i++)
		sum += 3 * i + 1;
	printf("%lld", sum % 45678);
	return 0;
}