#include <stdio.h>
int self_num(int num) {
	int sum = num;
	while (num != 0) {
		sum += num % 10;
		num /= 10;
	}
	return sum;
}

int main() {
	int i = 1, tmp;
	char arr[10001] = { 0, };
	for (; i < 10001; i++) {
		tmp = self_num(i);
		if (tmp < 10001)
			arr[tmp] = 1;
	}

	for (i = 1; i < 10001; i++) {
		if (!arr[i])
			printf("%d\n", i);
	}

	return 0;
}