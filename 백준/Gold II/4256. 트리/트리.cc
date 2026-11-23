#include <iostream>
#include <vector>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

int preorder[1000], inorder[1000];
int n;

int postorder(int s = 0, int e = n, int pos = 0) {
	for (int i = s; i < e; i++) {
		if (preorder[pos] == inorder[i]) {
			postorder(s, i, pos + 1);
			postorder(i + 1, e, pos + i - s + 1);
			cout << inorder[i] << ' ';
		}
	}
	return 0;
}

void input() {
	for (int i = 0; i < n; i++) {
		cin >> preorder[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> inorder[i];
	}
}

int main() {
	fastio;
	int t;
	cin >> t;
	while (t--) {
		cin >> n;
		input();
		postorder();
		cout << '\n';
	}
}