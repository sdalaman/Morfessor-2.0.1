import morfessor
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

def prepMorpDict(morphFile):
    dict = {}
    i = 0
    cnt = 0
    with codecs.open(morphFile, 'r','utf-8') as f:
        for line in f:
            i += 1
            if line[0] in punctuation or line[0] in digits:
                cnt += 1
                continue
            words = line.split(":-")
            w1 = words[0].strip()
            w2 = words[1].replace('\n','')
            w2 = w2.split('+')
            w2.remove('')
            w2s=''
            for i in range(len(w2)):
                w2s = w2s + w2[i] + ' \t '
            dict[w1]=w2s
    return dict

def prepMorphFile(infile,outfile,dict):
    out = codecs.open(outfile,'w','utf-8')
    with codecs.open(infile, 'r','utf-8') as f:
        for line in f:
            words = line.split()
            for i in range(len(words)):
                if words[i].strip() in dict.keys():
                    words[i] = dict[words[i]]
            newline = '\t'.join(words) + '\n'
            out.write(newline)
    out.close()

def wordCount(infile):
    lcnt = wtot = 0
    with codecs.open(infile, 'r','utf-8') as f:
        for line in f:
            lcnt += 1
            words = line.split()
            wtot += len(words)
    print("file : %s word : %d line : %d" % (infile,wtot,lcnt))
    return wtot,lcnt

prepFiles = True
if prepFiles == True:
    #inMorphFileTr = "turkish.all.tok.morph.list"
    #dictTr = prepMorpDict(inMorphFileTr)
    #infileTr = "turkish.all.tok"
    #prepMorphFile(infileTr,infileTr+".morph",dictTr)
    #inMorphFileEn = "english.all.tok.morph.list"
    #dictEn = prepMorpDict(inMorphFileEn)
    #infileEn = "english.all.tok"
    #prepMorphFile(infileEn,infileEn+".morph",dictEn)

    inMorphFileEn = "deutch.all.tok.morph.list"
    dictDe = prepMorpDict(inMorphFileEn)
    infileDe = "train.de-en.de.tok"
    prepMorphFile(infileDe,infileDe+".morph",dictDe)
    wordCount("train.de-en.de.tok")
    wordCount("train.de-en.de.tok.morph")

    inMorphFileFr = "french.all.tok.morph.list"
    dictFr = prepMorpDict(inMorphFileFr)
    infileFr = "train.en-fr.fr.tok"
    prepMorphFile(infileFr,infileFr+".morph",dictFr)
    wordCount("train.en-fr.fr.tok")
    wordCount("train.en-fr.fr.tok.morph")

    inMorphFileEn = "english.all.tok.morph.list"
    dictEn = prepMorpDict(inMorphFileEn)
    infileEn = "train.de-en.en.tok"
    prepMorphFile(infileEn,infileEn+".morph",dictEn)
    wordCount("train.de-en.en.tok")
    wordCount("train.de-en.en.tok.morph")

    inMorphFileEn = "english.all.tok.morph.list"
    dictEn = prepMorpDict(inMorphFileEn)
    infileEn = "train.en-fr.en.tok"
    prepMorphFile(infileEn,infileEn+".morph",dictEn)
    wordCount("train.en-fr.en.tok")
    wordCount("train.en-fr.en.tok.morph")

#trWdCnt,trLnCnt = wordCount("turkish.all.tok")
#trWdMrpCnt,trLnMrpCnt = wordCount("turkish.all.tok.morph")
#enWdCnt,enLnCnt = wordCount("english.all.tok")
#enWdMrpCnt,enLnMrpCnt = wordCount("english.all.tok.morph")


#print("word cnt tr : %d tr-morph: %d - en: %d en-morph: %d\n" %(trWdCnt,trWdMrpCnt,enWdCnt,enWdMrpCnt) )
#print("line cnt tr : %d tr-morph: %d - en: %d en-morph: %d\n" %(trLnCnt,trLnMrpCnt,enLnCnt,enLnMrpCnt) )
#print("tr: %f - en: %f \n" % ( 100*(trWdMrpCnt - trWdCnt)/trWdCnt,100*(enWdMrpCnt - enWdCnt)/enWdCnt ))

print("end")