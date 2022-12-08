from dahuffman import HuffmanCodec
import pickle
#import json
import PC.lzw as lzw
import PC.arithmetic_coding as arithmetic_coding

def compress(input, flag: int):
    '''
    To select Desired Algorithm:\n
    0 = Huffman\n
    1 = Arithmetic Coding (Non implementato)\n
    2 = LZW
    '''
    encoded = ""

    if flag == 0:
        print("Using Huffman")
        codec = HuffmanCodec.from_data(input)
        encoded = codec.encode(input)
        fileOutputPCCodec = open("TestFiles/Output/outputPCCodec.txt", "wb")
        pickle.dump(codec, fileOutputPCCodec)
        
    elif flag == 1:
        print("Using Arithmetic Coding")
        encoded, length, symbols_dict = arithmetic_coding.compress(input)
        support_data = (length, symbols_dict)
        fileAE = open("TestFiles/Output/fileAE.txt", "wb")
        pickle.dump(support_data, fileAE)
        
    elif flag == 2:
        print("LZW")
        encoded, dictionary = lzw.compress(input)
        fileOutputDict = open("TestFiles/Output/outputDictLZW.txt", "wb")
        pickle.dump(dictionary, fileOutputDict)
        
        # LZW

    fileOutputPC = open("TestFiles/Output/outputPC.txt", "wb")
    pickle.dump(encoded, fileOutputPC)


def decompress(input, flag):
    '''
    To select Desired Algorithm:\n
    0 = Huffman\n
    1 = Arithmetic Coding\n
    2 = LZW
    '''

    output = ""
    
    if flag == 0:
        print("Using Huffman")
        codecFile = open("TestFiles/Output/outputPCCodec.txt", "rb")
        codec = pickle.load(codecFile)
        output = codec.decode(input)
    
    elif flag == 1:
        print("Using Arithmetic Coding")
        fileAE = open("TestFiles/Output/fileAE.txt", "rb")
        support_data = pickle.load(fileAE)
        length = support_data[0]
        symbols_dict = support_data[1]
        output = arithmetic_coding.decompress(input, length, symbols_dict)

    elif flag == 2:
        print("Using LZW")
        fileDict = open("TestFiles/Output/outputDictLZW.txt", "rb")
        dictionary = pickle.load(fileDict)
        output = lzw.decompress(input, dictionary).decode()

    return output 

if __name__ == "__main__":
    input = "ciao orazio questa\nè una richiesta di §e$$o"
    encoded = compress(input, 1)
    print("CODIFICA:", encoded)
    decoded = decompress(encoded, 1)
    print("Decodifica:", decoded, "UGUALI?", input == decoded)