""" 
Title：ABC088B - Card Game for Two
URL：https://atcoder.jp/contests/abs/tasks/abc088_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
4
20 18 2 18
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
N = int(input())
cards = list(map(int, input().split()))

# Aliceの合計点数
alice = 0
# Bobの合計点数
bob = 0
# 繰り返し回数
cnt = 0

# カードのリストを降順に並び替える
cards.sort(reverse=True)

# リストからカードを1つずつ取り出す
for card in cards:
    if cnt%2 == 0:
        # Aliceの点数を加算する
        alice += card
    else:
        # Bobの点数を加算する
        bob += card
    # 繰り返し回数を加算する
    cnt += 1

# 得点差を出力する
print(alice - bob)