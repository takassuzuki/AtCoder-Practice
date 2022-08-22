""" 
Title：ABC260B-Better Students Are Needed!
URL：https://atcoder.jp/contests/abc260/tasks/abc260_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
6 1 0 2
80 60 80 60 70 70
40 20 50 90 90 80
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。

# N:受験者数
# X:数学の点数による合格者数
# Y:英語の点数による合格者数
# Z:数学＋英語の点数による合格者数
n,x,y,z = map(int, input().split())
# idx = [i+1 for i in range(N)]
# # 受験者の数学の点数
# a = list(map(int, input().split()))
# A = dict(zip(idx, a))
# # 受験者の英語の点数
# b = list(map(int, input().split()))
# B = dict(zip(idx, b))
# # 合格者
# P = list()

# for x in range(X):
#     print(x)

# 受験者の数学の点数
a = map(int, input().split())
# 受験者の英語の点数
b = map(int, input().split())

s = list(zip(range(1,n+1),a,b))

# 全体を(-A,i)の昇順にソート
s.sort(key=lambda p: (-p[1],p[0]))
# print(s)
# for aa in s:
#     print(aa)
#     print((-aa[2], aa[0]))
# X+1番目以降を(-B,i)の昇順にソート
s[x:] = sorted(s[x:], key= lambda p:(-p[2],p[0]))
# X+Y+1番目以降を(-(A+B),i)の昇順にソート
s[x+y:] = sorted(s[x+y:], key=lambda p: (-(p[1]+p[2]),p[0]))
# X+Y+Z番目以前をiの昇順にソート
s[:x+y+z] = sorted(s[:x+y+z], key=lambda p: p[0])

print(s[x:])
print(s[x+y:])
print(s[:x+y+z])

for p in s[:x+y+z]:
    print(p[0])
# print(s)



# 標準出力
