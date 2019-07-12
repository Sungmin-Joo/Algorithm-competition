#include <stdio.h>
int main(void) {
	int n, origin, cnt = 0;
	scanf("%d", &origin);
	n = origin;
	do {
		n = (n % 10) * 10 + (n / 10 + n % 10) % 10;
		cnt++;
	} while (!(origin == n));

	printf("%d\n", cnt);
	return 0;
}