num=int(input('あなたの番号を教えてください'))
if num%2==0:
    if num%4==0:
        print('番号は4の倍数です')
    else:
        print('番号は偶数です')
else:
    print('番号は奇数です')