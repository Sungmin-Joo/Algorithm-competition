#include <stdio.h>

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void quick_sort(int* array, int start, int end) {
	if (start >= end) return;
	int mid = (start + end) / 2;
	int pivot = array[mid];
	swap(&array[start], &array[mid]);
	int p = start + 1, q = end;
	while (1) {
		while (array[p] <= pivot) { p++; }
		while (array[q] > pivot) { q--; }
		if (p > q) break;
		swap(&array[p], &array[q]);
	}
	swap(&array[start], &array[q]);
	quick_sort(array, start, q - 1);
	quick_sort(array, q + 1, end);
}

int main() {
	int i, n, arr[10000] = { 0 }, mid, high, low = 0, result = 0;
	int tmp_sum, sum;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	scanf("%d", &sum);


	quick_sort(arr, 0, n - 1);
	high = arr[n - 1];
	low = 0;
	while (low <= high) {
		tmp_sum = 0;
		mid = (high + low) / 2;

		for (i = n - 1; i > -1; i--) {

			if (arr[i] < mid)
				tmp_sum += arr[i];
			else
				tmp_sum += mid;

			if (tmp_sum > sum)
				break;
		}
		if (tmp_sum > sum && high == low)
			high--, low--;
		else if (tmp_sum > sum) {
			high = mid;
		}
		else {
			low = mid + 1;
			result = mid;
		}


	}
	printf("%d\n", result);
	return 0;
}