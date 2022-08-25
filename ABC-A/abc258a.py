""" 
Title：ABC258A-When?
URL：https://atcoder.jp/contests/abc258/tasks/abc258_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
k = int(input())

h = 21 + k//60
m = k-60 if k>=60 else k
print('{:02d}:{:02d}'.format(h,m))

