#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, m, k;
string words[1005];
const int ALPHABETS = 26;
int toNumber(char ch) { return ch - 'A'; }
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
vector<pair<int, int>> ahoCorasick(const string& s, TrieNode* root) {
    vector<pair<int, int>> ret;
    TrieNode* state = root;
    for (int i = 0; i < s.size(); ++i) {
        int chr = toNumber(s[i]);
        while (state != root && state->children[chr] == NULL) state = state->fail;

        if (state->children[chr]) state = state->children[chr];
        for (int j = 0; j < state->output.size(); ++j) {
            ret.push_back(make_pair(i-words[state->output[j]].length()+1, state->output[j]));
        }
    }
    return ret;
}
int main() {
	fastio;
    cin >> n >> m >> k;
    vector<string> puzzle(n);
    for (int i = 0; i < n; ++i) {
        cin >> puzzle[i];
    }
    TrieNode* trie = new TrieNode();
    for (int i = 0; i < k; ++i) {
        string s;
        cin >> s;
        words[i] = s;
        trie->insert(s.c_str(), i);
    }
    computeFailFunc(trie);
    vector<string> turned(n);
    vector<tuple<int, int, char>> found(k, {1500, 1500, 'I'});
    // direction A
    for (int i = 0; i < m; ++i) {
        for (int j = n - 1; j >= 0; --j) {
            turned[i] += puzzle[j][i];
        }
        vector<pair<int, int>> res = ahoCorasick(turned[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { n - p.first - 1, i, 'A' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction C
    for (int i = 0; i < n; ++i) {
        vector<pair<int, int>> res = ahoCorasick(puzzle[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { i, p.first, 'C' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction E
    turned.clear();
    turned.resize(n);
    for (int i = m - 1; i >= 0; --i) {
        for (int j = 0; j < n; ++j) {
            turned[m - i - 1] += puzzle[j][i];
        }
        vector<pair<int, int>> res = ahoCorasick(turned[m - i - 1], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { p.first, i, 'E' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction G
    turned.clear();
    turned.resize(n);
    for (int i = 0; i < n; ++i) {
        for (int j = m - 1; j >= 0; --j) {
            turned[i] += puzzle[i][j];
        }
        vector<pair<int, int>> res = ahoCorasick(turned[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { i, m - p.first - 1, 'G' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction B
    turned.clear();
    turned.resize(n+m-1);
    for (int i = 0; i <= n + m - 2; ++i) {
        int left = min(n - 1, i);
        int right = i - min(m - 1, left);
        for (int j = left; j >= right; --j) {
            turned[i] += puzzle[j][i - j];
        }
        vector<pair<int, int>> res = ahoCorasick(turned[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { left - p.first, i - left + p.first, 'B' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction D
    turned.clear();
    turned.resize(n + m - 1);
    for (int i = 0; i < turned.size(); ++i) {
        int sj = 0, sk = m - i - 1;
        if (sk < 0) {
            sj = -sk;
            sk = 0;
        }
        int j = sj, k = sk;
        while (j < n && k < m) {
            turned[i] += puzzle[j][k];
            ++j; ++k;
        }
        vector<pair<int, int>> res = ahoCorasick(turned[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { sj + p.first, sk + p.first, 'D' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction F
    turned.clear();
    turned.resize(n + m - 1);
    for (int i = 0; i < turned.size(); ++i) {
        int sk = min(m - 1, i), sj = i-sk;
        int j = sj, k = sk;
        while (j < n && k >= 0) {
            turned[i] += puzzle[j][k];
            ++j; --k;
        }
        vector<pair<int, int>> res = ahoCorasick(turned[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { sj + p.first, sk - p.first, 'F' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    // direction H
    turned.clear();
    turned.resize(n + m - 1);
    for (int i = 0; i < turned.size(); ++i) {
        int sj = n-1, sk = i;
        if (sk > m-1) {
            int s = sk - m + 1;
            sj -= s;
            sk -= s;
        }
        int j = sj, k = sk;
        while (j >= 0 && k >= 0) {
            turned[i] += puzzle[j][k];
            --j; --k;
        }
        vector<pair<int, int>> res = ahoCorasick(turned[i], trie);
        for (auto& p : res) {
            tuple<int, int, char> cand = { sj - p.first, sk - p.first, 'H' };
            found[p.second] = min(found[p.second], cand);
        }
    }
    for (int i = 0; i < k; ++i) {
        cout << get<0>(found[i]) << " " << get<1>(found[i]) << " " << get<2>(found[i]) << endl;
    }
	return 0;
}