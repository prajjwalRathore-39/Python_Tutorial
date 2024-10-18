#  A = P(1 + R/100)^t 


principal = int(input("Enter the principal."))
rate = int(input("Enter the rate."))
time = int(input("Enter the time."))

amount = principal * pow((1 + (rate/100)),time)

print("The compound interest is : ", amount - principal)