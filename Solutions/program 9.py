a=int(input("enter any number:"))
sum=0
for i in range(0,n):
    sum=sum+a%10
    a=a//10
print("sum of it is:",sum)

