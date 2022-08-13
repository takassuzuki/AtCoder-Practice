""" 
辞書
"""
# 辞書の宣言・初期化
dictionary_a = {'りんご':1, 'いちご':5, 'みかん':10}
print(dictionary_a)
dictionary_b ={('チョコ',200):20, ('マカロン',500):15, ('クッキー',300):30}
print(dictionary_b)

# 辞書の要素を参照する
print(dictionary_a['りんご'])
print(dictionary_a['いちご'])
print(dictionary_a['みかん'])
print(dictionary_a.get('りんご'))
print(dictionary_a.get('いちご'))
print(dictionary_a.get('みかん'))
print(dictionary_a.get('れもん')) # キーが存在しない場合はNoneを返す

# 辞書のキーの存在をチェックする
print('いちご' in dictionary_a)
print('れもん' in dictionary_a)

# 要素の値の代入
dictionary_c = {'チョコ':1, 'マカロン':2, 'クッキー':3}
print(dictionary_c)
dictionary_c['チョコ'] = 'One'
dictionary_c['マカロン'] = 'Two'
dictionary_c['クッキー'] = 'Three'
print(dictionary_c)

# dict()で辞書を作る
# キーワード引数を指定して作る
dictionary_d = dict(チョコ = 20, マカロン = 15, クッキー = 30)
print(dictionary_d)
# zip()でキーのリストと値のリストを合体させて作る
key = ['チョコ','マカロン','クッキー']
value = [20,15,10]
dictionary_e = dict(zip(key,value))
print(dictionary_e)
# タプルのリストから作る
dictionary_f = dict([('チョコ',20), ('マカロン',15), ('クッキー', 30)])
print(dictionary_f)

# 辞書の要素を追加する
dictionary_g = {'チョコ':20, 'マカロン':15, 'クッキー':30}
dictionary_g['キャンディー'] = 50
print(dictionary_g)
dictionary_h = {'チョコ':20, 'マカロン':15, 'クッキー':30}
dictionary_h.setdefault('キャンディー', 50)
print(dictionary_h)

# 辞書の要素を削除する
# キーを指定して要素を削除する
dictionary_i = {'チョコ':20, 'マカロン':15, 'クッキー':30}
pop = dictionary_i.pop('マカロン')
print('削除された要素：', pop)
print(dictionary_i)

dictionary_j = {'チョコ':20, 'マカロン':15, 'クッキー':30}
del dictionary_j['チョコ']
print(dictionary_j)

# すべての要素を削除する
dictionary_k = {'チョコ':20, 'マカロン':15, 'クッキー':30}
dictionary_k.clear()
print(dictionary_k)

# 辞書のキーのリストを作成する
dictionary_l = {'Apple':30, 'Banana':40, 'Orange':20}
print(dictionary_l.keys())
print(list(dictionary_l.keys()))

# 辞書の値のリストを作成する
print(dictionary_l.values())
print(list(dictionary_l.values()))

# 辞書の要素のリストを作成する
print(dictionary_l.items())
print(list(dictionary_l.items()))