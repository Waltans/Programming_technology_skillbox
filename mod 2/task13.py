string = input()
cnt_nechet  = 0
cnt_chet  = 0

for i in range(len(string)):
    if (i % 2 == 0):
        cnt_nechet += int(string[i])
    else:
        cnt_chet += int(string[i])

if (cnt_nechet + cnt_chet * 3) % 10 == 0:
    print("yes")
else:
    print("no")

