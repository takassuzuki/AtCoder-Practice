""" 
Title：ABC260A-A Unique Letter
URL：https://atcoder.jp/contests/abc260/tasks/abc260_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
pop
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
S=list(input())
# 文字列の中で使われている文字のリストを作成する
P=list(set(S))

for p in P:
    if S.count(p) == 1:
        print(p)
        exit()
print(-1)
