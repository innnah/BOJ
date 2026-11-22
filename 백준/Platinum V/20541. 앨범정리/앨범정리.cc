#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct Album {
	Album* p;
	string an;
	map<string, Album*> sa;
	set<string> sp;
	Album(Album* parent, string name) {
		p = parent;
		an = name;
	}
	void mkalb(string name) {
		if (sa.find(name) != sa.end()) cout << "duplicated album name" << endl;
		else sa[name] = new Album(this, name);
	}
	void rmalb(string name) {
		if (sa.find(name) != sa.end()) {
			pair<int, int> r = sa[name]->rmall();
			sa.erase(name);
			cout << r.first + 1 << " " << r.second << endl;
		}
		else cout << 0 << " " << 0 << endl;
	}
	pair<int, int> rmall() {
		int rma = 0, rmp = sp.size();
		sp.clear();
		for (auto p = sa.begin(); p != sa.end(); ++p) {
			pair<int, int> r = p->second->rmall();
			rma += ++r.first, rmp += r.second;
		}
		sa.clear();
		return { rma, rmp };
	}
	pair<int, int> rmalb(int n) {
		if (n == 0) {
			int rma = 0, rmp = 0;
			for (auto p = sa.begin(); p != sa.end(); ++p) {
				pair<int, int> r = p->second->rmall();
				rma += ++r.first, rmp += r.second;
			}
			sa.clear();
			return { rma, rmp };
		}
		if (n == -1) {
			if (!sa.empty()) {
				pair<int, int> r = sa.begin()->second->rmall();
				sa.erase(sa.begin());
				return { r.first + 1, r.second };
			}
			return { 0, 0 };
		}
		if (n == 1) {
			if (!sa.empty()) {
				pair<int, int> r = (--sa.end())->second->rmall();
				sa.erase(--sa.end());
				return { r.first + 1, r.second };
			}
			return { 0, 0 };
		}
	}
	void insert(string name) {
		if (sp.find(name) != sp.end()) cout << "duplicated photo name" << endl;
		else sp.insert(name);
	}
	void dt(string name) {
		if (sp.find(name) != sp.end()) {
			sp.erase(name);
			cout << 1 << endl;
		}
		else cout << 0 << endl;
	}
	void dt(int n) {
		if (!sp.empty()) {
			if (n) cout << 1 << endl;
			else cout << sp.size() << endl;
			if (n == -1) sp.erase(sp.begin());
			if (n == 1) sp.erase(--sp.end());
			if (n == 0) sp.clear();
		}
		else cout << 0 << endl;
	}
};
int main() {
	fastio;
	Album* top = new Album(NULL, "album");
	Album* cur = top;
	int t; cin >> t;
	while (t--) {
		string c, na;
		cin >> c >> na;
		if (c == "mkalb") {
			cur->mkalb(na);
		}
		else if (c == "insert") {
			cur->insert(na);
		}
		else if (c == "ca") {
			if (na == "..") {
				if (cur->p != NULL) cur = cur->p;
			}
			else if (na == "/") cur = top;
			else {
				if (cur->sa.find(na) != cur->sa.end()) cur = cur->sa[na];
			}
			cout << cur->an << endl;
		}
		else if (c == "delete") {
			if (na == "-1" || na == "0" || na == "1") cur->dt(stoi(na));
			else cur->dt(na);
		}
		else if (c == "rmalb") {
			if (na == "-1" || na == "0" || na == "1") {
				pair<int, int> r = cur->rmalb(stoi(na));
				cout << r.first << " " << r.second << endl;
			}
			else cur->rmalb(na);
		}
	}
	return 0;
}