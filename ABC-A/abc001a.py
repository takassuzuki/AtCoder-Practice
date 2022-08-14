""" 
Title：ABC001A-積雪深差
URL：https://atcoder.jp/contests/abc001/tasks/abc001_1
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
15
10
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
h1 = int(input())
h2 = int(input())

# 結果出力
print(h1-h2)
