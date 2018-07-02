import sys
import re
import os
import codecs

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = ' \t\n\r\x0b\x0c'

def createFile(infile,outfile,size):
    out = codecs.open(outfile,'w','utf-8')
    cnt = 0
    with codecs.open(infile, 'r','utf-8') as f:
        for line in f:
            out.write(line)
            cnt=cnt+1
            if cnt == size:
                break
    out.close()

sizeList = [1000,10000]
typeList = ["tok","tok.morph"]
fileList = ["train.de-en.de","train.de-en.en","train.en-fr.en","train.en-fr.fr"]

prepFiles = True
if prepFiles == True:
    for size in sizeList:
        for type in typeList:
            for fname in fileList:
                inFile = fname+"."+type
                outFile =fname+"."+str(size)+"."+type
                createFile(inFile,outFile,size)

print("end")