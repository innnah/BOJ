/*
import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def scc(v):
    global vertexCounter, sccCounter
    discovered[v] = vertexCounter
    vertexCounter += 1
    ret = discovered[v]
    stack.append(v)
    for i in graph[v]:
        if discovered[i] == -1:
            ret = min(ret, scc(i))
        elif sccId[i] == -1:
            ret = min(ret, discovered[i])
    if ret == discovered[v]:
        while 1:
            t = stack.pop()
            sccId[t] = sccCounter
            if t == v: break
        sccCounter += 1
    return ret
def tarjanSCC():
    global sccCounter, vertexCounter
    for i in range(1, n+1):
        if discovered[i] == -1: scc(i)
    ids = [[] for _ in range(n)]
    for i in range(1, n+1):
        ids[sccId[i]].append(i)
    return ids
while 1:
    a = input().rstrip()
    if a == '0': break
    n, m = map(int, a.split())
    discovered = [-1 for _ in range(n+1)]
    sccCounter, vertexCounter = 0, 0
    stack = []
    sccId = [-1 for _ in range(n+1)]
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        graph[edges[i*2]].append(edges[i*2+1])
    sccs = tarjanSCC()
    outdegree = [0 for _ in range(len(sccs))]
    for i in range(1, n+1):
        for j in graph[i]:
            if sccId[i] != sccId[j]:
                outdegree[sccId[i]] += 1
    ret = []
    for i in range(len(sccs)):
        if not outdegree[i]:
            for j in sccs[i]:
                ret.append(j)
    print(*sorted(ret))
*/
#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
int n, m, discovered[5005], sccId[5005], sccCounter, FGcounter;
vector<int> graph[5005], ids[5005];
stack<int> s;
int scc(int v) {
    discovered[v] = FGcounter++;
    int ret = discovered[v];
    s.push(v);
    for (auto& i : graph[v]) {
        if (discovered[i] == -1) ret = min(ret, scc(i));
        else if (sccId[i] == -1) ret = min(ret, discovered[i]);
    }
    if (ret == discovered[v]) {
        while (1) {
            int t = s.top();
            s.pop();
            sccId[t] = sccCounter;
            if (t == v) break;
        }
        ++sccCounter;
    }
    return ret;
}
void tarjanSCC() {
    for (int i = 1; i <= n; ++i) {
        if (discovered[i] == -1) scc(i);
    }
    for (int i = 1; i <= n; ++i) {
        ids[sccId[i]].push_back(i);
    }
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    while (1) {
        memset(discovered, -1, sizeof(discovered));
        memset(sccId, -1, sizeof(sccId));
        for (int i = 0; i <= 5000; ++i) {
            graph[i].clear();
            ids[i].clear();
        }
        while(!s.empty()) s.pop();
        sccCounter = FGcounter = 0;
        cin >> n;
        if (n == 0) return 0;
        cin >> m;
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
        }
        tarjanSCC();
        vector<int> outdegree(n+1, 0);
        for (int i = 1; i <= n; ++i) {
            for (auto& j : graph[i]) {
                if (sccId[i] != sccId[j]) outdegree[sccId[i]] += 1;
            }
        }
        vector<int> ret;
        for (int i = 0; i < outdegree.size(); ++i) {
            if (!outdegree[i]) {
                for (auto& j : ids[i]) ret.push_back(j);
            }
        }
        sort(ret.begin(), ret.end());
        for (auto& i : ret) cout << i << " ";
        cout << endl;
    }
}