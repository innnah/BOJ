#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

struct TrieNode {
	TrieNode* children[2];
	int cnt;
	TrieNode() : cnt(0) {
		memset(children, 0, sizeof(children));
	}
	~TrieNode() {
		for (int i = 0; i < 2; ++i) {
			if (children[i]) delete children[i];
		}
	}
	void insert(int key, int d) {
		if (d == 0) return;
		else {
			int next = (key >> (d-1)) % 2;
			if (children[next] == NULL) children[next] = new TrieNode();
			children[next]->cnt++;
			children[next]->insert(key, d - 1);
		}
	}
	void del(int key, int d) {
		if (d == 0) return;
		else {
			int next = (key >> (d-1)) % 2;
			children[next]->cnt--;
			children[next]->del(key, d - 1);
		}
	}
	int query(int key, int d) {
		if (d == 0) return 0;
		bool next = (key >> (d-1)) % 2;
		if (children[!next] == NULL || children[!next]->cnt == 0) return children[next]->query(key, d - 1);
		return children[!next]->query(key, d - 1) + (1 << (d - 1));
	}
};

int n;
int main() {
	fastio;
	TrieNode* trie = new TrieNode();
    trie->insert(0, 31);
	cin >> n;
	while (n--) {
		int q, x;
		cin >> q >> x;
		if (q == 1) {
			trie->insert(x, 31);
		}
		else if (q == 2) {
			trie->del(x, 31);
		}
		else {
			cout << trie->query(x, 31) << endl;
		}
	}
	return 0;
}