#include<stdio.h>
int n, max, min, buf;
int main() {
	scanf("%d", &n);
	n--;
	scanf("%d", &min);
	max = min;
	while (n--) {
		scanf("%d", &buf);
		if (buf > max)
			max = buf;
		else if (buf < min)
			min = buf;
	}
	printf("%d %d", min, max);
	return 0;
}