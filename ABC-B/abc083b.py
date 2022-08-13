""" 
Title：ABC083B - Some Sums
URL：https://atcoder.jp/contests/abs/tasks/abc083_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
100 4 16
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
N,A,B = map(int, input().split())

# 1からNまで1ずつ増やしながら繰り返し実行する。
total = 0
for n in range(1,N+1,1):
    # 数値を文字列に変換する
    s = str(n)
    # 1文字ずつ数値化し配列にする
    array = list(map(int, s))
    # 各桁の和を算出する
    digit_sum = sum(array)
    # 各桁の和がA以上B以下の場合、totalに加算する。
    if (A <= digit_sum) and (digit_sum <= B):
        total += n

# 合計値を出力する
print(total)

