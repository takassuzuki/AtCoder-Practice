""" 
itertoolsのサンプル
イテレーションに関する関数が多く用意されている
"""

import itertools

# 順列
tmp = ['a','b','c']
# tmpの中から2つの要素を取り出し並べる
print(list(itertools.permutations(tmp,2)))


# 組み合わせ（重複なし）
# tmpの中から2つの要素を取り出すときの組み合わせを調べる
print(list(itertools.combinations(tmp,2)))


# 組み合わせ（重複あり）
# tmpの中から1つの要素を取り出す。
# そのあと、取り出した要素をtmpに戻し、再度tmpの中から要素を1つ取り出す。
print(list(itertools.combinations_with_replacement(tmp,2)))


# 無限イテレータ
# startからstep飛ばしの整数を無限に返す
itr = itertools.count(5,3)
for i in itr:
    print(i, end=' ')
    if i>25:
        break

# 引数に与えられたイテレータの要素を無限に返す
itr = itertools.cycle(tmp)
for i,x in enumerate(itr):
    print(x, end=' ')
    if i>10:
        break

# objectを指定回数返す
itr = itertools.repeat('Hello',3)
for i in itr:
    print(i, end=' ')