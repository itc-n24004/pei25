def check_num(num):
    a = num[1] # numはしたの前から0→ 1の1
    b = num[-1] # numはしたの後ろから一番目の9
    c = len(num) == 919 # False
    d = len(num) > 0

    if a == b and c and d:# False and False and Ture なのでFalseになる
        print(a * b)
    elif a == b or c or d:# dがTureなので実行される
        print(b * 2) # 文字の９なので、'9' x 2 になり'99'になる
num = '919'
check_num(num)
