string = input()
firstSpace = string.find( "." )
a = string[:firstSpace]
secondSpace = string.find( ".", firstSpace + 1 )
b = string[firstSpace + 1:secondSpace]
c = string[secondSpace + 1:]

print(c)
print(b)
print(a)