num = int(input("Insert the Number that you want to check whether it is prime or not."))

counter = 0
for i in range(2, num-1, 1):
  if num%i==0 : 
    counter = counter+1

if counter>0 :
  print("The Number is not a prime number.")
else :
  print("The number is a prime number.")