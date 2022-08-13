""" 
Title：ABC087B - Coins
URL：https://atcoder.jp/contests/abs/tasks/abc087_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
30
40
50
6000
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
A=int(input())
B=int(input())
C=int(input())
X=int(input())

# for文をネストしてすべてのパターンの合計金額を調べる
count = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            total = 500*a + 100*b + 50*c
            # 合計金額がXと一致したらカウントする
            if total == X:
                count += 1

# 条件を満たすパターンの数を出力する
print(count)


