
import math

n, k = input().split()
n, k = int(n), int(k)
most = k // 2

questions = []
for _ in range(n):
    questions.append(input().split()[1:])

curr, check, res = [], {}, [0]
def helper(i):
    if len(curr) == k:
        res[0] += 1
        return
    for j in range(i, len(questions)):
        question = questions[j]
        flag = False
        for topic in question:
            if topic in check and check[topic] + 1 > most:
                flag = True
                break
        if flag:
            continue
        for topic in question:
            if topic in check:
                check[topic] += 1
            else:
                check[topic] = 1
        curr.append(j)
        helper(j + 1)
        for topic in question:
            check[topic] -= 1
            if not check[topic]:
                check.pop(topic)
        curr.pop()

helper(0)

print(res[0])