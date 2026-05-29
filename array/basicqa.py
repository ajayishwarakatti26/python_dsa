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


