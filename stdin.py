# 標準入力のサンプル

import io
import sys

_INPUT = """\
Test
10
0.5
apple banana orange
1 2 3
0.1 0.01 0.001
aomori akita yamagata
10 100 1000
0.5 1.5 2.5
aaa
apple banana orange
apmori akita yamagata
japan china america
1 2 3
4 5 6
7 8 9
0.1 0.2 0.3
0.4 0.5 0.6
0.7 0.8 0.9
"""
sys.stdin = io.StringIO(_INPUT)

""" 
1行1列の入力を受け取る
 """
# 文字列を受け取る場合
S = input()

# 整数を受け取る場合
N = int(input())

# 少数を受け取る場合
F = float(input())

print("文字列：{}".format(S))
print("整数：{}".format(N))
print("少数：{}".format(F))


""" 
1行複数列の入力を受け取る
 """

# 文字列を受け取る場合
A,B,C = input().split()

# 整数を受け取る場合
X,Y,Z = map(int, input().split())

# 少数を受け取る場合
H,M,S = map(float, input().split())

print("文字列：{}, {}, {}".format(A,B,C))
print("整数：{}, {}, {}".format(X, Y, Z))
print("少数：{}, {}, {}".format(H, M, S))


""" 
1行の配列を受け取る場合
 """

# 文字列を受け取る場合
# print(list(input().split()))
print(input().split())

# 整数を受け取る場合
print(list(map(int, input().split())))

# 少数を受け取る場合
print(list(map(float, input().split())))

# 文字列を文字に分解する場合
print(list(input()))


""" 
複数行複数列の入力を受け取る
 """

# 複数行の文字列を受け取る場合
# A = list(input().split() for _ in range(3))
A = [input().split() for _ in range(3)]
print(A)

# 複数行の整数列を受け取る場合
B = list(list(map(int, input().split())) for _ in range(3)) 
# B = [list(map(int, input().split())) for _ in range(3)]
print(B)

# 複数行の少数列を受け取る場合
# C = list(list(map(float, input().split())) for _ in range(3))
C = [list(map(float, input().split())) for _ in range(3)]
print(C)

