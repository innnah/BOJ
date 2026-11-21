#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const int ALPHABETS = 2;
int h1, w1, h2, w2;
string original[2005];
set<string> picture;
map<string, int> m;
vector<int> needle;
string s;
vector<int> arr[2005];
int toNumber(char ch) { return ch == 'o'; }

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
            ret.push_back(make_pair(i, state->output[j]));
        }
    }
    return ret;
}
vector<int> getPi(vector<int>& s) {
    int n = s.size();
    int j = 0;
    vector<int> pi(n + 1, 0);
    for (int i = 1; i < n; i++) {
        while (j > 0 && s[i] != s[j]) j = pi[j];
        if (s[i] == s[j]) pi[i + 1] = ++j;
    }
    return pi;
}
int kmp(vector<int>& h, vector<int>& n, vector<int>& pi) {
    int a = h.size(), b = n.size();
    vector<int> ret;
    int matched = 0;
    for (int i = 0; i < a; ++i) {
        while (matched > 0 && h[i] != n[matched]) matched = pi[matched];
        if (h[i] == n[matched]) {
            ++matched;
            if (matched == b) {
                ret.push_back(i - b + 1);
                matched = pi[matched];
            }
        }
    }
    return ret.size();
}
int main() {
	fastio;
    TrieNode* trie = new TrieNode();
    cin >> h1 >> w1 >> h2 >> w2;
    for (int i = 0; i < w2; ++i) {
        arr[i] = vector<int>(h2, -1);
    }
    for (int i = 0; i < h1; ++i) {
        cin >> s;
        picture.insert(s);
        original[i] = s;
    }
    int cnt = 0;
    for (auto i = picture.begin(); i != picture.end(); ++i) {
        trie->insert((*i).c_str(), cnt);
        m.insert(make_pair(*i, cnt));
        cnt += 1;
    }
    for (int i = 0; i < h1; ++i) {
        needle.push_back(m[original[i]]);
    }
    computeFailFunc(trie);
    for (int i = 0; i < h2; ++i) {
        cin >> s;
        vector<pair<int, int>> ret = ahoCorasick(s, trie);
        for (auto j = ret.begin(); j != ret.end(); ++j) {
            arr[(*j).first][i] = (*j).second;
        }
    }
    int answer = 0;
    vector<int> pi = getPi(needle);
    for (int i = 0; i < w2; ++i) {
        answer += kmp(arr[i], needle, pi);
    }
    cout << answer << endl;
	return 0;
}