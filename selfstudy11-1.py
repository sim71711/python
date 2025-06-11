inFp = None
inStr = ""
lineNum = 1

inFp = open("C:/Temp/data1.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="")
    lineNum += 1

inFp.close()
