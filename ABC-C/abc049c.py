""" 
Title：ABC049C - 白昼夢
URL：https://atcoder.jp/contests/abs/tasks/arc065_a
"""

import io
import sys

# 問題のINPUTをここに入力する。
_INPUT = """\
erasedream
"""
sys.stdin = io.StringIO(_INPUT)

""" 
回答はここから
 """

# 標準入力から値を取得する。
s = input()

while len(s) > 0:
    for query in ('erase', 'eraser', 'dream', 'dreamer'):
        # print('s:', s, 'query', query)
        # print('endwith:', s.endswith(query))
        # sがqueryで終わるかチェックする
        if s.endswith(query):
            # sを末尾からqueryの文字数分だけ削除する
            s = s[:-len(query)]
            # print('s:',s)
            break
    else: # breakされなかったとき、つまり合致する文字列がなかった場合
        print('NO')
        exit()
print('YES')
