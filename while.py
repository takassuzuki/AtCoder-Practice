""" 
while文で条件を満たし続ける限り繰り返す
"""
a = 0
while a <= 5:
    print(a)
    a += 1


""" 
while ~ else
whileの繰り返しが終わった後に実行する処理を、elseブロックに記述する。
"""
a = 0
while a <= 5:
    print(a)
    a += 1
else:
    print("書き出しが終わりました。")


""" 
繰り返しを中断する。
"""
a = 0
b = 5
while a < 5:
    if (b - a) <= 2:
        break
    print("a:", a)
    print(b - a)
    a += 1


""" 
繰り返しの次の回に移る
"""
li = [1, 3, 5, '七', 9]
for a in li:
    if type(a) == str:
        print(a, "：数値ではなく文字列です。")
        continue
    print(a)
