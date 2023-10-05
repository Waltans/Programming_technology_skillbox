string = input()
firstSpace = string.find(",")
a = string[:firstSpace] + " "
symbol = string[firstSpace + 1:]
cnt = 0

for i in range(len(a)):
    if a[i] == symbol:
        cnt += 1
    if cnt > 0 and a[i+1] != symbol:
        break

print(cnt)