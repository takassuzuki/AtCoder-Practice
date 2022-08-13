""" 
Title：ABC086C - Traveling
URL：https://atcoder.jp/contests/abs/tasks/arc089_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
2
3 1 2
6 1 1
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
"""
# 条件
# x+yとtの偶奇が同じであること
# x+yがtより大きいこと

# 標準入力から値を取得する。
n = int(input())

plans = []
for _ in range(n):
    plans.append(map(int, input().split()))

st = 0
sx = 0
sy = 0
for t,x,y in plans:
    # print(t,x,y)
    # 前回移動時との差分
    # abs:絶対値を求める関数
    dt = t-st
    dx = abs(x-sx)
    dy = abs(y-sy)
    # print(dt,dx,dy)
    if t%2 != (x+y)%2 or dx+dy > dt:
        print('No')
        exit()
    st = t
    sx = x
    sy = y
print('Yes')

