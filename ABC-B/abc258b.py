""" 
Title：ABC268B-Number Box
URL：https://atcoder.jp/contests/abc258/tasks/abc258_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
4
1161
1119
7111
1811
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

d = [
    (1,1), # 右斜め下
    (1,0), # 右
    (1,-1), # 右斜め上
    (0,1), # 下
    (0,-1), # 上
    (-1,1), # 左斜め下
    (-1,0), # 左
    (-1,-1) # 左斜め上
]

# print(d[0][0], d[0][1],d[1][0],d[1][1])
# 標準入力から値を取得する。
n=int(input())
a=[list(map(int, input())) for _ in range(n)]
# ロジック記述

ans=0

# スタート位置を全探索する
for i in range(n):
    for j in range(n):
        # print(i,j)
        # print(a[i][j])
        # スタート位置から決まった方向にN-1回移動する
        for k in d:
            # print(k[0], k[1])
            now=0
            x=i
            y=j
            # 決まった方向にN-1回移動する
            for l in range(n):
                # print(x,y)
                now*=10
                now+=a[x][y]

                x+=k[0]
                y+=k[1]

                x%=n
                x+=n

                y%=n
                y+=n

                x%=n
                y%=n
            
            ans=max(ans, now)
print(ans)
