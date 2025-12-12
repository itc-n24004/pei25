day = ['月','月','火','水','木','金','金']
j = 0
for i in ['月', '火', '水', '木', '金']:
    while day.count(i) > 1:
        day.remove(i) #iと同じ要素をリストから1つ削除

day.insert(len(day), '土')#リストの最後(len(day)に土を挿入
j = len(day)
day.insert(j, '日')#リストの最後(len(day)に日を挿入
        
print(day)

