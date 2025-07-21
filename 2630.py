import sys

input = sys.stdin.readline

N = int(input())
square = [map(int, input().strip().split()) for _ in range(N)]

print(N)
print(square)