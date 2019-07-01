#include <iostream>
#include <string>
using namespace std;

int main()
{
	short n, a, b;
	string str;
	cin >> n;
	while (n--)
	{
		cin >> str;
		a = str[0] - 0x30;
		b = str[2] - 0x30;
		cout << a + b << endl;
	}
	return 0;
}