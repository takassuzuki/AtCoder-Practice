""" 
各桁の合計値を計算する
"""
def digitSum(n):
    # 数値を文字列に変換する
    s = str(n)
    # 1文字ずつ数値化し配列にする
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

print(digitSum(123))
print(digitSum(123456789))