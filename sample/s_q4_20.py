a = 0 #合計を入れる変数
counter = 0 #繰り返し回数をカウント
while counter < 6: #counterが6未満の間繰り返す
    a += counter #aにcounterの値を足す
    counter += 1 #counterを1増やす
    #aが4より大きくなったら
    if a > 4:
        break #whileを途中終了

print(a, counter)
