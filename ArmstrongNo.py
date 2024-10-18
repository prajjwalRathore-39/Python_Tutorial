number = int(input("Enter the Number to be checked."))
temp = number
sum = 0
while(number!=0) :
  rem = number %10
  sum += pow(rem,3)
  number//=10


sum = int(sum)

print(sum)
if sum == temp :
  print("Number is a Armstrong Number.")
else :
  print("Number is not an Armstrong Number.")