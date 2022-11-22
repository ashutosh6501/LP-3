def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("*** RECURSIVE APPROACH ***")
print("Entered Number of Terms:",n)
myLst = []
print("Fibonacci sequence:")
for i in range(n):
    myLst.append(fibonacci(i))
print(myLst)

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print("*** ITERATIVE APPROACH ***")
print("Entered Number of Terms:",n)
myLst = []
myLst.append(a)
myLst.append(b)
# print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    myLst.append(c)
    # print(c,end=" ")
    n=n-1
print("Fibonacci sequence:")
print(myLst)