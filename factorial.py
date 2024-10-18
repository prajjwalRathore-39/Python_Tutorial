num = int(input("Enter the Number to find the Factorial."))

def findFactorial(num) :
  fact = 1
  for i in range(num,1,-1) :
    fact*=i

  return fact


print("The factorial of the number is : ", findFactorial(num))
