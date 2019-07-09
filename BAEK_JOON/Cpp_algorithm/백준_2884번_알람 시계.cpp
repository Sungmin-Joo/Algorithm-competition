#include<stdio.h>
int h, m, total;
int main() {
	scanf_s("%d %d", &h, &m);
	total = 60 * h + m;
	total -= 45;

	if (total < 0)
		total = 1440 + total;
	printf("%d %d", total / 60, total % 60);

	return 0;
}