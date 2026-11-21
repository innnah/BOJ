#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct Line {
	ll a, b;
	double c;
};

double cross(const Line& l, const Line& r) {
	return (r.b - l.b) / (double)(l.a - r.a);
}
pair<int, int> cn[100100], rcn[100100];
ll dp[100100];
int main() {
	fastio;
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		fill(cn, cn + n + 5, make_pair(0, 0));
		for (int i = 0; i < n; ++i) {
			int a, b;
			cin >> a >> b;
			cn[i].first = a - b, cn[i].second = a + b;
		}
		sort(cn, cn + n);
		int idx = 2;
		rcn[1] = cn[0];
		for (int i = 1; i < n; ++i) {
			if (rcn[idx - 1].first == cn[i].first) {
				rcn[idx-1] = cn[i];
			}
			else {
				if (rcn[idx - 1].second < cn[i].second) {
					rcn[idx++] = cn[i];
				}
			}
		}
		n = idx - 1;
		vector<Line> lines(100100);
		int add = 0;
		dp[0] = 0;
		ll x = rcn[1].first;
		lines[add++] = { -2 * x, x * x + dp[0], -2147483648.0 };
		for (int i = 1; i <= n; ++i) {
			ll y = rcn[i].second;
			int fpos = add - 1;
			if (y < lines[add - 1].c) {
				int lo = 0, hi = add - 1;
				while (lo + 1 < hi) {
					int mid = (lo + hi) / 2;
					if (y < lines[mid].c) hi = mid - 1;
					else lo = mid;
				}
				if (y >= lines[hi].c) fpos = hi;
				else fpos = lo;
			}
			dp[i] = lines[fpos].a * y + lines[fpos].b + y * y;
			//cout << fpos << " " << dp[i] << endl;
			if (i != n) {
				x = rcn[i + 1].first;
				Line g = { -2 * x, x * x + dp[i], -2147483648.0 };
				//cout << g.a << " " << g.b << " " << i << endl;
				while (add > 0) {
					g.c = cross(g, lines[add - 1]);
					if (g.c > lines[add - 1].c) break;
					--add;
				}
				lines[add++] = g;
			}
		}
		cout << dp[n] / 4;
		if (dp[n] % 4) {
			cout << "." << dp[n] % 4 * 25 << endl;
		}
		else {
			cout << ".00\n";
		}
	}
	return 0;
}
