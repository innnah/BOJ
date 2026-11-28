# [Platinum III] Deforestation - 33060 

[문제 링크](https://acmicpc.net/problem/33060) 

### 성능 요약

메모리: 215088 KB, 시간: 2196 ms

### 분류

자료 구조, 그리디, 우선순위 큐, 세그먼트 트리, 집합과 맵, 정렬, 값 및 좌표 압축

### 제출 일자

2025년 02월 21일 08:40:30

### 문제 설명

<p>Farmer John is expanding his farm! He has identified the perfect location in the Red-Black Forest, which consists of $N$ trees ($1 \le N \le 10^5$) on a number line, with the $i$-th tree at position $x_i$ ($-10^9 \le x_i \le 10^9$).</p>

<p>Environmental protection laws restrict which trees Farmer John can cut down to make space for his farm. There are $K$ restrictions ($1 \leq K \leq 10^5$) specifying that there must always be at least $t_i$ trees ($1 \leq t_i \leq N$) in the line segment $[l_i, r_i]$, including the endpoints ($-10^9 \le l_i \leq r_i \le 10^9$). It is guaranteed that the Red-Black Forest initially satisfies these restrictions.</p>

<p>Farmer John wants to make his farm as big as possible. Please help him compute the maximum number of trees he can cut down while still satisfying all the restrictions!</p>

### 입력 

 <p>Each input consists of $T$ ($1 \le T \le 10$) independent test cases. It is guaranteed that the sums of all $N$ and of all $K$ within an input each do not exceed $3 \cdot 10^5$.</p>

<p>The first line of input contains $T$. Each test case is then formatted as follows:</p>

<ul>
	<li>The first line contains integers $N$ and $K$.</li>
	<li>The next line contains the $N$ integers $x_1, \dots, x_N$.</li>
	<li>Each of the next $K$ lines contains three space-separated integers: $l_i$, $r_i$ and $t_i$.</li>
</ul>

### 출력 

 <p>For each test case, output a single line with an integer denoting the maximum number of trees Farmer John can cut down.</p>

