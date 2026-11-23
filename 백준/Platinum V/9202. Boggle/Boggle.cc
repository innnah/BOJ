#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 300005;
string board[5], s;
set<string> canFind;
int n, k, scores[9] = { 0, 0, 0, 1, 1, 2, 3, 5, 11 };
int dx[8] = { 0, 0, 1, -1, 1, -1, 1, -1 };
int dy[8] = { 1, -1, 0, 0, 1, -1, -1, 1 };
bool visited[4][4];
const int ALPHABETS = 26;
inline int toNumber(char ch) { return ch - 'A'; }

struct TrieNode {
    TrieNode* children[26];
    bool terminal;
    TrieNode() : terminal(false) {
        memset(children, 0, sizeof(children));
    }
    ~TrieNode() {
        for (int i = 0; i < 26; ++i) {
            if (children[i]) delete children[i];
        }
    }
    void insert(const char* key) {
        if (*key == 0) terminal = true;
        else {
            int next = toNumber(*key);
            if (children[next] == NULL) {
                children[next] = new TrieNode();
            }
            children[next]->insert(key + 1);
        }
    }
    void search(int x, int y, string c) {
        if (this->terminal) {
            canFind.insert(c);
        }
        if (c == "") {
            for (auto a = 0; a < 26; ++a) {
                if (this->children[a] == NULL) continue;
                pair<char, TrieNode*> k = { a + 65, children[a] };
                for (int i = 0; i < 4; ++i) {
                    for (int j = 0; j < 4; ++j) {
                        if (k.first == board[i][j] && !visited[i][j]) {
                            visited[i][j] = 1;
                            k.second->search(j, i, c + k.first);
                            visited[i][j] = 0;
                        }
                    }
                }
            }
        }
        else {
            for (int i = 0; i < 8; ++i) {
                int nx = x + dx[i], ny = y + dy[i];
                if (0 <= nx && nx < 4 && 0 <= ny && ny < 4 && !visited[ny][nx]) {
                    auto ne = children[toNumber(board[ny][nx])];
                    if (ne != NULL) {
                        visited[ny][nx] = 1;
                        ne->search(nx, ny, c + board[ny][nx]);
                        visited[ny][nx] = 0;
                    }
                }
            }
        }
    }
};

int main() {
    fastio;
    TrieNode* trie = new TrieNode();
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> s;
        trie->insert(s.c_str());
    }
    cin >> k;
    while (k--) {
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                visited[i][j] = 0;
            }
        }
        for (int i = 0; i < 4; ++i) {
            cin >> board[i];
        }
        canFind.clear();
        trie->search(-1, -1, "");
        int ret = 0;
        int maxlength = 0;
        for (auto i = canFind.begin(); i != canFind.end(); ++i) {
            ret += scores[i->size()];
            maxlength = max(maxlength, (int)i->size());
        }
        cout << ret << " ";
        vector<string> a;
        for (auto i = canFind.begin(); i != canFind.end(); ++i) {
            if (i->size() == maxlength) a.push_back(*i);
        }
        sort(a.begin(), a.end());
        cout << a[0] << " " << canFind.size() << endl;
    }
    return 0;
}