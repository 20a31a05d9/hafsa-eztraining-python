'''  wrong / incomplete
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
  sum=sum+i
print(sum)  

'''

#sum of digits of a number
#function with arguments with return value 
#sum=0
def sum_of_digits(n):
    sum=0
    while(n!=0):
        rem =n%10
        sum=sum+rem
        n=n//10         #// annadi quotient istadi
    return sum

n=int(input("enter a number:"))
result=sum_of_digits(n)
print(result)
   