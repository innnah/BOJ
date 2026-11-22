# [Platinum II] Milk Buckets - 35321 

[문제 링크](https://acmicpc.net/problem/35321) 

### 성능 요약

메모리: 215252 KB, 시간: 888 ms

### 분류

자료 구조, 그리디, 세그먼트 트리

### 제출 일자

2026년 3월 10일 23:50:22

### 문제 설명

<p>Bessie has challenged Farmer John to a game involving milk buckets! There are $N$ $(2 \leq N \leq 2 \cdot 10^5)$ milk buckets lined up in a row. The $i$-th bucket from the left initially contains $a_i$ $(0 \leq a_i \leq 10^9)$ gallons of milk.</p>

<p>The game consists of two phases:</p>

<p>Phase 1: Farmer John may swap any two adjacent buckets. He may perform as many swaps as he likes, but each swap costs 1 coin.</p>

<p>Phase 2: After swapping, Farmer John performs the following operation until only one bucket is left: Choose two adjacent buckets with milk amounts $a_i$ and $a_{i+1}$, and replace both buckets with one bucket containing $\frac{a_i+a_{i+1}}2$ gallons of milk in their place.</p>

<p>Your goal is to determine the minimum number of coins Farmer John must spend in the swapping phase to maximize the amount of milk in the final bucket after all merges are complete.</p>

### 입력 

 <p>The first line contains one integer $T$ $(1 \leq T \leq 100)$: the number of independent test cases.</p>

<p>Then, for each test case, the first line contains an integer $N$: the number of milk buckets. The second line contains $N$ integers $a_1, a_2, \dots, a_N$, separated by spaces: the number of gallons of milk in each bucket.</p>

<p>It is guaranteed that the sum of $N$ over all test cases does not exceed $5 \cdot 10^5.$</p>

### 출력 

 <p>For each test case, output the minimum number of coins Farmer John must spend to maximize the amount of milk in the final bucket.</p>

