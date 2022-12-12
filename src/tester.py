import compression
import decompression
import sys
import filecmp

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("specify 2 parameters")
        exit()
    file_name = sys.argv[1]
    secret_key = sys.argv[2]
    print("starting compression...")
    compression.compressione(sys.argv[1], sys.argv[2])
    print("\n\nstarting decompression...")
    decompression.decompressione(sys.argv[2])
    original_file_path = "TestFiles/Input/" + sys.argv[1]
    decompressed_file_path = "TestFiles/Output/decompressed.txt"
    equals = filecmp.cmp(original_file_path, decompressed_file_path, False)
    if equals:
        print("decompression was successful")
    else:
        print("decompression failed")