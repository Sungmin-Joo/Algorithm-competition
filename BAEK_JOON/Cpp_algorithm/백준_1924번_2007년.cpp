#include <cstdio>
const char *list[7] = {"MON","TUE","WED","THU","FRI","SAT","SUN"};
int main(void)
{
	int x, y;
	scanf("%d %d", &x, &y);

	int sum = 0;
	for (int i = 1; i <= x; i++) {
		switch (i) {
		case 2:
		case 4:
		case 6:
		case 8:
		case 9:
		case 11:
			sum += 31;
			break;
		case 5:
		case 7:
		case 10:
		case 12:
			sum += 30;
			break;
		case 3:
			sum += 28;
			break;
		default:
			break;
		}
	}
	printf("%s", list[(sum-1 + y) % 7]);

	return 0;
}