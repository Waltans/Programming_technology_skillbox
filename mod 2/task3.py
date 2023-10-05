string = input()
firstSpace = string.find( " " )
a = int( string[:firstSpace] )
secondSpace = string.find( " ", firstSpace + 1 )
b = int( string[firstSpace + 1:secondSpace] )
c = int( string[secondSpace + 1:] )

if (a <= b <= c) or (c <= b <= a):
    print(b)
elif (b <= a <= c) or (c <= a <= b):
    print(a)
else:
    print(c)