#include <stdio.h>

int main(){
	int go, back, peek, one_day, temp, mod, Day;

	scanf("%d %d %d", &go, &back, &peek);

	one_day = go - back;
	temp = peek - go;
	Day = temp / one_day;
	mod = temp % one_day;

	Day = (mod) ? Day + 2 : Day + 1;
	printf("%d\n", Day);

	return 0;
}