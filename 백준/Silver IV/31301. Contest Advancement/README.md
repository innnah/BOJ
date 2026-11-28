# [Silver IV] Contest Advancement - 31301 

[문제 링크](https://acmicpc.net/problem/31301) 

### 성능 요약

메모리: 137984 KB, 시간: 184 ms

### 분류

구현, 정렬

### 제출 일자

2025년 04월 19일 00:04:54

### 문제 설명

<p>You are the RCD for your regional contest. It just ended and you now need to decide which teams qualify for the next level of competition. The teams are uniquely ranked (there are no ties). The next level has a limit on how many teams from any given school can participate. However, if that limit causes there to be not enough teams advancing, the remaining slots will be filled by teams from schools over the limit. If this happens, you will always give preference to higher-ranking teams, even if it means many teams from the same school advancing.</p>

<p>Output, in rank order, the teams that qualify for the next contest.</p>

### 입력 

 <p>The first line of input contains three integers $n$, $k$ ($1 \leq k < n \leq 10^5$) and $c$ ($ 1 \leq c \leq n$), where $n$ is the number of teams in the competition, $k$ is the number of teams that will advance, and $c$ is the limit on the number of teams that may advance from any given school.</p>

<p>Each of the next $n$ lines contains two integers $t$ and $s$ ($1 \le t,s \le n$). Each line describes a team, with $t$ being the team's unique ID, and $s$ indicating the team's school. All team IDs will be distinct. The teams will be listed in rank order, with the highest ranking teams first.</p>

### 출력 

 <p>Output $k$ lines. On each line output a single integer, which is the ID of a team. List the IDs of the teams that qualified to advance in rank order.</p>

