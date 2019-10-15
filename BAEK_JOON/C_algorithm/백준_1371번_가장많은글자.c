#include <stdio.h>

int main(void) {
	char str[5001];

	int cnt[26] = { 0 }, i, max = 0;

	while (gets(str)) {
		for (i = 0; str[i]; i++) {
			if (str[i] >='a' && str[i] <= 'z') {
				cnt[str[i] - 'a']++;
			}
		}
	}

	for (i = 0; i < 26; i++) {
		if (max < cnt[i]) {
			max = cnt[i];
		}
	}

	for (i = 0; i < 26; i++) {
		if (max == cnt[i]) {
			putchar(i+'a');
		}
	}
	return 0;
}
