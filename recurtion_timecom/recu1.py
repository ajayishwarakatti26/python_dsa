##  1 to n nimber print
def printNumber(i,n):

    if i>n:
        return
    print(i,end=' ')
    printNumber(i+1,n)

# printNumber(1,5)

## fact rial number 

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

# print(fact (4))


### fibonaacci serise:
def fib(n:int) -> int:
    if n==1 or n==0:
        return n
    return fib(n-1) + fib(n-2)

print(fib(4
          ))

### two power:
def power(n):
    while n%2==0:
        n=n//2
    return n==1

print(power(60))

