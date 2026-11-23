#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

char preorder[1000], inorder[1000];
string s1, s2;
int n;

int postorder(int s = 0, int e = n, int pos = 0) {
	for (int i = s; i < e; i++) {
		if (preorder[pos] == inorder[i]) {
			postorder(s, i, pos + 1);
			postorder(i + 1, e, pos + i - s + 1);
			cout << inorder[i];
		}
	}
	return 0;
}

void input() {
	cin >> s1 >> s2;
	n = s1.length();
	for (int i = 0; i < n; i++) {
		preorder[i] = s1[i];
	}
	for (int i = 0; i < n; i++) {
		inorder[i] = s2[i];
	}
}

int main() {
	fastio;
	while (1) {
		input();
		if (cin.eof()) break;
		postorder();
		cout << endl;
	}
}