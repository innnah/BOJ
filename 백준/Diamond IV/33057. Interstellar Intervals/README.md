# [Diamond IV] Interstellar Intervals - 33057 

[문제 링크](https://acmicpc.net/problem/33057) 

### 성능 요약

메모리: 132152 KB, 시간: 236 ms

### 분류

다이나믹 프로그래밍, 두 포인터

### 제출 일자

2026년 1월 22일 23:53:28

### 문제 설명

<p>It's the year $3000$, and Bessie became the first cow in space! During her journey between the stars, she found a number line with $N$ ($2 \leq N \leq 5 \cdot 10^5$) points, numbered from $1$ to $N$. All points are initially colored white. She can perform the following operation any number of times.</p>

<ul>
	<li>Choose a position $i$ within the number line and a positive integer $x$. Then, color all the points in the interval $[i, i + x - 1]$ red and all points in $[i + x, i + 2x - 1]$ blue. All chosen intervals must be <strong>disjoint</strong> (i.e. no points in $[i, i + 2x - 1]$ can be already colored red or blue). The entire interval must also fall within the number line (i.e. $1 \leq i \leq i + 2x - 1 \leq N$).</li>
</ul>

<p>Farmer John gives Bessie a string $s$ of length $N$ consisting of characters $R$, $B$, and $X$. The string represents Farmer John's color preferences for each point: $s_i=R$ means the $i$'th point must be colored red, $s_i = B$ means the $i$'th point must be colored blue, and $s_i = X$ means there is <strong>no constraint</strong> on the color for the $i$'th point.</p>

<p>Help Bessie count the number of distinct ways for the number line to be colored while satisfying Farmer John's preferences. Two colorings are different if there is at least one corresponding point with a different color. Because the answer may be large, output it modulo $10^9+7$.</p>

### 입력 

 <p>The first line contains an integer $N$.</p>

<p>The following line contains string $s$.</p>

### 출력 

 <p>Output the number of distinct ways for the number line to be colored while satisfying Farmer John's preferences modulo $10^9+7$.</p>

