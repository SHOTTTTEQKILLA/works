i=0
num=0
min=0
while i <=10:
    num=int(input('入力'))
    if num<0:
        min=1
    i=i+1
if min==1:
    print('入力した数に負の数が含まれています')
else:
    print('入力した数に負の数が含まれていません')
        
