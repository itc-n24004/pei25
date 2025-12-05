colors = '赤:青:黄'
parts = colors.split(':') # 指定した文字で分割する
number = len(colors)
print(parts[1] + number * parts[2])
'''
numberは、赤、:、青、:、黄が全部で５なので５になる
なので、青＋５×黄になる
'''
