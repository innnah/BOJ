#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool visited[51];
int length;
int nums[51];
string s;

void backup(int picked = 0, vector<int> nums = {}) {
	if (picked == length) {
		if (*max_element(nums.begin(), nums.end()) == nums.size()) {
			for (auto& i : nums) {
				printf("%d ", i);
			}
			exit(0);
		}
		return;
	}

	string tmp1, tmp2;
	tmp1 = s[picked];
	tmp2 = s.substr(picked, 2);
	if (picked < length && !visited[stoi(tmp1)]) {
		visited[stoi(tmp1)] = true;
		nums.push_back(stoi(tmp1));
		backup(picked + 1, nums);
		nums.pop_back();
		visited[stoi(tmp1)] = false;
	}
	if (picked + 1 < length && stoi(tmp2) <= 50 && !visited[stoi(tmp2)]) {
		visited[stoi(tmp2)] = true;
		nums.push_back(stoi(tmp2));
		backup(picked + 2, nums);
		nums.pop_back();
		visited[stoi(tmp2)] = false;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> s;
	length = s.length();
	backup();
	return 0;
}