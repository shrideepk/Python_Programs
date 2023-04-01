# Suppose a user gives a number 103 and wants the output 301 for that we can use this program.
''' First take the input a number and store in a variable
    perform loop operation preferred while loop 
    get the unit place of number by using mod function
    store the value in a new string
    do the same till the time loop gets end.
'''
n=int(input("Enter your number :"))
rev=0
i=1
while i <=n:
  j=n%10
  rev=rev*10+j
  n=n//10
print(rev)
