#リストを作成
animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
#文字列が'D'で始まっているか調べる→ その結果をfrom_Dに代入
    is_long = len(animal) > 5
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find('b')
#文字列の中で'b'が最初に現れる位置（インデックス）を返す
#'Rabbit'は'b'は3文字目だから2
#'House'は'b'がないから-1
#これはその動物の中で、'b'がどこにあるか調べてなかったら-1になる。
#-1はインデックスではありえない数字（0から始まるから）にしてわかりやすく区別しているから自動で-1になる。
    else:
        total += len(animal)
    print(f"totalの値は{total}")
print(total)
