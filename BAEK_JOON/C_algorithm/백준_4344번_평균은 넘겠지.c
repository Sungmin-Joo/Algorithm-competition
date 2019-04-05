#include <stdio.h>
#include <stdlib.h>
int main() {
	int c, n, s, i, *stu;
	double sum, cnt = 0;
	scanf("%d", &c);
	while (c != 0)
	{
		sum = 0;
		cnt = 0;
		scanf("%d", &n);
		stu = (int *)calloc(n, sizeof(int));
		for (i = 0; i < n; i++)
		{
			scanf("%d", &s);
			stu[i] = s;
			sum += s;
		}
		sum = sum / n;
		for (i = 0; i < n; i++)
		{
			if (stu[i] > sum)
				cnt += 1;
		}
		printf("%.3f%%\n", (100*cnt / n));
		free(stu);
		c--;
	}
	return 0;
}