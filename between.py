def countdiv(a,b,c):

    count=0
    for i in range(a,b+1):
        if i%c==0:
            count+=1
        return count

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
result=countdiv(a,b,c)
print(f"Number of numbers between {a} and {b} divisible by {c}: {result}")