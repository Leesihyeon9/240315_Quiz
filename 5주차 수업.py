x = input("점수를 입력하세요:")

if int(x) >70:
    print("A")
elif int(x) <=70 and int(x) >40:
    print("B")
elif int(x) <=40 and int(x) >10:
    print("C")
else:
    print("D")