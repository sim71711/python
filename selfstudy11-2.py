inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for i in range(len(inList)):
    print("%d: %s" % (i + 1, inList[i]), end="")

inFp.close()
