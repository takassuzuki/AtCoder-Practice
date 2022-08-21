""" 
Title：ABC263A-Full House
URL：https://atcoder.jp/contests/abc263/tasks/abc263_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
12 12 11 1 2
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
li = list(map(int, input().split()))
# リストを昇順で並び替える
li.sort()

# フルハウスなのは以下の2通り
# 1枚目から3枚目までのカードの数字が同じ かつ 4枚目と5枚目のカードの数字が同じ
# 1枚目と2枚目のカードの数字が同じ かつ 3枚目から5枚目までのカードの数字が同じ
if (li[0] == li[1] == li[2] and li[3] == li[4]) or (li[0] == li[1] and li[2] == li[3] == li[4]):
    print('Yes')
else:
    print('No')

