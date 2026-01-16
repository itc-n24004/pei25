row = 3 #行数（段数）
sp = ' ' #空白文字
mark = '*' #表示する記号

for i in range(row): #0, 1, 2まで繰り返す
    lr = sp * (row - i) #3, 2, 1


#i=0のとき 3(row) - 0(i) = 3 空白が3つ(sp = 空白文字)
#これを2まで繰り返す

    center = mark * (i * 2 + 1) #1, 3, 5


#i=0のとき 0(i) * 2 + 1 = 1 *が１つ（mark = *）
#これを２まで繰り返す


    line = lr + center + lr

#lr + center + lrなので
#1行目　空白３つ＋*１つ＋空白３つ
#1行目　空白２つ＋*３つ＋空白２つ
#1行目　空白１つ＋*５つ＋空白１つ

    print(line)
