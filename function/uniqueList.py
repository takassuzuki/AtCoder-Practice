""" 
リストの重複を削除したリストを返す
"""
def uniqueList(li):
    s = set(li)
    return list(s)


print(uniqueList([1,3,5,2,3,1,6,6,7,9]))