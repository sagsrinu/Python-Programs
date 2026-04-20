#int(string,base)
#--- convert a string into a decimal integer

str="1c2"
n=int(str,16)
print(n)

## Python program to convert into decimal number system 
s1="17"
s2="1110010"
s3="1c2"

n=int(s1,8)
print('Octal 17=',n)
n=int(s2,2)
print('Binary of 1110010=',n)
n=int(s3,16)
print('hexa decimal=',n)

