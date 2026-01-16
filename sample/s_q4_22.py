name_a = 'ant' #探したい文字の集合
name_b = 'Attention please' #１文字ずつ調べる文字列
strs = '' #見つかった文字を入れる箱

#name_bを１文字ずつ取り出す
for b in name_b:
    if name_a.find(b) >= 0: #bがname_aの中に含まれているか
        strs += b #含まれていれば追加
print(strs)

'''
文字列.find(探したい文字)
.find()は文字がどこにあるか探すメソッド

for b in name_b:は
name_b = 'Attention please'を１文字ずつ取り出しす
取り出した１文字がbになる
'''
