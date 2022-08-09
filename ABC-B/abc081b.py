""" 
Title：ABC081B-Shift only
URL：https://atcoder.jp/contests/abs/tasks/abc081_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
6
382253568 723152896 37802240 379425024 404894720 471526144
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
n = int(input())
m = list(map(int, input().split()))

# 操作回数を格納する変数
cnt = 0

# 操作が行える限り操作を繰り返す
while True:
    # リストの中の値がすべて偶数かどうかを判定するフラグ
    exist_odd = False

    # リストの中の値が偶数であるかどうかをチェックする
    for a in range(n):
        if m[a] % 2 != 0:
            # 奇数だった場合フラグを立てる
            exist_odd = True
    
    # リストの中に奇数が存在する場合はBreak
    if exist_odd:
        break

    # リストの中の値がすべて偶数の場合は2で割る
    for a in range(n):
        m[a] /= 2
    
    # 操作回数をインクリメント
    cnt += 1

# 操作回数を出力する
print(cnt)
