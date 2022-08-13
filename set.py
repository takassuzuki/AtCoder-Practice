""" 
集合（セット）
"""
# 集合（セット）の宣言・初期化
set_a = {'いちご', 'みかん', 'りんご', 'れもん'}
print(set_a)

# 他の型から集合型に変換する。
print(set('ABCDE'))
print(set([1,3,5,7,9]))

# 集合の要素数を取得する
set_b = set('ABCDE')
print(len(set_b))

# 値の有無を判別する。
set_c = {'チョコ', 'クッキー', 'アイス'}
print('クッキー' in set_c)
print('マカロン' in set_c)


""" 
集合演算
"""
set_d = {'きいろ', 'みどり', 'あか', 'むらさき'}
set_e = {'あお', 'みどり', 'むらさき'}
# 積集合
print(set_d&set_e)
print(set_d.intersection(set_e))
# 和集合
print(set_d|set_e)
print(set_d.union(set_e))
# 差集合
print(set_d-set_e)
print(set_d.difference(set_e))
# 対称差（排他的論理和）集合
# 集合のどちらか一方にある要素の集合
print(set_d^set_e)
print(set_d.symmetric_difference(set_e))
# 部分集合
# どちらかがもう一方の要素を含んでいるかどうか
print(set_e<=set_d)
print(set_e.issubset(set_d))
set_f = {'みどり', 'むらさき', 'あお', 'きいろ'}
set_g = {'あお', 'きいろ'}
print(set_g<=set_f)
print(set_g.issubset(set_f))