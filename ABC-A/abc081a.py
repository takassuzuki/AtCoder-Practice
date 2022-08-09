""" 
Title：ABC081A-Placing Marbles
URL：https://atcoder.jp/contests/abs/tasks/abc081_a
"""

import io
import sys

# 問題のINPUTをここに入力する
_INPUT = """\
101
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する
a = list(input())

# 標準出力
print(int(a[0]) + int(a[1]) + int(a[2]))
