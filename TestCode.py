print("Input six integers:")
nums = list(map(float, input().split()))
nums.sort()
print("After sorting:")
print(*nums)

