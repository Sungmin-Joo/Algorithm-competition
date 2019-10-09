#include <stdio.h>

int main() {
	int t, i, j, n, arr[10001] = { 0 };
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &t);
		arr[t]++;
	}
	
	for (i = 1; i < 10001; i++) {
		if (arr[i] != 0) {
			for (j = 0; j < arr[i]; j++) {
				printf("%d\n",i);
			}
		}
	}
}