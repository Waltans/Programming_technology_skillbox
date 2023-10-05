


string = input()
string = string.replace(" ", "")
cnt = 0

for i in range(len(string)):
    for j in range(len(string)-1):
        if string[i] == string[j+1]:
            cnt += 1
            break
    break

print(True if cnt > 0 else False)