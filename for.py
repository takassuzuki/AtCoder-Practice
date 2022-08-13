""" 
for文を使ってリストの値を取り出す。
"""
w = ['月','火','水','木','金','土','日',]
for wday in w:
    print(wday)


""" 
for文を使って辞書の内容を取り出す。
"""
we = {
    '金':'Fri',
    '土':'Sat',
    '日':'Sun'
}
# 辞書をそのまま記述すると、キーのみを取得する。
for keys in we:
    print(keys)
# value()メソッドを使って辞書の値のみを取得する。
for value in we.values():
    print(value)
# items()メソッドを使って辞書のキーと値のペアをタプルで取得する。
for item in we.items():
    print(item)


""" 
rangeを使った繰り返し 
"""
for a in range(7):
    print(a)
# range(開始値, 終端値, ステップ)
for a in range(20, 31, 2):
    print(a)


""" 
rangeを使ったlistの作成
"""
li = list(range(10, 35, 3))
print(li)


""" 
リストの内包表記
"""
a = [1,2,3,4,5]
a_db = [x*2 for x in a]
print(a_db)


""" 
条件式を含むリストの内包表記
"""
a = [1,5,10,15,20]
a_chk = [x*2 for x in a if x >= 10]
print(a_chk)


""" 
辞書の内包表記
"""
from random import randint
keys = ['いちご', 9, 'みかん', 25, 'りんご']
d = {x:randint(1,100) for x in keys if type(x) == str}
print(d)


""" 
集合の内包表記
"""
a = {1,4,5,-1,9,-2,10,9,15,4,-5}
setA = {x for x in a if (0 < x <= 10)}
print(setA)


