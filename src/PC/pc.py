from dahuffman import HuffmanCodec
import pickle
#import json
from lzw3 import compressor, decompressor

def compress(input, flag: int):
    '''
    To select Desired Algorithm:\n
    0 = Huffman\n
    1 = Arithmetic Coding
    '''
    encoded = ""

    if flag == 0:
        print("Using Huffman")
        codec = HuffmanCodec.from_data(input)
        encoded = codec.encode(input)
        fileOutputPCCodec = open("TestFiles/Output/outputPCCodec.txt", "wb")
        pickle.dump(codec, fileOutputPCCodec)
        
        '''elif flag == 1:
            print("Using Arithmetic Coding")
            getcontext().prec = len(input)
            alphabeth = sorted(set(input))
            # Initialize dict with all characters
            freq_chars = dict()
            for char in alphabeth:
                freq_chars[char] = 0

            # Calculate chars frequencies
            for i in input:
                freq_chars[i] += 1
            
            coder = pyae.ArithmeticEncoding(frequency_table=freq_chars)
            encoded, encoder , interval_min_value, interval_max_value  = coder.encode(msg=input, probability_table=coder.probability_table)
            #encoded, encoder = coder.encode_binary(float_interval_min=interval_min_value, float_interval_max=interval_max_value)
            length = len(input)
            if __name__ == "__main__":
                fileAE = open("../TestFiles/Output/freqAE.txt", "w")
            else:
                fileAE = open("TestFiles/Output/freqAE.txt", "w")
            fileAE.write(str(length) + "\n")
            fileAE.write(json.dumps(freq_chars))
            fileAE.close()
            return encoded'''
    elif flag == 2:
        print("Not implemented")
        
        # LZW

    fileOutputPC = open("TestFiles/Output/outputPC.txt", "wb")
    pickle.dump(encoded, fileOutputPC)


def decompress(input, flag):
    '''
    To select Desired Algorithm:\n
    0 = Huffman\n
    1 = Arithmetic Coding
    '''

    output = ""
    
    if flag == 0:
        print("Using Huffman")
        codecFile = open("TestFiles/Output/outputPCCodec.txt", "rb")
        codec = pickle.load(codecFile)
        output = codec.decode(input)
    '''elif flag == 1:
        print("Using Arithmetic Coding")
        if __name__ == "__main__":
            fileAE = open("../TestFiles/Output/freqAE.txt", "r")
        else:
            fileAE = open("TestFiles/Output/freqAE.txt", "r")

        length = int(fileAE.readline())
        getcontext().prec = length
        # Get the frequency table
        data = fileAE.readline()
        freq_chars = json.loads(data)
        #print("LUNGHEZZA:", length, "FREQ:", freq_chars)
        codec = pyae.ArithmeticEncoding(frequency_table=freq_chars)
        output_ae, decoder = codec.decode(input, length, codec.probability_table)'''

    return output 

if __name__ == "__main__":
    input = "ciao orazio questa\nè una richiesta di §e$$o"
    encoded = compress(input, 1)
    print("CODIFICA:", encoded)
    decoded = decompress(encoded, 1)
    print("Decodifica:", decoded, "UGUALI?", input == decoded)