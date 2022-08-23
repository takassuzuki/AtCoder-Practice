""" 
Title：ABC259A-Growth Record
URL：https://atcoder.jp/contests/abc259/tasks/abc259_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
38 20 17 168 3
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。

# n:高橋君の現在の年齢
# m:身長を求める高橋君の年齢
# x:身長が伸びた最後の年齢
# t:n歳(x歳以降)の時の高橋君に身長
# d:x歳までの毎年の身長の増加数
n,m,x,t,d = map(int, input().split())

if m>x:
    # x歳以降高橋君の身長は伸びないので、m>xの場合はtの値を出力する。
    print(t)
else:
    print(t-(x-m)*d)


