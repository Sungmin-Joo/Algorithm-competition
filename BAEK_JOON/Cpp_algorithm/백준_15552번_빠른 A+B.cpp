#include <iostream>
using namespace std;

int main(void)
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int n, a, b;
	cin >> n;
	while (n--)
	{
		cin >> a >> b;
		cout << a + b << '\n';
	}
	return 0;
}