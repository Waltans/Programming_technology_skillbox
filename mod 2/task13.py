string = input()
cnt_chet  = 0
cnt_nechet  = 0

for i in range(len(string)):
    if (i % 2 == 0):
        cnt_chet += int(string[i])
    else:
        cnt_nechet += int(string[i])

if ((cnt_nechet*3 + cnt_chet) % 10 == 0):
    print("yes")
else:
    print("no")

