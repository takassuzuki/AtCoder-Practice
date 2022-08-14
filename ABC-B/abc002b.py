""" 
Title：ABC002B-罠
URL：https://atcoder.jp/contests/abc002/tasks/abc002_2
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
okanemochi
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
W = input()
c = 'aiueo'

# 文字列からaiueoを削除する
for i in range(len(c)):
    W = W.replace(c[i],'')

# 結果出力
print(W)
