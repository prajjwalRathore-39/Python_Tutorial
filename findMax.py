a = int(input("Enter the first Number."))
b = int(input("Enter second Number"))

def findMaximum(a,b) : 
  if a>b : 
    print ("a is larger then b")
  elif b>a: 
    print ("b is larger then a")
  else :
    print("Both the Numbers are Equal.")

findMaximum(a,b)


print(max(a,b))