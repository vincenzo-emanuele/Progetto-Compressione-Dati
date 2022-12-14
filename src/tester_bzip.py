import bz2
import sys
import time
import filecmp

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Specify file name to compress!!!")
        exit()
    file_name = sys.argv[1]
    path = "TestFiles/Input/" + file_name
    
    print("Reading file...\n")
    file = open(path, "rb")
    '''contentLines = file.readlines()
    content = ""
    for line in contentLines:
        content += line
    byteContent = content.encode()'''
    byteContent = file.read()
    
    print("Finished reading, starting compression...")
    compression_start = time.time()
    encoded = bz2.compress(byteContent)
    compression_end = time.time()
    
    print("Finished compression, elapsed time: ", compression_end - compression_start)
    compressedFile = open("compressed.txt", "wb")
    compressedFile.write(encoded)

    print("\n\nStarting decompression...")
    decompression_start = time.time()
    decoded = bz2.decompress(encoded)
    decompression_end = time.time()
    print("Finished decompression, elapsed time:", decompression_end - decompression_start)

    decompressedFile = open("decompressed.txt", "w")
    decompressedFile.write(decoded.decode())
    result = filecmp.cmp(path, "decompressed.txt", False)
    if result:
        print("Compression and decompression successfully")
    else:
        print("Some error occurred, files are different")
