""" 
Title：ABC264C-Matrix Reducing
URL：https://atcoder.jp/contests/abc264/tasks/abc264_c
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """
from itertools import combinations

# 標準入力から値を取得する。
H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
h,w = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h)]

def check(hidx, widx):
    # print('hidx:',hidx,'widx:',widx)
    # print('range(h):', range(h))
    # print('range(w):',range(w))
    for i in range(h):
        # print('i:',i)
        for j in range(w):
            # print('j:',j)
            # print('hidx[i]:',hidx[i],'widx[j]:',widx[j])
            # print(widx[j])
            if A[hidx[i]][widx[j]] != B[i][j]:
                return False
    return True

# print('range(H):',range(H))
# print('h',h)
# print('combinations(range(H),h):',combinations(range(H),h))

for hidx in combinations(range(H),h):
    # print('hidx:',hidx)
    for widx in combinations(range(W),w):
        # print('widx:',widx)
        if check(hidx, widx):
            print('Yes')
            exit()
print('No')
