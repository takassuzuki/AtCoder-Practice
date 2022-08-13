""" 
リスト
"""
# リストの宣言・初期化
from os import remove


list_a=[]
print(list_a)
list_b=list()
print(list_b)
list_c=[1,2,3]
print(list_c)
list_d=['ねこ', 100, 'いぬ', 0.1]
print(list_d)

# リストの要素を参照する
print(list_d[0])
print(list_d[1])
print(list_d[2])
print(list_d[3])

# リストの要素に値を代入する
list_e = [1,2,3]
list_e[0] = 'One'
list_e[1] = 'Two'
list_e[2] = 'Three'
print(list_e)

# リストの要素数を取得する
list_f=['A','B','C','D','E']
length = len(list_f)
print(length)

# 値の有無を判別する
# (リスト内にあるか調べたい値) in (調べたいリスト名)
list_g = ['Ace','Queen','King']
chk = 'Ace' in list_g
print('リストの中にAceが存在するか:', chk)
chk = 'Jack' in list_g
print('リストの中にJackが存在するか:', chk)

# 他の型からリスト型に変換する
str = 'ABCDE'
print(list(str))
taple = ('F','G','H','I','J')
print(list(taple))

# リストの中にリストを入れる
list_h=['A','B','C']
list_i=['D','E','F']
list_j=[list_h,list_i]
print(list_j)

# リストに要素を追加する
# リストの末尾に新しい要素を追加する
list_k=[1,2,3]
list_k.append(4)
list_k.append(5)
print(list_k)
# リストの指定した位置に新しい要素を追加する
list_l=[1,2,3]
list_l.insert(1,4)
list_l.insert(3,5)
print(list_l)

# リストを連結する
# +演算子でリストを結合する
list_m=['red','blue','yellow']
list_n=['white','black']
list_o = list_m + list_n
print(list_m) # list_mとlist_nはそのまま
print(list_n)
print(list_o)
# +=演算子でリストを結合する
list_m += list_n
print(list_n) # list_nはそのまま
print(list_m)
# extend()メソッドでリストを結合する
list_p=[1,2,3]
list_q=[4,5,6]
list_p.extend(list_q)
print(list_q) # list_qはそのまま
print(list_p)

# リストの要素を削除する
# インデックスを指定して要素を削除する
list_r=['tea','coffee','soda','milk','juice']
pop = list_r.pop(2)
print(pop, 'を削除しました。', sep='')
print('削除後のリスト:', list_r)
# 値を指定して要素を削除する
list_s=['tea','coffee','soda','milk','juice','coffee']
list_s.remove('coffee') # 該当の値が2つ以上存在する場合は最初の値を削除する。
print('削除後のリスト:', list_s)
# delによる削除
# delは要素のオブジェクトをそのものをメモリから削除する
list_t=['tea','coffee','soda','milk','juice']
del list_t[3]
print('削除後のリスト:', list_t)

# リストを変数に分割する
list_u=['apple','banana','orange']
x,y,z=list_u
print(x,y,z)

# ソート
# リストを昇順で並び替える
list_v=[48,3,100,49,22,64,0]
list_v.sort()
print(list_v)
# リストを降順で並び替える
list_w=[48,3,100,49,22,64,0]
list_w.sort(reverse=True)
print(list_w)
# 昇順で並び替えて、結果を別のリストとして返す。
list_x=[48,3,100,49,22,64,0]
print(sorted(list_x))
print('元のリストはそのまま残る：',list_x)
# 降順で並び替えて、結果を別のリストとして返す。
list_y=[48,3,100,49,22,64,0]
print(sorted(list_y, reverse=True))
print('元のリストはそのまま残る：',list_y)
