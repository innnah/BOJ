#pragma GCC optimize("O3")
#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;

namespace fio {
    const int BSIZE = 524288;
    char bin[BSIZE+1], bout[BSIZE], tmp[8];
    int p = BSIZE, q = 0;
    inline char readChar() {
        if(p == BSIZE) {
            //syscall(0, 0, bin, BSIZE);
            bin[fread(bin, 1, BSIZE, stdin)] = '\n';
            p = 0;
        }
        return bin[p++];
    }
    int readInt() {
        char c = readChar();
        while (c < '-') {
            c = readChar();
        }
        int ret = 0; bool neg = c == '-';
        if (neg) c = readChar();
        while (c>='0') {
            ret = ret * 10 + c - '0';
            c = readChar();
        }
        return neg ? -ret : ret;
    }
    void flush() {
      syscall(1, 1, bout, q);
      q = 0;
    }
    void put(char x) {
      if(q == BSIZE) flush();
      bout[q++] = x;
    }
    void print(int x) {
      if(!x) {
        put('0');
      } else {
        int i=8;
        if(x<0) {
          x = -x;
          put('-');
        }
        while(x) {
          tmp[--i] = '0' + x%10;
          x /= 10;
        }
        while(i<8) put(tmp[i++]);
      }
      put('\n');
    }
}

int s[2000001];

int main() {
  int n = fio::readInt();
  for(int i=0;i<n;i++)
    s[fio::readInt() + 1000000]++;
  for(int i=0;i<=2000000;i++) {
    while(s[i]--)
      fio::print(i-1000000);
  }
  fio::flush();
}
