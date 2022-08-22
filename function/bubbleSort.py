""" 
バブルソート
"""
def bubble_sort(data):
    # バブルソート：前から2つずつデータを比較し並べ替える
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            print('i:',i,'j:',j)
            if data[j] > data[j+1]: # 左の方が大きい場合
                data[j], data[j+1] = data[j+1], data[j] # 前後を入れ替え

    return data

def bubble_sort2(data):
    # バブルソート：前から2つずつデータを比較し並べ替える。ただし、交換がない場合は省略する
    change = True # 交換の余地ありと家庭
    for i in range(len(data)):
        print('1.change:',change)
        if not change: # 交換の余地なしで繰り返しを脱出
            break
        change = False # 交換の余地なしと家庭
        for j in range(len(data)-i-1):
            print('i:',i,'j:',j)
            if data[j] > data[j+1]: # 左の方が大きい場合
                data[j], data[j+1] = data[j+1], data[j] # 前後を入れ替え
                change = True # 交換の余地ありと仮定
            print('2.change:',change)

    return data

DATA = [6,15,4,2,8,5,11,9,7,13]
#DATA = [6,15,4,2,8]
sorted_data = bubble_sort2(DATA.copy())
print(f'{DATA} → {sorted_data}')