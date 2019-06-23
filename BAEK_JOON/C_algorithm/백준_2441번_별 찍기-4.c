#include <stdio.h>

int main(void) {
	int i,j,n;
	scanf("%d",&n);
	i = n;
	while (i--){
		j = n - (i + 1);
		while (j--)
			putchar(' ');
		j = i + 1;
		while (j--)
			putchar('*');
		putchar('\n');
	}
	return 0;
}