while True:
    num=int(input('入力してください：'))
    if num%7==0:
        print('7の倍数です')
    else:
        print('7の倍数ではありません')
    if num%3==0:
        print('3の倍数です')
    else:
        print('3の倍数ではありません')
    if num<0:
        print('負の数です')
    else:
        print('負の数ではありません')