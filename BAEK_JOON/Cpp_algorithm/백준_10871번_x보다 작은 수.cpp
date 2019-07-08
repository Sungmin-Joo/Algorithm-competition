#include<stdio.h>
int main() {
	int n, x, temp;
	scanf("%d %d", &n, &x);
	
	while (n--) {
		scanf("%d", &temp);
		if (temp<x)
			printf("%d ", temp);
	}
	return 0;
}