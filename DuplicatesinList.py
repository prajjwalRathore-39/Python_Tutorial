list = []
size = int(input("Enter the Size of the List."))
for i in range (size) :
  list.append(int(input()))


Dict = {}
for i in range (len(list)) :
  Dict[i] = list.count(i)

list.clear()
print("Elements Having more than one occurence in the List is : \n")
for ele in Dict.keys() :
  if Dict[ele] > 1 :
    list.append(ele)


print(list)