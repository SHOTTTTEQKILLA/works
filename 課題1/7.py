print("名前を入力してください")
name = input()
print("2019年現在の年齢を教えてください")
old = input()
intold = int(old)
year = 2019
while intold < 100:
    intold+=1
    year+=1

print(name + "さんが100歳になる年は" + str(year) + "年です")