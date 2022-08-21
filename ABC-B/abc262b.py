""" 
Title：ABC262B-Triangle(Easier)
URL：https://atcoder.jp/contests/abc262/tasks/abc262_b
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
5 6
1 5
4 5
2 3
1 4
3 5
2 5
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
n,m=map(int, input().split())
adj=[[False]*n for _ in range(n)]

# print(n,m)
# print(adj)

for _ in range(m):
    u,v = map(int,input().split())
    # print(u,v)
    u -= 1
    v -= 1
    # print(u,v)
    adj[u][v] = True
    adj[v][u] = True
# print(adj)

ans=0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # print(i,j,k,adj[i][j],adj[j][k],adj[k][i])
            if adj[i][j] and adj[j][k] and adj[k][i]:
                ans += 1

print(ans)
