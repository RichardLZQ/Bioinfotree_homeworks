def readfasta(filename, sample):
    fa = open(filename, 'r')
    fo = open(sample, 'w')
    res = {}
    rres = []
    ID = ''
    for line in fa:
        if line.startswith('>'):
            ID = line.strip('\n')
            res[ID] = ''
        else:
            res[ID] += line.strip('\n')

    for key in res.values():
        rres.append(key)
        fo.write(key + '\n')
    return rres


def fragement(seq_list):
    res = []
    seq = seq_list[0]
    for i in range(len(seq)):
        s_seq = seq[i:]
        for j in range(len(s_seq)):
            res.append(s_seq[:(len(s_seq) - j)])

    return res


def main(infile, sample):
    seq_list = readfasta(infile, sample)
    frags = fragement(seq_list)
    frags.sort(key=len, reverse=True)
    for i in range(len(frags)):
        ans = []
        # s = 0
        # m+=1
        # print(m)
        # res[frags[i]] = 0
        for j in seq_list:
            r = j.count(frags[i])
            if r != 0:
                ans.append(r)
        if len(ans) >= len(seq_list):
            print(frags[i])
            break


main('rosalind_lcsm.txt', 'sample.txt')
