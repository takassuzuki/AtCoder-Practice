""" 
Title：ABC001A-視程の通報
URL：https://atcoder.jp/contests/abc001/tasks/abc001_2
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
15000
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
m = int(input())

# mからkmに変換する
km = m/1000
# 通報式の値
vv = 0
if km < 0.1: #0.1km未満の場合
    vv = 0
elif 0.1 <= km and km <= 5: # 0.1km以上5km以下
    vv = km*10
elif 6 <= km and km <= 30: # 6km以上30km以下
    vv = km+50
elif 35 <= km and km <= 70: # 35km以上70km以下
    vv = (km-30)/5+80
else: # 70kmより大きい
    vv = 89
print('{:02d}'.format(int(vv)))
