#include <stdio.h>
#include <stdlib.h>
int main(void) {
	int n, *arr, i, temp, j;
	scanf("%d",&n);
	//while (getchar() != '\n');
	arr = (int*)malloc(sizeof(int)*n);
	for (i = 0; i < n; i++){
		scanf("%d", arr+i);
		//while (getchar() != '\n');
	}
	i = 0;
	do {
		j = 0;
		do {
			if (*(arr + j) > *(arr + j + 1))
			{
				temp = *(arr + j);
				*(arr + j) = *(arr + j + 1);
				*(arr + j + 1) = temp;
			}
			j++;
		} while (j < n - 1 - i);
		i++;
	} while (i < n - 1);
	for (i = 0; i < n; i++)
		printf("%d\n", *(arr + i));
	free(arr);
	return 0;
}