#!/usr/bin/env python
# encoding=utf-8
import sys
args = sys.argv




class Gene:
    def __init__(self):
        self.chr = ''
        self.start = 0
        self.end = 0
        self.orientation = 0
        self.id = ''


def main(args):


    chr_list = {}
    fi = open(args[1], 'r')
    for line in fi:
        lines = line.strip('\n').split()

        id = lines[0]
        chrs = lines[1][:4]
        start = lines[2]
        end = lines[3]
        orientation = lines[4]

        if not chrs in chr_list:
            chr_list[chrs] = {}

        gene = Gene()
        gene.start = int(start)
        gene.end = int(end)
        gene.chr = chrs
        gene.orientation = int(orientation)
        gene.id = id
        chr_list[chrs][id] = gene

    fi2 = open(args[2], 'r')
    gene_list = []
    for line in fi2:
        lines = line.strip('\n').split()
        chrs = lines[0]
        start = int(lines[1])
        end = int(lines[2])
        for id, gene in chr_list[chrs].items():
            if (gene.start <= start <= gene.end) or (gene.start <= end <= gene.end) or (start <= gene.start <= end) or (
                            start <= gene.end <= end):
                gene_list.append(id)
    print(gene_list, sep='\n')


if __name__ == '__main__':
    main(args)
