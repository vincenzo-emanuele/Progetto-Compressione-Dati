from math import floor, ceil
import pickle

#ASCII_TO_INT: dict = {i.to_bytes(1, 'big'): i for i in range(256)}
#INT_TO_ASCII: dict = {i: b for b, i in ASCII_TO_INT.items()}


def compress(data: str) -> bytes:
    alpha_list = sorted(set(data))
    if type(data) is str:
        data = data.encode()
    
    alphabeth = {}
    i_char = 0
    for char in alpha_list:
        alphabeth[char.encode()] = i_char
        i_char += 1
    keys: dict = alphabeth.copy()
    n_keys: int = len(alpha_list)
    compressed: list = []
    start: int = 0
    n_data: int = len(data)+1
    while True:
        if n_keys >= len(alpha_list) * 2: # Max dimensione che sono disposto a fornire al dizionario
            keys = alphabeth.copy()
            n_keys = len(alpha_list)
        for i in range(1, n_data-start):
            w: bytes = data[start:start+i]
            if w not in keys:
                compressed.append(keys[w[:-1]])
                keys[w] = n_keys
                start += i-1
                n_keys += 1
                break
        else:
            compressed.append(keys[w])
            break
    bits: str = ''.join([bin(i)[2:].zfill(9) for i in compressed])
    return int(bits, 2).to_bytes(ceil(len(bits) / 8), 'big'), alphabeth


def decompress(data: str, compression_alphabeth: dict) -> bytes:
    alpha_list = compression_alphabeth.keys()
    i_key = 0
    alphabeth = {}
    for key in alpha_list:
        alphabeth[i_key] = key
        i_key += 1
    
    if type(data) is str:
        data = data.encode()
    keys: dict = alphabeth.copy()
    bits: str = bin(int.from_bytes(data, 'big'))[2:].zfill(len(data) * 8)
    n_extended_bytes: int = floor(len(bits) / 9)
    bits: str = bits[-n_extended_bytes * 9:]
    data_list: list = [int(bits[i*9:(i+1)*9], 2)
                       for i in range(n_extended_bytes)]
    previous: bytes = keys[data_list[0]]
    uncompressed: list = [previous]
    n_keys: int = len(alpha_list)
    for i in data_list[1:]:
        if n_keys >= len(alpha_list) * 2:
            keys = alphabeth.copy()
            n_keys = len(alpha_list)
        try:
            current: bytes = keys[i]
        except KeyError:
            current = previous + previous[:1]
        uncompressed.append(current)
        keys[n_keys] = previous + current[:1]
        previous = current
        n_keys += 1
    return b''.join(uncompressed)

if __name__ == "__main__":
    inputFile = open("../TestFiles/Input/alice29.txt", "r")
    listInput = inputFile.readlines()
    stringInput = ""
    for val in listInput:
        stringInput += val
    #stringInput = "Ciaonelmao"
    compression, dictionary = compress(stringInput)
    print("Compressione:", compression)
    fileout = open("out.txt", "wb")
    fileout.write(compression)
    fileoutDict = open("outDict.txt", "wb")
    pickle.dump(dictionary, fileoutDict)

    decompression = decompress(compression, dictionary).decode()
    filein = open("in.txt", "w")
    filein.write(decompression)
    print("Decompressione:", decompression)
    print("Vero?", decompression == stringInput)