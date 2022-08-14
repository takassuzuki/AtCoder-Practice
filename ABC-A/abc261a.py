""" 
Title：ABC261A-Intersection
URL：https://atcoder.jp/contests/abc261/tasks/abc261_a
"""

import io
from posixpath import split
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
0 10 2 5
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
"""

# 標準入力から値を取得する。
l1,r1,l2,r2 = map(int, input().split())
# 結果出力
print(max(0, min(r1,r2)-max(l1,l2)))

""" 
if l1>l2:
    l1,r1,l2,r2 = l2,r2,l1,r1
if r1<=l2:
    print(0)
elif r1<=r2:
    print(r1-l2)
else:
    print(r2-l2)
 """
