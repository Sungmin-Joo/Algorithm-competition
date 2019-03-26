#include <stdio.h>  

int main()
{
	int sum=0,min=99,i=0,temp[7];
	for (i = 0; i < 7; i++) {
		scanf("%d", &temp[i]);
	}
	for (i = 0; i <7; i++){
		if (temp[i] % 2){
			sum += temp[i];
			if (min > temp[i]){
				min = temp[i];
			}
		}
	}
	if(sum == 0){
		printf("%d\n", -1);
	}
	else{
		printf("%d\n%d\n", sum, min);
	}
	return 0;
}