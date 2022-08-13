""" 
Title：ABC085C - Otoshidama
URL：https://atcoder.jp/contests/abs/tasks/abc085_c
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
1000 1234000
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
"""

# 標準入力から値を取得する。
N,Y = map(int, input().split())

res10000 = -1 #返却する10000円札の枚数
res5000 = -1 #返却する5000円札の枚数
res1000 = -1 #返却する1000円札の枚数

# 10000円札の枚数を0~Nで調べる
for a in range(0, N+1, 1):
    # 5000円札の枚数を0~N-aで調べる
    for b in range(0, N-a+1, 1):
        # 1000円札の枚数はN-a-bで決まる
        c = N-a-b
        # 合計金額を計算する
        total = 10000*a + 5000*b + 1000*c
        # 答えが決まったら返却用変数に代入する
        if total == Y:
            res10000 = a
            res5000 = b
            res1000 = c

# 結果を返却する
print(res10000, res5000, res1000)
