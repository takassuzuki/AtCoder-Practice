""" 
Title：ABC261C - NewFolder(1)
URL：https://atcoder.jp/contests/abc261/tasks/abc261_c
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
11
a
a
a
a
a
a
a
a
a
a
a
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
N = int(input())
S = [input() for _ in range(N)]

cnt = dict()
for s in S:
    if s not in cnt:
        print(s)
        cnt.setdefault(s,1)
    else:
        print('{}({})'.format(s,cnt[s]))
        cnt[s] += 1
