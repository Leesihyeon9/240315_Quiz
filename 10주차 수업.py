def ran_lotto():
    results = []

import random

results =[]
while len(results) < 6:
    ran_num = random.randint(1,45)
    if ran_num in results:
        print("results 안에 ran_num이 있으므로, results에 추가하지 않습니다")
    else:
        results.append(ran_num)

print(results)