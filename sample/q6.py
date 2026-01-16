import random #乱数やシャッフルで利用
import sys #sys.exit()で利用

# 英単語と日本語訳をタプルで管理したリスト
words = [('apple', 'りんご'), ('banana', 'バナナ'), 
         ('coconut', 'ココナッツ'), ('doughnut', 'ドーナツ'), 
         ('effort', '努力'), ('future', '未来'), ('gorilla', 'ゴリラ'), 
         ('house', '家'), ('information', '情報'), ('journey', '旅')]

questions = int(input('出題数を入力：'))

length = len(words) #登録されている単語数を取得
if length < questions:
    print('登録された単語数以下の数値を入力してください。')
    sys.exit() #条件を満たされなければ終了

count = 0
correct  = 0 #正解数をカウント

while count < questions:
    random.shuffle(words) #wordsの中身をシャッフル
    ans_index = random.randint(0, 3) #正解の選択肢番号
    #問題分を表示
    print(f'問題{count + 1}:{words[ans_index][0]}の意味は？')
    #選択肢を４つ表示
    for i in range(2):
        print(f'{i * 2 + 1}:{words[i * 2][1]}, {i * 2 + 2}:{words[i * 2 + 1][1]}')
    #解答を入力
    answer = input('1から4の数字で解答（終了する場合は"x"を入力）：')
    if answer == 'x':
        break

    print(f'あなたの解答：{answer}')

    #正解不正解の判定
    if answer == str(ans_index + 1):
        print('正解！')
        correct += 1 #正解数を増やす
    else:
        print(f'不正解！正解は{ans_index + 1}の{words[ans_index][1]}でした！')

    count += 1 #出題数を増やす
    
    #成績表示
    print(f'成績：正解{correct}問 (全{count}問)')

#プログラム終了
