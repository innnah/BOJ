#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

string sa, sb;
vector<int> a, b, c;
int n;
string selectbig(const string num, vector<int> s) {
	int idx = num.length();
	if (idx == n) return num;
	int digit = idx;
	for (int i = 9; i >= 0; --i) {
		for (int j = 0; j < s[i]; ++j) {
			if (i > a[digit]) goto A;
			else if (i < a[digit]) return "";
			++digit;
		}
	}
A:
	for (int i = a[idx]; i <= 9; ++i) {
		if (s[i]) {
			--s[i];
			if (i == a[idx]) {
				string sub = selectbig(num + to_string(i), s);
				if (sub != "") return sub;
				++s[i];
			}
			else {
				string ret = num + to_string(i);
				for (int j = 0; j <= 9; ++j)
					while (s[j]--)
						ret += to_string(j);
				return ret;
			}
		}
	}
	return "";
}
string selectsmall(const string num, vector<int> s) {
	int idx = num.length();
	if (idx == n) return num;
	int digit = idx;
	if (idx == 0) {
		for (int i = 1; i <= 9; ++i) {
			if (s[i]) {
				if (i < a[digit]) goto B;
				else if (i > a[digit]) return "";
				else break;
			}
		}
		++digit;
	}
	for (int i = 0; i <= 9; ++i) {
		for (int j = 0; j < s[i]; ++j) {
			if (i < a[digit]) goto B;
			else if (i > a[digit]) return "";
			++digit;
		}
	}
	return "";
B:
	for (int i = a[idx]; i >= (idx ? 0 : 1); --i) {
		if (s[i]) {
			--s[i];
			if (i == a[idx]) {
				string sub = selectsmall(num + to_string(i), s);
				if (sub != "") return sub;
				++s[i];
			}
			else {
				string ret = num + to_string(i);
				for (int j = 9; j >= 0; --j)
					while (s[j]--)
						ret += to_string(j);
				return ret;
			}
		}
	}
	return "";
}
int main() {
	fastio;
	cin >> sa >> sb;
	n = sa.length();
	b = vector<int>(10, 0);
	c = vector<int>(10, 0);
	for (int i = 0; i < n; ++i) {
		a.push_back(sa[i] - 48);
		++b[sb[i] - 48];
		++c[sb[i] - 48];
	}
	string r1 = selectbig("", b);
	if (r1 == "") cout << 0 << endl;
	else cout << r1 << endl;

	string r2 = selectsmall("", c);
	if (r2 == "") cout << 0 << endl;
	else cout << r2 << endl;
	return 0;
}