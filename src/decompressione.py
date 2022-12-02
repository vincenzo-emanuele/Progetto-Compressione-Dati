import Bwt.bwt as bwt
import time

fileI = open("TestFiles/Output/outputBWT.txt", "r")
lines = fileI.readlines()
outLines = ""
for val in lines:
    outLines += val
inverse = bwt.ibwt_from_suffix(outLines)
fileO = open("TestFiles/Output/decompresso.txt", "w+")
strInverse = ""
for i in range(1, len(inverse)):
    strInverse += inverse[i]
fileO.write(str(strInverse))
