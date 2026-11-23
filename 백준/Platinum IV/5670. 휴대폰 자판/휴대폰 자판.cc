#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 100005;
int n;
const int ALPHABETS = 26;

struct TrieNode {
    map<char, TrieNode*> children;
    bool terminal, isRoot;
    int cnt;
    TrieNode() : terminal(false), isRoot(false), cnt(0) {}
    ~TrieNode() {
        children.clear();
    }
    void insert(const char* key) {
        if (*key == 0) terminal = true;
        else {
            char next = *key;
            if (children.find(next) == children.end()) {
                children[next] = new TrieNode();
                ++cnt;
            }
            children[next]->insert(key + 1);
        }
    }
    int find(const char* key) {
        if (*key == 0) return 0;
        char next = *key;
        if (children.find(next) == children.end()) return 0;
        int ret = children[next]->find(key + 1);
        if (this->terminal || this->cnt >= 2 || this->isRoot) ++ret;
        return ret;
    }
};

int main() {
    fastio;
    while (1) {
        if (scanf("%d", &n) == EOF) break;
        TrieNode* trie = new TrieNode();
        trie->isRoot = true;
        vector<char[85]> s(n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", s[i]);
            trie->insert(s[i]);
        }
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += trie->find(s[i]);
        }
        printf("%.2lf\n", sum / (double)n);
    }
    return 0;
}