#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>

typedef struct  stackNode {
	char data;
	struct stackNode *link;
} stackNode, stackNode2;

stackNode* top;

int isEmpty() {
	if (top == NULL) return 1;
	else return 0;
}

void push(char item) {
	stackNode* temp = (stackNode *)malloc(sizeof(stackNode));
	temp->data = item;
	temp->link = top;
	top = temp;
}

char pop() {
	char item;
	stackNode* temp = top;

	if (top == NULL) {
		printf("\n\n Stack is empty !\n");
		return 0;
	}
	else {
		item = temp->data;
		top = temp->link;
		free(temp);
		return item; 
	}
}

int main(void) {
	char d;
	int i;
	char str[500] = { 0, };
	
	top = NULL;
	while (1) {
		scanf("%[^\n]", str);
		if (!strcmp(str, "END"))
			break;
		else {
			for (i = 0; i <  strlen(str) ; i++) {
				push(str[i]);
			}
			while (!isEmpty())
				putchar(pop());
			putchar('\n');
		}
		while (getchar() != '\n');
	}
	return 0;
}