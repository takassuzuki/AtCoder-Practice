# 単純なif文
a = 4
if a % 2 == 0:
    print(a, "は偶数です。")
else:
    print(a, "は奇数です。")


# 連続したif文
a = 100
print(a, "は")
if 0 <= a & a <= 9:
    print("1桁の数字です。")
elif 10 <= a & a <= 99:
    print("2桁の数字です。")
elif 100 <= a & a <= 999:
    print("3桁の数字です。")
else:
    print("マイナスの数字、または、4桁以上の数字です。")


# if文のネスト
a = 90
if a > 80:
    if a == 100:
        print("満点です。")
    else:
        print("もう少しです。")
else:
    print("頑張りましょう。")