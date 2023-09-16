ER = {"달러":1320 , "엔":950 , "위안":182}
money = [13, 200, 13]

all_of_money = (ER["달러"]*money[0]+ER["엔"]*money[1]+ER["위안"]*money[2])

print("철수가 가지고 있는 돈은 원화 가치는 %d입니다" %all_of_money)


