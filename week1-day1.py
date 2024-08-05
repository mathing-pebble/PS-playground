from collections import deque

heights = list(map(int, input().split())) 

sum = sum(heights)
done = False

for i in range(9):
    for j in range(i + 1, 9):
        if sum - heights[i] - heights[j] == 100:
            result = [heights[k] for k in range(9) if k != i and k != j]
            done = True
            break
        if done:
            break

result.sort()
for h in result:
    print(h)
