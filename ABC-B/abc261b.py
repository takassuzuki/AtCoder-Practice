""" 
Title：ABC261B - Tournament Result
URL：https://atcoder.jp/contests/abc261/tasks/abc261_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
4
-WWW
L-DD
LD-W
LDW-
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
N=int(input())
A=[input() for i in range(N)]

# 2重ループを用いてすべての(i,j)の組み合わせを調べる
for i in range(N):
    for j in range(N):
        if i==j: continue
        if A[i][j]=="W":
            if A[j][i]!="L":
                print("incorrect")
                exit()
        elif A[i][j]=="D":
            if A[j][i]!="D":
                print("incorrect")
                exit()
        elif A[i][j]=="L":
            if A[j][i]!="W":
                print("incorrect")
                exit()
print("correct")

# 標準出力
