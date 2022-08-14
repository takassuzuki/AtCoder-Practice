""" 
Title：ABC002A-正直者
URL：https://atcoder.jp/contests/abc002/tasks/abc002_1
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
10 11
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
li = list(map(int, input().split()))
# 結果出力
print(max(li))
