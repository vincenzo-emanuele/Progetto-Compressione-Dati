import compression
import decompression
import sys
import filecmp

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Missing arguments, proceeding with default ones\nname=alice29.txt, key=Chiave Segreta and mode = 0" )
        file_name = "alice29.txt"
        secret_key = "Chiave segreta"
        mode = 0
    else:
        file_name = sys.argv[1]
        secret_key = sys.argv[2]
        mode = int(sys.argv[3])
    print("starting compression...")
    compression.compressione(file_name, secret_key, mode)
    print("\n\nstarting decompression...")
    decompression.decompressione(secret_key, mode)
    original_file_path = "TestFiles/Input/" + file_name
    decompressed_file_path = "TestFiles/Output/decompressed.txt"
    equals = filecmp.cmp(original_file_path, decompressed_file_path, False)
    if equals:
        print("decompression was successful")
    else:
        print("decompression failed")