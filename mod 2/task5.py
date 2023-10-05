alphabet = "abcdefghiklmnopqrstvxyz"
string = input()
firstSpace = string.find(",")
a = string[:firstSpace]
b = int(string[firstSpace + 1:])

print(alphabet[alphabet.find(a)+b:alphabet.find(a)+b+1])