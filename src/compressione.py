import Bwt.bwt as bwt
import time

file = open("TestFiles/Input/input.txt", "r")
lines = file.readlines()
outLines = ""
for val in lines:
    outLines += val
outLines += "\003" #add EOF
print("Starting BWT...")
Bmtf_start_time = time.time()
output = bwt.bwt_from_suffix(outLines)
Bmtf_elapsed_time = time.time() - Bmtf_start_time
print(str(Bmtf_elapsed_time) + "  -> elapsed time of BWT")
fileO = open("TestFiles/Output/outputBWT.txt", "w+")
fileO.write(output)
