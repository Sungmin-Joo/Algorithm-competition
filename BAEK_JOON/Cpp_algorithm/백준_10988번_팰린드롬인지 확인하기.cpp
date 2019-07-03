#include <iostream>
#include <string>
using namespace std;

int main()
{
	string str;
	cin >> str;

	int l = str.length(), i;
	char front[50];
	for (int i = 0; i < l / 2; i++)
		front[i] = str[i];

	int top = l / 2 - 1;
	int flag = 1;

	if (l % 2 == 0)
		i = (l / 2);
	else
		i = (l / 2) + 1;

	for (i; i < l; i++)
	{
		if (str[i] == front[top--])
			continue;
		else
		{
			flag = 0;
			break;
		}
	}

	cout << flag;
	return 0;
}