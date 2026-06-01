# Given an array of integers, reverse the array without using extra space.
# a=[1,2,3,4,5]
# print(a[::-1] ,end="")

# Given a string, reverse it using two pointers.

def rever_star(s):
    s=list(s)
    left=0
    right=len(s)-1

    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right+1

        return "".join(s)
  

print(rever_star("python"))

# Given a string, check whether it is a palindrome or not.
def palindrom(p):
    left=0
    right=len(p)-1

    while left<=right:
        if p[left]==p[right]:
            return "this the palindrom"
        else:
            return "not palindrom"
        
print(palindrom("121"))

# Given an array, move all zeroes to the end while maintaining the order of non-zero elements.
def move_zerolast(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums

print(move_zerolast([1,0,8,0,7,6]))

### mearge arry:
def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(merge_sorted_arrays(arr1, arr2))

#####Given a sorted array and a target value, find two numbers whose sum equals the target.
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None

arr = [1, 2, 3, 4, 6]
target = 6

print(two_sum(arr, target))