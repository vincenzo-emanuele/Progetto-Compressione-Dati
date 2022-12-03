import Bwt.bwt as bwt
import Mtf.mtf as mtf
import Rle.rle as rle
import time
import pickle
from dahuffman import HuffmanCodec

start = time.time()
# leggo il dizionario salvato dalla bwt in fase di compressione
dictionaryFile = open("TestFiles/Output/outputDictBWT.txt")
dictionaryLines = dictionaryFile.readlines()
dictionaryStr = ""
for string in dictionaryLines:
    dictionaryStr += string


# IPC
encodedFile = open("TestFiles/Output/outputPC.txt", "rb")
codecFile = open("TestFiles/Output/outputPCCodec.txt", "rb")
encoded = pickle.load(encodedFile)
codec = pickle.load(codecFile)
outputPC = codec.decode(encoded)

# IRLE
'''rleFile = open("TestFiles/Output/outputRLE.txt", "r")
rleLines = rleFile.readlines()
rleString = ""
for val in rleLines:
    rleString += val'''
rleModule = rle.Rle()
rleDecodedString = rle.Rle.rle_decode(rleModule, data=outputPC)
#print(rleDecodedString)

# IMTF
mtfList = rleDecodedString.split(",")
res = []
for i in mtfList:
    res.append(int(i))
mtfDecodedString = mtf.decode(res, dictionary=sorted(dictionaryStr))
#print("-----MTF: " + mtfDecodedString)

# IBWT

# Dividi in blocchi mtfDecodedString
block_lenght = 1024*300 +1 # Deve essere la stessa usata in compressione +1 per l'EOF
using_blocks = True
bwtDecodedString = []
if using_blocks and len(mtfDecodedString) > block_lenght:
    print("Block mode")
    for i in range(0, len(mtfDecodedString),block_lenght):
        input_block = mtfDecodedString[i:i+block_lenght]
        bwtDecodedString.extend(bwt.ibwt_from_suffix(input_block)) 

else:
    print("Full file mode")
    bwtDecodedString = bwt.ibwt_from_suffix(mtfDecodedString)

print(bwtDecodedString)
outputBWTFile = open("TestFiles/Output/decompresso.txt", "w+")
outputBWTString = ""
for i in range(0, len(bwtDecodedString)):
    outputBWTString += bwtDecodedString[i]
outputBWTFile.write(str(outputBWTString))

print("elapsed time: " + str(time.time() - start))