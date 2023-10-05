alphabetVowel = "ауоыиэяюёе"
alphabet = "бвгджзйклмнпрстфхцчшщ"
string = input()

cnt = 0
cnt2 = 0
for i in string:
    if i in alphabetVowel:
        cnt += 1
    if i in alphabet:
        cnt2 += 1


print(cnt, cnt2)

