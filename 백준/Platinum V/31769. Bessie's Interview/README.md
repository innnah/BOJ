# [Platinum V] Bessie's Interview - 31769 

[문제 링크](https://acmicpc.net/problem/31769) 

### 성능 요약

메모리: 202192 KB, 시간: 984 ms

### 분류

자료 구조, 그래프, 우선순위 큐

### 제출 일자

2025년 4월 30일 21:45:41

### 문제 설명

<p>Bessie is looking for a new job! Fortunately, $K$ farmers are currently hiring and conducting interviews. Since jobs are highly competitive, the farmers have decided to number and interview cows in the order they applied. There are $N$ cows that applied before Bessie, so her number is $N+1$ ($1 \leq K \leq N \leq 3 \cdot 10^5$).</p>

<p>The interview process will go as follows. At time $0$, farmer $i$ will start interviewing cow $i$ for each $1 \leq i \leq K$. Once a farmer finishes an interview, he will immediately begin interviewing the next cow in line. If multiple farmers finish at the same time, the next cow may choose to be interviewed by any of the available farmers, according to her preference.</p>

<p>For each $1\le i\le N$, Bessie already knows that cow $i$'s interview will take exactly $t_i$ minutes ($1 \leq t_i \leq 10^9$). However, she doesn't know each cow's preference of farmers.</p>

<p>Since this job is very important to Bessie, she wants to carefully prepare for her interview. To do this, she needs to know when she will be interviewed and which farmers could potentially interview her. Help her find this information!</p>

### 입력 

 The first line of the input will contain two integers $N$ and $K$.

<p>The second line will contain $N$ integers $t_1 \dots t_N$.

					</p>

### 출력 

 <p>On the first line, print the time Bessie's interview will begin.</p>

<p>On the second line, a bit string of length $K$, where the $i$-th bit is $1$ if farmer $i$ could interview Bessie and $0$ otherwise.</p>

