#include <stdio.h>

int main(void) {
	long long n;
	scanf("%lld", &n);
	switch (n % 8) {
	case 1:
		putchar(0x31);
		break;
	case 2:
	case 0:
		putchar(0x32);
		break;
	case 3:
	case 7:
		putchar(0x33);
		break;
	case 4:
	case 6:
		putchar(0x34);
		break;
	case 5:
		putchar(0x35);
		break;
	}

	return 0;
}