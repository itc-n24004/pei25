a = 2
list_a = []
for i in range(6):
    list_a.append(a)#aの値をリストの最後に追加する
    a = a * 2 #aを２倍にして次のループで使う値にする
print(list_a)
