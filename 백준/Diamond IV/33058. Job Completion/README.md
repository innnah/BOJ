# [Diamond IV] Job Completion - 33058 

[문제 링크](https://acmicpc.net/problem/33058) 

### 성능 요약

메모리: 184464 KB, 시간: 1220 ms

### 분류

자료 구조, 그리디, 우선순위 큐, 정렬

### 제출 일자

2026년 1월 29일 19:15:59

### 문제 설명

<p>Bessie the cow has $N$ ($1\le N\le 2\cdot 10^5$) jobs for you to potentially
complete. The $i$-th one, if you choose to complete it, must be started at or
before time $s_i$  and takes $t_i$ time to complete
($0\le s_i\le 10^{18}, 1\le t_i\le 10^{18}$).

</p><p>What is the maximum number of jobs you can complete? Time starts at $0$, and
once you start a job you must work on it until it is complete, without starting
any other jobs in the meantime.


				</p>

### 입력 

 <p>The first line contains $T$, the number of independent test cases ($1\le T\le 10$). Each test case is formatted as follows.</p>

<p>The first line contains $N$.</p>

<p>Each of the next $N$ lines contains two integers $s_i$ and $t_i$. Row $i+1$ has the details for the $i$th job.</p>

<p>It is guaranteed that the sum of $N$ over all test cases does not exceed $3\cdot 10^5$.</p>

### 출력 

 <p>For each test case, the maximum number of jobs you can complete, on a new line.</p>

