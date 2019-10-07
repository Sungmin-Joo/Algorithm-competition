#include <stdio.h>

int main() {
	int n, i, j, t;
	int arr[21][21];
	int arr_road[21][21];
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			scanf("%d", &arr[i][j]);
			arr_road[i][j] = arr[i][j];
		}
	}

	for (t = 1; t <= n; t++) {
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= n; j++) {
				if (i == t || j == t) continue;
				if (arr[i][j] > arr[i][t] + arr[t][j]) {
					printf("-1\n");
					return 0;
				}
				if (arr[i][j] == arr[i][t] + arr[t][j]) arr_road[i][j] = 0;
			}
		}
	}

	t = 0;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			t += arr_road[i][j];
		}
	}

	printf("%d\n", t/2);
	return 0;
}