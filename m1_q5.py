list_a = []
for i in range(4):
#iの値は0から始まる
    list_a.append(2 * i)
print(list_a) #25

list_b = [21, 22, 23, 24]
list_c = []
for i in range(4):
    list_c.append(list_b[i] // (3 * (i + 1)))
print(list_c) #26

list_d = [2, 4, 1, 6, 9, 3, 5, 7]
d = 2
while d < 12:
    list_d.pop(11 % d)
    d += 2
print(list_d) #27

"""
d   11%d    list_d
2   1       [2, 1, 6, 9, 3, 5, 7]
4   3       [2, 1, 6, 3, 5, 7]
6   5       [2, 1, 6, 3, 5]
8   3       [2, 1, 6, 5]
10  1       [2, 6, 5]
よってlist_dは[2, 6, 5]となる

"""

list_e = [1, 2, 2, 7]
j = 0
for cd in [7, 3, 2, 6, 5]:#[7, 3, 2, 6, 4]から順に1つずつ取り出しcdに代入
    if cd in list_e:#list_eにcdが含まれていればTrue
        list_e.remove(cd)#cdと等しい最初の要素をlist_eから削除(1つだけ)
        list_e.insert(j, 2 * cd)#indexjの位置に2倍した値を挿入（以降の要素は後ろにずれる）
        j += 1
print(list_e) #28

"""
ループごとの変化
cd  j   list_e
7   0   [14, 1, 2, 2]
3   0   [14, 1, 2, 2]※ 条件（if）に満たさないのでリストに変化なし
2   0   [14, 4, 1, 2]
6   0   [14, 4, 1, 2]※ 条件（if）に満たさないのでリストに変化なし
5   0   [14, 4, 1, 2]※ 条件（if）に満たさないのでリストに変化なし
"""

result = ''
for e in [20, 6, -2, 12]:
    if (e + 4) ** 2 < 30:#(e+4)の２乗という意味
        result += 'A'
    elif 4 < e / 3:
        result += 'B'
    else:
        result += 'C'
print(result)

"""
1回目：B
2回目：BC
3回目：BCA
4回目：BCAC
"""
