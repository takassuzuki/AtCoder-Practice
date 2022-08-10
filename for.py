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