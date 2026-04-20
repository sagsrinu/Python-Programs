
#create list of bytes type array
#create a list of byte numbers
elements =[10,20,30,40]
#convert the list into bytes type array
x=bytearray(elements)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
## print through loop
print("-----------------------------")
## Modifying the array list
x[0] = 80
for i in x:print(i)
