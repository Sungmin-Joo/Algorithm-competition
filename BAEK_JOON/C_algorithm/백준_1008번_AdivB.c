#include <stdio.h>
int main() {
	long double a,b;
	scanf("%Lf %Lf", &a, &b);
	printf("%.11Lf\n", a / b);
}