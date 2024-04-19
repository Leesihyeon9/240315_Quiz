number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

results = []

for row in number:
    for a in row:
        if a%2 == 0:
            results.append(a)
print("짝수를 입력하겠습니다")
print(results)
