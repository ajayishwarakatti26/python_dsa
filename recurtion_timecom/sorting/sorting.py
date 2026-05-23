#bobble sort:
mylist=[12,23,45,56,67,9,62,1,0]

n=len(mylist)

for i in range(n):
    for j in range(n-i-1):
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1]=mylist[j+1],mylist[j]


print(mylist)


#insertion sort:
numslist=[1,23,4,5,67,8,8,99,9,99,64]

n=len(numslist)

for i in range(1,n):
    key=numslist[i]
    j=i-1
    while j>=0 and numslist[j]>key:
        numslist[j+1]=numslist[j]
        j-=1
        numslist[j+1]=key

print( numslist)

# selection sort:
nums1=[1,23,4,5,67,8,8,99,9,99,64]

n=len(nums1)

for i in range(n):
    mn=nums1[i]
    ind=i
    for j in range(i+1,n):
        if nums1[j]<mn:
            mn=nums1[j]
            ind=j

    tem=nums1[i]
    nums1[i]=nums1[ind]
    nums1[ind]=tem

print(nums1)

# mearg short :
def merge_sort(arr):
    if len(arr) > 1:
        
        # Find middle
        mid = len(arr) // 2

        # Divide array
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call
        merge_sort(left)
        merge_sort(right)

        # Merge process
        i = j = k = 0

        # Compare elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Driver code
arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort(arr)

print("Sorted Array:", arr)

## quick short :
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)

### counting sort:

