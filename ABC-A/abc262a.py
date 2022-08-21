""" 
Title：ABC262A-World Cup
URL：https://atcoder.jp/contests/abc262/tasks/abc262_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
3000
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
Y = int(input())

a=Y%4
if a==3:
    print(Y+a)
elif a==2:
    print(Y)
elif a==1:
    print(Y+a)
else:
    print(Y+2)

