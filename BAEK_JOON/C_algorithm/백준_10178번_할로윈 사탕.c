#include <stdio.h>
int main() {
	int  N, a, b;
	scanf("%d", &N);
	while(N--)
	{
		scanf("%d %d", &a, &b);
		printf("You get %d piece(s) and your dad gets %d piece(s).\n", a / b, a%b);
	}
	return 0;
}