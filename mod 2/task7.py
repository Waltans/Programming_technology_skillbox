string = input()

cntOne = 0
cntZero = 0

for i in string:
    if i == "1":
        cntOne +=1
    if i == "0":
        cntZero +=1

if cntOne == cntZero:
    print("yes")
else:
    print("no")
