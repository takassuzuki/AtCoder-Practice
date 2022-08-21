""" 
Title：ABC263B-Ancestor
URL：https://atcoder.jp/contests/abc263/tasks/abc263_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
3
1 2
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
N = int(input())
P = [0,0] + list(map(int, input().split()))

crr = N #今注目している人
cnt = 0 #今注目している人が人Nの何代前か
while crr != 1:
    # 1代遡る
    cnt+=1
    crr=P[crr]
print(cnt)
