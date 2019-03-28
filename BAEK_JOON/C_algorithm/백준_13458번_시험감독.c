#include <stdio.h> 
#include <stdlib.h>
int i = 0, N, B, C, *A;
long long sum = 0;
int main() {
	scanf("%d", &N);
	A = (unsigned long long*)malloc(sizeof(unsigned long long) * N);
	for (i = 0; i<N; i++)
	{
		scanf("%d", &A[i]);
	}
	scanf("%d %d", &B, &C);
	
	for (i = 0; i < N; i++)
	{
		sum++;
		A[i] = A[i] - B;
		if (A[i] < 0) { continue; }
		if (A[i] % C){	sum += (A[i] / C) + 1;	}
		else{	sum += (A[i] / C);	}
	
	}
	printf("%llu\n", sum);
	free(A);
	return 0;
}