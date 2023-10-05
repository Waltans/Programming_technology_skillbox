string = input()
result = ""

cnt = 0
while cnt < len(string):
    if string[cnt] == " ":
        result += string[cnt-1]
    cnt += 1

print(result+ string[-1])

