#include <iostream>

using namespace std;

int main()
{
	int mod[10] = { 0, }, num, cnt = 0, index = 1, zero = 1;
	for (int i = 0; i < 10; i++)
	{
		int flag = 1;
		cin >> num;
		num %= 42;
		for (int j = 0; j < 10; j++)
		{
			if (mod[j] == num)
			{
				flag = 0;
				if (num == 0 && zero)
				{
					cnt++;
					zero = 0;
				}
				break;
			}
		}
		if (flag)
		{
			cnt++;
			mod[index++] = num;
		}
	}
	cout << cnt;

	
	return 0;
}