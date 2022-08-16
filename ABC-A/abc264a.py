""" 
Title：ABC264A-"atcoder".substr()
URL：https://atcoder.jp/contests/abc264/tasks/abc264_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
1 7
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
L,R = map(int, input().split())
# 文字列atcoderのLからR文字目を切り取り出力する。
print('atcoder'[L-1:R])

