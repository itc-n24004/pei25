phrase = 'PythonProgramming'
list_p = []

#phraseを1文字ずつ取り出す
for p in phrase:
    #まだlist_pに入っていない文字だけを追加する
    #list_pには重複しない文字のみが保存される
    if p not in list_p:
        list_p.append(p)
#文字列全体の長さ-重複を除いた文字数
#重複している文字の個数になる
print(len(phrase) - len(list_p))

#list_pに入っている文字を横に連続して出力する
for p in list_p:
    print(p, end='')
    #end=''を指定することで、printのたびに改行されず、同じ行に文字が続けて表示される
print() #最後に開業して見た目を整える
