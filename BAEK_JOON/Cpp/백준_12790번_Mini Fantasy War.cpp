#include <iostream>
using namespace std;

struct Char {
	int HP;
	int MP;
	int AD;
	int DF;
};


int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		Char a;
		cin >> a.HP >> a.MP >> a.AD >> a.DF;
		int tp1;
		cin >> tp1;
		(a.HP + tp1 < 1) ? a.HP = 1 : a.HP += tp1;
		cin >> tp1;
		(a.MP + tp1 < 1) ? a.MP = 1 : a.MP += tp1;
		cin >> tp1;
		(a.AD + tp1 < 0) ? a.AD = 0 : a.AD += tp1;
		cin >> tp1;
		a.DF += tp1;
		cout << a.HP + 5 * a.MP + 2 *a.AD + 2 * a.DF << endl;
	}
	return 0;
}