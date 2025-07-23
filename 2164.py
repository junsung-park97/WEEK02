import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque([int(i) for i in range(1, n + 1)])

while len(queue) > 1:
   
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)

print(queue.popleft())
        