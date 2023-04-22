#Write a program to find the largest element in an array.

#SOLUTION : Type 1 using simple mathod 

# Prompt the user to enter the length of the array & its elements.
# Store the values into the related variables.
n = int(input("Enter the lenth of the array :"))
arr=[]
# Use the for loop to enter the elements into the list variable.
i=1
while i<=n:
  a=int(input(f"Enter the elements :{i} :"))
  arr.append(a)
  i+=1
max = arr[0]
for i in range(1,n):
  if arr[i]>max:
    max=arr[i]
  
print(f"Max value is :{max}")


# SOLUTION : Type 2 Using Function

# largest element

def largest_element(arr):
  max = arr[0]
  for i in range (1,n):
    if arr[i]>max:
      max=arr[i]
  return max

n=int(input("Enter the length of the array :"))
arr=[]
for i in range(n):
  a=int(input(f"Enter the value {i+1} :"))
  arr.append(a)

largest_element = largest_element(arr)
print(f"largest element of the list is : {largest_element}")
