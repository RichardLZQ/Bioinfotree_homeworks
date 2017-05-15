#!/usr/bin/env python
# encoding=utf-8

"""
My first bioinformatic tools for FASTA file

Richard 2017
"""

from optparse import OptionParser

import sys

args = sys.argv


def readfasta(filename):
    """
    :param filename: ；要读取的FASTA文件名
    :return: 返回基因名：序列的字典文件
    """

    fa = open(filename, 'r')
    res = {}
    ID = ''
    for line in fa:
        if line.startswith('<'):
            ID = line.strip('\n')
            res[ID] = ''
        else:
            res[ID] += line.strip('\n')

    return res


def cut35(filename, cut_5, cut_3, fileout):
    """
    用于从5/'和3/'端分别去掉几个碱基
    :param filename: 读入的文件
    :param cut_5: 5/'端要去掉的碱基数量
    :param cut_3: 3/'端要去掉的碱基数量
    :return: 返回文件fileout
    """

    of = open(fileout, 'w')

    data = readfasta(filename)

    for key, value in data.items():
        of.write(key + '\n')
        out = value[int(cut_5):][:-int(cut_3)]
        of.write(out + '\n')


def distribution(filename):
    """
    用直方图表示序列长度的分布
    用到numpy和matplotlib包
    :param filename: 
    :return: 
    """

    import numpy as np
    import pylab as pl

    data = readfasta(filename)
    res = []

    for value in data.values():
        res.append(len(value))

    dataarray = np.array(res)

    pl.hist(dataarray)
    pl.xlabel('The length of sequences')
    pl.show()


def countGC(filename, fileout):
    """
    统计整个FASTA文件中的GC含量和占比
    :param filename: 
    :param fileout: 
    :return: 
    """
    fo = open(fileout, 'w')
    data = readfasta(filename)
    NUM = 0
    GContent = 0
    for key, value in data.items():
        value = value.upper()
        NUM += len(value)
        GContent += (value.count('G') + value.count('C'))
    output = 'The total length is ' + str(NUM) + '\n' + 'The total GC content is ' + str(
        GContent) + '\n' + 'The GC ration is ' + str(float(GContent / NUM))
    print(output)
    fo.write(output)


def complement(filename, fileout):
    """
    取互补序列，即DNA to RNA
    :param filename: 
    :param fileout: 
    :return: 
    """

    fo = open(fileout, ' w')
    data = readfasta(filename)
    seq = ''

    compdic = {'A': 'A', 'T': 'U', 'G': 'G', 'C': 'C'}

    for key, value in data.items():
        fo.write(key + '\n')
        for i in value:
            seq += compdic[i]
        fo.write(seq + '\n')


def reverse(filename, fileout):
    """
    取反向序列
    :param filename: 
    :param fileout: 
    :return: 
    """
    fo = open(fileout, 'w')
    data = readfasta(filename)
    seq = []

    for key, value in data.items():
        fo.write('%s(reverse)\n' % key)
        seq = list(value)
        seq = seq.reverse()
        seq = ''.join(seq)
        fo.write('%s\n' % seq)


def main(args):
    parser = OptionParser()
    parser.add_option("-f", "--fasta", dest="filename", help="fasta filename",
                      metavar="FILE")
    parser.add_option("-o", "--txt", dest="fileout", help="output filename",
                      metavar="FILE")
    parser.add_option("--cut", "--cut-fasta", dest="cut", help="cut fasta file",
                      action="store_true", default=False)
    parser.add_option("-5", "--cut-5", dest="cut_5", type=int, help="cut fasta N(N>0) from 5'",
                      metavar="INT", default=0)
    parser.add_option("-3", "--cut-3", dest="cut_3", type=int, help="cut fasta N(N>0) from 3'",
                      metavar="INT", default=0)
    parser.add_option("--len-dis", dest="len_dis", help="sequence length distribution",
                      action="store_true", default=False)
    parser.add_option("--gc", "--count-gc", dest="gc", help="pring GC%", action="store_true",
                      default=False)
    parser.add_option("--comp", "--complement-seq", dest="comp", help="get complement sequences", action="store_true",
                      default=False)
    parser.add_option("--rev", "--reverse-seq", dest="rev", help="get reverse sequence", action="store_true",
                      default=False)

    (options, args) = parser.parse_args()

    if not options.filename:
        parser.print_help()
    filename = options.filename
    fileout = options.fileout

    if options.cut:
        cut_5 = options.cut_5
        cut_3 = options.cut_3
        cut35(filename=filename, cut_5=cut_5, cut_3=cut_3, fileout=fileout)

    if options.len_dis:
        distribution(filename=filename)

    if options.gc:
        countGC(filename=filename, fileout=fileout)

    if options.comp:
        complement(filename=filename, fileout=fileout)

    if options.rev:
        complement(filename=filename, fileout=fileout)


if __name__ == '__main__':
    main(args)
