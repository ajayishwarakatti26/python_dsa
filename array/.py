from functools import reduce

nums = [1,2,3,4,5,6]
even = filter(lambda x: x%2==0, nums)
result = list(map(lambda x: x*x, even))
print(result)

# ///////
n1 = [10, 40, 20, 50]

result = reduce(lambda x,y: x if x > y else y, n1)

print(result)

# resuresion:

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

print(sum_n(2))