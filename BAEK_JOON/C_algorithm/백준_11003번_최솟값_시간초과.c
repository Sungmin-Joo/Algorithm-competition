#include <stdio.h> 
#include <stdlib.h>
int i = 0, N, L, *A, j= 0,temp,t;
int min = 0;
int main() {
	scanf("%d %d", &N, &L);
	A = (int*)malloc(sizeof(int) * L);
	
	for (i = 0; i<N; i++)
	{
		if (i < L)
		{
			scanf("%d", &A[i]);
			if(i)
			{
				if (A[i] < min)
				{
					min = A[i];
				}
			}
			else
			{
				min = A[i];
			}
		}
		else
		{
			temp = A[j];
			scanf("%d", &A[j]);
			if (temp == min)
			{
				if (A[j] <= temp)
				{
					min = A[j];
				}
				else
				{
					min = A[0];
					for (t = 1; t < L; t++)
					{
						if (A[t] < min)
						{
							min = A[t];
						}
					}
				}
			}
			else
			{
				if (A[j] < min)
				{
					min = A[j];
				}
			}
			if (j >= L - 1)
			{
				j = 0;
			}
			else
			{
				j++;
			}
		}
		printf("%d ", min);
	}
	free(A);
	return 0;
}