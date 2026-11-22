# [Silver I] It's Mooin' Time II - 33508 

[문제 링크](https://acmicpc.net/problem/33508) 

### 성능 요약

메모리: 244692 KB, 시간: 580 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 집합과 맵

### 제출 일자

2025년 2월 23일 22:18:09

### 문제 설명

<p>Farmer John is trying to describe his favorite USACO contest to Elsie, but she is having trouble understanding why he likes it so much. He says "My favorite part of the contest was when Bessie said 'It's Mooin' Time' and mooed all over the contest."</p>

<p>Elsie still doesn't understand, so Farmer John downloads the contest as a text file and tries to explain what he means. The contest is defined as an array of $N$ ($1\le N\le 10^6$) integers $a_1, a_2, \dots, a_N$ ($1\le a_i\le N$). Farmer John defines a moo as an array of three integers where the second integer equals the third but not the first. A moo is said to occur in the contest if it is possible to remove integers from the array until only the moo remains.</p>

<p>As Bessie allegedly "mooed all over the contest", help Elsie count the number of distinct moos that occur in the contest! Two moos are distinct if they do not consist of the same integers in the same order.</p>

### 입력 

 <p>The first line contains $N$.</p>

<p>The second line contains $N$ space-separated integers $a_1,a_2,\dots,a_N$.</p>

### 출력 

 <p>Output the number of distinct moos that occur in the contest.</p>

<p><strong>Note that the large size of integers involved in this problem may require the use of 64-bit integer data types (e.g., a "long" in Java, a "long long" in C/C++).</strong></p>

