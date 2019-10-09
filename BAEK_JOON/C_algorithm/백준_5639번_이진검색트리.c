#include <stdio.h>
int arr[10000];
void solution(int start, int end) {
	int root = arr[start], i = start + 1, j = end;
	if (start > end) return;
	
	while (arr[j] > root) j--;
	solution(i, j);
	solution(j + 1, end);
	printf("%d\n", root);

}

int main() {
	int n = 0, i = 0;
	while (scanf("%d", &n) != EOF) {
		arr[i++] = n;
	}
	solution(0, i - 1);
}