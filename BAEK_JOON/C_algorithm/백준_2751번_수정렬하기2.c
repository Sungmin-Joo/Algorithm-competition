#include <stdio.h>
#include <stdlib.h>

void quickSort(int i, int j, int *arr)
{
	if (i >= j) return;
	int pivot = arr[(i + j) / 2];
	int left = i;
	int right = j;
	int temp;

	while (left <= right) {
		while (arr[left] < pivot) left++;
		while (arr[right] > pivot) right--;
		if (left <= right) {
			temp = arr[left];
			arr[left] = arr[right];
			arr[right] = temp;
			left++; right--;
		}
	}
	quickSort(i, right, arr);
	quickSort(left, j, arr);
}

int main(void) {
	int i, n, *arr;
	scanf("%d", &n);
	arr = (int*)calloc(n, sizeof(int));

	for (i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	quickSort(0, n - 1, arr);

	for (i = 0; i < n; i++) {
		printf("%d\n",arr[i]);
	}
	free(arr);
	return 0;
}