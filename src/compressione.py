import Bwt.bwt as bwt
import Mtf.mtf as mtf
import Rle.rle as rle
from dahuffman import HuffmanCodec 
import time
import pickle
import multiprocessing

def block_bwt(input, key, index, return_dict):
    outputBWT = bwt.bwt_from_suffix(input, key)
    return_dict[index] = outputBWT

if __name__ == "__main__":
    inputFile = open("TestFiles/Input/PROVA.txt", "r")
    listInput = inputFile.readlines()
    stringInput = ""
    for val in listInput:
        stringInput += val

    dictionary = set(stringInput)
    dictionary.add("\003")
    dictionary = sorted(dictionary)
    #BWT
    print("Starting BWT...")
    bwtStartTime = time.time()

    # Codice per eseguire la BWT a blocchi

    block_lenght = 1024*300
    using_blocks = True
    outputBWT = ""
    key = "Chiave segreta"
    if using_blocks and len(stringInput) > block_lenght:
        print("Block mode")
        # Creo il dizionario condiviso
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        # Creo l'indice e i processi
        j=0
        process_list = []
        for i in range(0, len(stringInput),block_lenght):
            input_block = stringInput[i:i+block_lenght] + "\003" # Add EOF
            p = multiprocessing.Process(target=block_bwt, args=(input_block, key, j, return_dict))
            j+=1
            process_list.append(p)
            p.start()

        for p in process_list:
            p.join()

        for i in range(0, j):
            outputBWT += return_dict[i]

    else:
        print("Full file mode")
        stringInput += "\003" # Add EOF
        outputBWT = bwt.bwt_from_suffix(stringInput, key)

    bwtElapsedTime = time.time() - bwtStartTime
    print(str(bwtElapsedTime) + "  -> elapsed time of BWT")
    fileOutputBWT = open("TestFiles/Output/outputBWT.txt", "w+")
    fileOutputBWT.write(outputBWT)
    #salvo il dizionario della BWT
    fileOutputDictBWT = open("TestFiles/Output/outputDictBWT.txt", "w+")
    dictStr = ""
    for element in set(outputBWT):
        dictStr += element
    fileOutputDictBWT.write(dictStr)

    #MTF
    print("Starting MTF...")
    mtf_start_time = time.time()
    #print(sorted(dictionary))
    outputMTF = mtf.encode(plain_text=outputBWT, dictionary=sorted(dictionary)) 
    mtf_elapsed_time = time.time() - mtf_start_time
    print(str(mtf_elapsed_time) + "  -> elapsed time of MTF")
    fileOutputMTF = open("TestFiles/Output/outputMTF.txt", "w+")
    fileOutputMTF.write(str(outputMTF).replace(" ", ""))

    #RLE
    print("Starting RLE")
    rleModule = rle.Rle()
    rle_start_time = time.time()
    outputRLE = rle.Rle.rle_encode(rleModule, data=list(map(str, outputMTF))) # trasformo la lista di interi in lista di stringhe
    rle_elapsed_time = time.time() - rle_start_time
    print(str(rle_elapsed_time) + "  -> elapsed time of RLE")
    fileOutputRLE = open("TestFiles/Output/outputRLE.txt", "w+")
    fileOutputRLE.write(str(outputRLE))

    #PC
    codec = HuffmanCodec.from_data(outputRLE)
    encoded = codec.encode(outputRLE)
    fileOutputPC = open("TestFiles/Output/outputPC.txt", "wb")
    fileOutputPCCodec = open("TestFiles/Output/outputPCCodec.txt", "wb")
    pickle.dump(encoded, fileOutputPC)
    pickle.dump(codec, fileOutputPCCodec)