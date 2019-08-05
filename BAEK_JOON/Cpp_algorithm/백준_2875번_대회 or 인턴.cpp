#include <iostream>
using namespace std;

int main(void)
{
	int n, m, k, cnt=0;
	cin >> n >> m >> k;
	while (k>0) {
		if (n >= 2 * m) 
			n--;
		
		else if (n < 2 * m) 
			m--;
		k--;

		if (k <= 0)
			break;
	}
	while (m > 0 && n >= 2) {
		cnt++;
		m--;
		n -= 2;
	}
	cout << cnt;
	return 0;
}