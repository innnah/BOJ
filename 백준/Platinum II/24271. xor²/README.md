# [Platinum II] xor² - 24271 

[문제 링크](https://acmicpc.net/problem/24271) 

### 성능 요약

메모리: 4856 KB, 시간: 228 ms

### 분류

비트마스킹, 자료 구조, 세그먼트 트리

### 제출 일자

2024년 8월 30일 23:43:09

### 문제 설명

<p>음이 아닌 정수만으로 이루어진 길이가 $N$인 수열 $A_0$, $A_1$, $\cdots$, $A_{N-1}$이 주어진다. 이 때, 다음 쿼리를 수행하는 프로그램을 작성하시오.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>1 l r x</code></span>: $l \le \left( i \oplus x \right) \le r$과 $0 \le i < N$을 모두 만족하는 모든 정수 $i$에 대해, $A_i$의 값들을 전부 bitwise XOR하여 출력한다. 단, 해당하는 $i$가 없을 경우 $0$을 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>2 i x</code></span>: $A_i$를 $A_i \oplus x$로 설정한다.</li>
</ul>

<p>$\oplus$는 bitwise XOR 연산자이다. 인덱스가 $0$부터 시작함에 유의하라.</p>

### 입력 

 <p>첫 번째 줄에 수열의 길이 $N$이 주어진다.</p>

<p>두 번째 줄에 $N$ 개의 정수 $A_0$, $A_1$, $\cdots$, $A_{N-1}$이 공백으로 구분되어 주어진다.</p>

<p>세 번째 줄에 쿼리의 수 $Q$가 주어진다.</p>

<p>다음 $Q$ 개의 줄의 각 줄에 쿼리가 주어진다. 각 쿼리는 <span style="color:#e74c3c;"><code>1 l r x</code></span> 또는 <span style="color:#e74c3c;"><code>2 i x</code></span> 중 한 가지 형식이다.</p>

### 출력 

 <p>$1$번 쿼리가 주어질 때마다 각 줄에 답을 출력한다.</p>

