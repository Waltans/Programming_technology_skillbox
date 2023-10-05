string = input()
firstSpace = string.find(", ")
firstNum = int(string[:firstSpace])
secondNum = int(string[firstSpace + 1:])

print (firstNum % secondNum)