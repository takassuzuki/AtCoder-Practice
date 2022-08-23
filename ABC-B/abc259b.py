""" 
Title：ABC259B-Counterclockwise Rotation
URL：https://atcoder.jp/contests/abc259/tasks/abc259_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
2 2 180
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

from math import sin, cos, radians

# a:座標x
# b:座標y
# d:半回転させる角度
a, b, d = map(int, input().split())
d = radians(d)
print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))

