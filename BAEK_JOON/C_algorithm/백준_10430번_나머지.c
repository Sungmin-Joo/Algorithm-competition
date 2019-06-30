#include <stdio.h>
#define A (a + b) % c
#define B ((a % c) + (b % c)) % c
#define C (a * b) % c
#define D ((a % c) * (b % c)) % c
int main(void) {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	//printf("%d\n%d\n%d\n%d\n", (a + b) % c, (a % c) + (b % c), (a * b) % c, (a % c) * (b % c));
	printf("%d\n%d\n%d\n%d\n", A, B, C, D);
	return 0;
}