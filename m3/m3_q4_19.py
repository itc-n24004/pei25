list_a = []
for x in range(1, 10):
    if x % 2 == 1:
        continue # 奇数の時次の繰り返しへ（だから奇数は飛ばされて次に行く）
    list_a.append(x) # appendはリストに新しい要素を追加する命令
print(list_a)
