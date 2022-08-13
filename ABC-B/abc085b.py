""" 
Title：ABC085B - Kagami Mochi
URL：https://atcoder.jp/contests/abs/tasks/abc085_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
7
50
30
50
100
50
80
30
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
N = int(input())
d = []
for n in range(N):
    d.append(int(input()))

# リストから重複を削除した要素の数を数える。
print(len(list(set(d))))

