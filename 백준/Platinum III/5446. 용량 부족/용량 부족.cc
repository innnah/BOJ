#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct TrieNode {
    map<char, TrieNode*> children;
    bool terminal;
    TrieNode() : terminal(false) {
        children.clear();
    }
    ~TrieNode() {
        children.clear();
    }
    void insert(const char* key) {
        if (*key == 0) terminal = true;
        else {
            if (children[*key] == NULL) children[*key] = new TrieNode();
            children[*key]->insert(key + 1);
        }
    }
    TrieNode* find(const char* key) {
        if (*key == 0) return this;
        if (children[*key] == NULL) return NULL;
        return children[*key]->find(key + 1);
    }
};
int trie_search(TrieNode* node, TrieNode* nd_node) {
    int ret = node->terminal;
    for (auto& child : node->children) {
        if (nd_node->children.find(child.first) != nd_node->children.end()) {
            ret += trie_search(child.second, nd_node->children[child.first]);
        }
        else ret += 1;
    }
    return ret;
}
int main() {
	fastio;
    int t;
    cin >> t;
    while (t--) {
        TrieNode* will_delete = new TrieNode();
        TrieNode* not_delete = new TrieNode();
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            will_delete->insert(s.c_str());
        }
        int m;
        cin >> m;
        for (int i = 0; i < m; ++i) {
            string s;
            cin >> s;
            not_delete->insert(s.c_str());
        }
        if (m)
            cout << trie_search(will_delete, not_delete) << endl;
        else cout << 1 << endl;
    }
	return 0;
}