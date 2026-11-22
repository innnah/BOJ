#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

const int ALPHABETS = 26;
int toNumber(char ch) { return ch - 'a'; }

struct TrieNode {
    TrieNode* children[ALPHABETS];
    ll cnt = 0;
    TrieNode() {
        memset(children, 0, sizeof(children));
    }
    ~TrieNode() {
        for (int i = 0; i < ALPHABETS; ++i) {
            if (children[i]) delete children[i];
        }
    }
};

const int MOD = 1000000007;
int n, m;
string target;
ll dp[200127];
TrieNode* root = new TrieNode();
ll dpf(int idx) {
    if (idx >= m) return 1;
    ll& ret = dp[idx];
    if (ret != -1) return ret;
    ret = 0;
    TrieNode* node = root;
    for (int i = 0; i < 300; ++i) {
        if (idx + i >= m) break;
        int next = toNumber(target[idx + i]);
        if (node->children[next] == NULL) break;
        node = node->children[next];
        ret += node->cnt * dpf(idx + i + 1);
        ret %= MOD;
    }
    return ret;
}
int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
        
        TrieNode* node = root;
        int len = s.length();
        for (int i = 0; i < len; ++i) {
            int next = toNumber(s[i]);
            if (node->children[next] == NULL) node->children[next] = new TrieNode();
            node = node->children[next];
            node->cnt += 1;
        }
	}
    cin >> target;
    m = target.size();
    memset(dp, -1, sizeof(dp));
    cout << dpf(0);
	return 0;
}