'''
x = -321
s = str(x)
i = list(s[::-1])
print(i)
run = True
for x in range(0, len(i)-1):

    if i[-1] == "-":
        i = i[-1:] + i[:-1]
    if i[0] == "0":
        while run == True:
            print("while", i)
            if x < len(i):
                if i[x] == "0" and i[x + 1] == "0":
                    i[x] = "_"
                if i[x+1] != "0":
                    i[x] = "_"
                    run = False
                x += 1
print(i)
#print(i)
finalList = list(filter(lambda a: a != "_", i))

final =""
for y in range(len(finalList)):
    final += finalList[y]

finalRes = int(final)
if finalRes < -2**31 or finalRes > (2**31) - 1:
    print(0)
print(finalRes)

'''

s = "hello (Offical Audio)"
q = "hello (Offical Video)"
print(s[::-1])
print(q[::-1])
r = (q[::-1])[16::][::-1]
print(r)