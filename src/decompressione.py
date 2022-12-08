import Bwt.bwt as bwt
import Mtf.bmtf as bmtf
import Rle.rle as rle
import PC.pc as pc
import pickle
import time
import multiprocessing

def block_bwt(input, key, index, return_dict):
    output = bwt.ibwt_from_suffix(input, key)
    return_dict[index] = output


if __name__ == "__main__":
    start = time.time()
    # leggo il dizionario salvato dalla bwt in fase di compressione
    dictionaryFile = open("TestFiles/Output/outputDictBWT.txt")
    dictionaryLines = dictionaryFile.readlines()
    dictionaryStr = ""
    for string in dictionaryLines:
        dictionaryStr += string

    # IPC
    pcStartTime = time.time()

    encodedFile = open("TestFiles/Output/outputPC.txt", "rb")
    encoded = pickle.load(encodedFile)
    
    outputPC = pc.decompress(encoded, 2)

    pcElapsedTime = time.time() - pcStartTime
    print(str(pcElapsedTime) + "  -> elapsed time of IPC")
    #print("OUTPUT", outputPC[:500])

    # IRLE
    '''rleFile = open("TestFiles/Output/outputRLE.txt", "r")
    rleLines = rleFile.readlines()
    rleString = ""
    for val in rleLines:
        rleString += val'''
    rleStartTime = time.time()
    
    rleModule = rle.Rle()
    rleDecodedString = rle.Rle.rle_decode(rleModule, data=outputPC)
    #print(rleDecodedString)

    rleElapsedTime = time.time() - rleStartTime
    print(str(rleElapsedTime) + "  -> elapsed time of IRLE")

    # IMTF
    
    mtfStartTime = time.time()

    key = "Chiave segreta"
    block_size = 1024

    mtfList = rleDecodedString.split(",")
    res = []
    for i in mtfList:
        res.append(int(i))
    #mtfDecodedString = mtf.decode(res, dictionary=sorted(dictionaryStr))
    mtfDecodedString = bmtf.secure_decode(res, sorted(dictionaryStr), key, block_size)
    #print("-----MTF: " + mtfDecodedString)

    mtfElapsedTime = time.time() - mtfStartTime
    print(str(mtfElapsedTime) + "  -> elapsed time of IMTF")

    # IBWT

    bwtStartTime = time.time()

    # Dividi in blocchi mtfDecodedString
    block_lenght = 1024*300 +1 # Deve essere la stessa usata in compressione +1 per l'EOF
    using_blocks = True
    bwtDecodedString = []   
    rFile = open("TestFiles/Output/rfile.txt", "r")
    r = rFile.readline()

    if using_blocks and len(mtfDecodedString) > block_lenght:
        print("Block mode")
        # Creo la variabile condivisa
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        # Divido l'input e creo i processi
        j = 0
        processList = []
        for i in range(0, len(mtfDecodedString),block_lenght):
            input_block = mtfDecodedString[i:i+block_lenght]
            p = multiprocessing.Process(target=block_bwt, args=(input_block, r + key, j, return_dict))
            j+=1
            processList.append(p)
            p.start()
        
        for p in processList:
            p.join()

        for i in range(0,j):
            bwtDecodedString.extend(return_dict[i])
    else:
        print("Full file mode")
        bwtDecodedString = bwt.ibwt_from_suffix(mtfDecodedString, key)

    #print(bwtDecodedString)
    outputBWTFile = open("TestFiles/Output/decompresso.txt", "w+")
    outputBWTString = ""
    for i in range(0, len(bwtDecodedString)):
        outputBWTString += bwtDecodedString[i]
    outputBWTFile.write(str(outputBWTString))

    bwtElapsedTime = time.time() - bwtStartTime
    print(str(bwtElapsedTime) + "  -> elapsed time of IBWT")

    print("Total elapsed time: " + str(time.time() - start))