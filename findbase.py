#!/usr/bin/env python
# encoding=utf-8

def findbase(filename, chrom, pos):
    fi = open(filename, 'r')
    ID = ''
    genedic = {}
    pos = int(pos)
    for line in fi:
        line = line.strip('\n')
        if line.startswith('>'):
            ID = line
            genedic[ID] = ''
        else:
            genedic[ID] += line
    key = '>chr_' + str(chrom)
    base = genedic[key][pos - 1]
    print(base)


findbase('fa1.fa', 3, 6)
