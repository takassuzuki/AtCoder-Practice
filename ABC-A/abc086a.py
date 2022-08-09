""" 
Title：ABC086A-Product
URL：https://atcoder.jp/contests/abs/tasks/abc086_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
1 21
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
a, b = map(int, input().split())

# 積を計算し、2で割ったときの余りで出力内容を条件分岐する。
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
