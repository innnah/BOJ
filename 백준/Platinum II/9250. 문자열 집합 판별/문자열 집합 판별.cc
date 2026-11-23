#include <bits/stdc++.h>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const int ALPHABETS = 26;
int a, b;
int toNumber(char ch) { return ch - 'a'; }

struct TrieNode {
    TrieNode* children[ALPHABETS];
    int terminal;
    TrieNode* fail;
    vector<int> output;

    TrieNode() : terminal(-1) {
        memset(children, 0, sizeof(children));
    }

    ~TrieNode() {
        for (int i = 0; i < ALPHABETS; i++)
            if (children[i])
                delete children[i];
    }

    void insert(const char* key, int id) {
        if (*key == 0) terminal = id;
        else {
            int next = toNumber(*key);
            if (children[next] == NULL) children[next] = new TrieNode();
            children[next]->insert(key + 1, id);
        }
    }

    TrieNode* find(const char* key) {
        if (*key == 0) return this;
        int next = toNumber(*key);
        if (children[next] == NULL) return NULL;
        return children[next]->find(key + 1);
    }
};
void computeFailFunc(TrieNode* root) {
    queue<TrieNode*> q;
    root->fail = root;
    q.push(root);

    while (!q.empty()) {
        TrieNode* here = q.front();
        q.pop();
        for (int edge = 0; edge < ALPHABETS; ++edge) {
            TrieNode* child = here->children[edge];
            if (!child) continue;
            if (here == root) child->fail = root;
            else {
                TrieNode* t = here->fail;
                while (t != root && t->children[edge] == NULL)
                    t = t->fail;
                if (t->children[edge]) t = t->children[edge];
                child->fail = t;
            }

            child->output = child->fail->output;
            if (child->terminal != -1) child->output.push_back(child->terminal);
            q.push(child);
        }
    }
}
void ahoCorasick(const string& s, TrieNode* root) {
    TrieNode* state = root;
    for (int i = 0; i < s.size(); ++i) {
        int chr = toNumber(s[i]);
        while (state != root && state->children[chr] == NULL) state = state->fail;

        if (state->children[chr]) state = state->children[chr];
        for (int j = 0; j < state->output.size(); ++j) {
            cout << "YES" << endl;
            return;
        }
    }
    cout << "NO" << endl;
}
int main() {
	fastio;
    string h, n;
    cin >> a;
    TrieNode* trie = new TrieNode();
    for (int i = 0; i < a; ++i) {
        cin >> n;
        trie->insert(n.c_str(), i);
    }
    computeFailFunc(trie);
    cin >> b;
    for (int i = 0; i < b; ++i) {
        cin >> h;
        ahoCorasick(h, trie);
    }
	return 0;
}