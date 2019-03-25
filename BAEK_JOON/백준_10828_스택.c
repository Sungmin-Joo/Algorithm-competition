#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
int main(){
	int s_count = 0, data, n, i, *stack;
	char *ptr, input[12] = { 0 };
	scanf("%d", &n);
	while (getchar() != '\n');
	stack = (int*)calloc(n, sizeof(int));
	for (i = 0; i < n; i++){
		scanf("%[^\n]", input);
		ptr = strtok(input," ");
		while (getchar() != '\n');	
		if (!strcmp(ptr, "push")){
			ptr = strtok(NULL, " ");
			stack[s_count++] = atoi(ptr);
		}
		else if (!strcmp(ptr, "pop")){
			if (s_count == 0){
				printf("%d\n", -1);
			}
			else{
				printf("%d\n", stack[--s_count]);
				stack[s_count] = NULL;
			}
		}
		else if (!strcmp(ptr, "top")){
			if (s_count == 0) {
				printf("%d\n", -1);
			}
			else {
				printf("%d\n", stack[s_count-1]);
			}
		}
		else if (!strcmp(ptr, "size")) {
			printf("%d\n", s_count);
		}
		else if (!strcmp(ptr, "empty")) {
			if (s_count) { printf("%d\n", 0); }else{ printf("%d\n", 1); }
		}
	}
	free(stack);
	return 0;
}