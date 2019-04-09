#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	
	int temp, cnt = 0;
	while(n--)
	{
		cin >> temp;
		if (temp == 1)
			continue;
		else
		{
			for (int i = temp / 2; i > 0; i--)
			{
				if (temp % i == 0)
				{
					if (i == 1)
						cnt++;
					else
						break;
				}
		
			}
		}
	}
	cout << cnt << endl;
	return 0;
}