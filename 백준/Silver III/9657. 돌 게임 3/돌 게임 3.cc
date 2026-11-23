#include <bits/stdc++.h>
using namespace std;
int dp[1002];
int main(){
    int n;
    scanf("%d",&n);
    dp[1] = 1;dp[2] = 0;dp[3] = 1;dp[4] = 1;
    for(int i=5;i<=n;i++)dp[i]=!dp[i-1]||!dp[i-3]||!dp[i-4];
    if(dp[n])printf("SK");
    else printf("CY");
}