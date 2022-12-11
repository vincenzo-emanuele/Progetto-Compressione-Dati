import compressione
import decompressione
import platform
import os
import sys
import filecmp

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("specify 2 parameters")
        exit()
    file_name = sys.argv[1]
    secret_key = sys.argv[2]
    print("inizio compressione...")
    compressione.compressione(sys.argv[1], sys.argv[2])
    print("\n\ninizio decompressione...")
    decompressione.decompressione(sys.argv[2])
    original_file_path = "TestFiles/Input/" + sys.argv[1]
    decompressed_file_path = "TestFiles/Output/decompresso.txt"
    equals = filecmp.cmp(original_file_path, decompressed_file_path, False)
    if equals:
        print("La decompressione è andata a buon fine")
    else:
        print("Decompressione fallita")