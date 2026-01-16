commands = ['forward', 'back', 'Back', 'turn_left'] #コマンド一覧

for cmd in commands:
    match cmd:
        case 'forward':
            print('前へ移動')
        case 'back':
            print('後ろへ移動')
        case 'turn_right':
            print('右へ回る')
        case 'turn_left':
            print('左へ回る')
        case x: #上のどれにも当てはまらないとき（簡単に言うとelseと役割はほぼ一緒）
            #xは何でもマッチするから必ず最後に書く
            print(x + 'は存在しないコマンド')
