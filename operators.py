""" 
比較演算子
"""
a=10
b=20
print('a = ', a, ', b = ', b, sep='')
print('a < b:', a<b)
print('a > b:', a>b)
print('a == b:', a==b)
print('a <= b:', a<=b)
print('a >= b:', a>=b)
print('a != b:', a!=b)


""" 
論理演算子
"""
a=30
print('(a >= 10) and (a < 50):', (a >= 10) and (a < 50))
print('(a ==1) or (a == 100):', (a ==1) or (a == 100))
print('not(a == 100):', not(a == 100))
print('a != 100:', a != 100)

# and演算子でつなげた場合、前の条件がFalseだったら、次の条件式演算は行われない。
(a < 100) and (print('aは10未満'))
(a > 100) and (print('aは100以上'))
# or演算子でつなげた場合、前の条件式がTrueだったら、次の条件式演算は行われない。
(a < 100) or (print('aは10以上'))
(a > 100) or (print('aは100未満'))


""" 
三項演算子
"""
# (条件式がTrueの場合) if (条件式) else (条件式がFalseの場合)
point = 90
a = '合格' if point > 80 else '不合格'
print(a)