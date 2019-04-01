#include <stdio.h>
int main() {
	int  N, a, b, ball = 1;
	scanf("%d", &N);
	while(N--)
	{
		scanf("%d %d", &a, &b);
		if (a == ball)
		{
			ball = b;
		}
		else if(b == ball)
		{
			ball = a;
		}
	}
	printf("%d\n",ball);
	return 0;
}