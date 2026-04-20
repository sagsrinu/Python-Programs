#######Set data type

# Set list
s={10,20,36,10}
#assging set to k
k=set(s)
#print set
print(k)
## Add value to the set
k.update([11])
print(k)
## remove value from the set
k.remove(36)
print(k)

#######frozenSet data type

# Set list
a={10,20,36,10}
#assging set to k
b=frozenset(s)
#print set
print(b)
## Add value to the set
#b.update([11])
#print(b)
## remove value from the set
#b.remove(36)
#print(b)