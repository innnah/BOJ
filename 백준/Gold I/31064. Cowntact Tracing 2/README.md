# [Gold I] Cowntact Tracing 2 - 31064 

[문제 링크](https://acmicpc.net/problem/31064) 

### 성능 요약

메모리: 134264 KB, 시간: 120 ms

### 분류

많은 조건 분기, 그리디, 수학

### 제출 일자

2025년 3월 7일 17:41:55

### 문제 설명

<p>Farmer John has $N$ cows in a line ($1 \leq N \leq 3\cdot 10^5$). Unfortunately, there is a sickness spreading throughout.</p>

<p>Initially, some cows start off infected. Every night, an infected cow spreads the sickness to the cows on their left and right (if they exist). Once a cow is infected, she stays infected.</p>

<p>After some amount of nights, Farmer John realizes that the issue has gotten out of control, so he tests his cows to determine who has the sickness. Find the minimum number of cows that could have started with the sickness.</p>

### 입력 

 <p>The first line contains $N$, the number of cows that Farmer John has.</p>

<p>The next line contains an $N$ character bitstring of only $1$s and $0$s where a $1$ represents an infected cow and a $0$ represents an uninfected cow after some number of nights.</p>

### 출력 

 <p>Output a single integer: the minimum number of cows that could have started with the sickness.</p>

