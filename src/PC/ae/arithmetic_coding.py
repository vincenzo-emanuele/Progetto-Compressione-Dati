#!/usr/bin/env python

import os
import argparse
from coding.encoder import ArithmeticEncoder
from coding.decoder import ArithmeticalDecoder
#from termcolor import cprint


def compress(file_in):
    #cprint(f'Input file size: {os.stat(file_in).st_size}', 'magenta')
    '''with open(file_in, 'rb') as f:
        content = f.read()'''
    content = file_in

    ae = ArithmeticEncoder(content)
    content_fraction, length, symbols_dict = ae.encode()

    '''fw = FileWriter(file_out)
    fw.write(content_fraction, length, symbols_dict)'''
    
    return content_fraction, length, symbols_dict
    #cprint(f'Output file size: {os.stat(file_out).st_size}', 'green')


def decompress(content_fraction, length, symbols_dict):
    #cprint(f'Input file size: {os.stat(file_in).st_size}', 'cyan')
    #fr = FileReader(file_in)
    #content_fraction, length, symbols_dict = fr.read()

    ad = ArithmeticalDecoder(content_fraction, length, symbols_dict)
    decoded_content = ad.decode()

    '''with open(file_out, 'wb') as f:
        f.write(decoded_content)'''
    fileOut = open("decompresso.txt", "w")
    string = ""
    for char in decoded_content:
        string += char
    fileOut.write(string)
    #print("Decodifica:", decoded_content)
    #cprint(f'Output file size: {os.stat(file_out).st_size}', 'blue')


def main():
    action_dict = dict(compress=compress, decompress=decompress)
    parser = argparse.ArgumentParser(description='Compress/Decompress files using arithmetic coding algorithm.')
    parser.add_argument('action', choices=action_dict.keys())
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()

    action = args.action
    params = [args.input, args.output]
    action_dict[action](*params)


if __name__ == '__main__':
    #main()
    #input = "ciao ciao ciao ciao ciao ciao"
    inputFile = open("alice29.txt", "r")
    listInput = inputFile.readlines()
    stringInput = ""
    for val in listInput:
        stringInput += val
    print("Compressione")
    content_fraction, length, symbols_dict = compress(stringInput)
    print("Decompressione")
    decompress(content_fraction, length, symbols_dict)