print("借金総額を入力")
shakkin = input()
print("ひと月の返済額を入力")
hitotuki = input()
ichinen = int(hitotuki) * 12
nensuu = int(shakkin) / ichinen
print("かかる年数は"  + str(nensuu) + "年です")
print("1年ごとに返済するボーナスを入力")
bonus = input()
bichinen = int(hitotuki) * 12 + int(bonus) 
bnensuu = int(shakkin) / bichinen
print("かかる年数は"  + str(nensuu - bnensuu) + "年早くなります")
print("返済完了したい年数を入力")
complete = input()
cbonus = (int(shakkin) - (ichinen * int(complete))) / int(complete)
print("その年数に返済する場合、ボーナス時に" + str(cbonus) + "円の返済が必要です")