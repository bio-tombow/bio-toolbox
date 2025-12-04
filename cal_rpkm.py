

import os
import sys

'''
'''
count_f = sys.argv[1]
rpkm_f = count_f.split('.txt')[0]+'.rpkm.txt'
'''
'''

gene2len = {}
with open('/mnt/disk1/test/SC+OO/BMK_DATA_20241024105134_1/rnaseq.rst/0.ref/genomic.gff') as f:
    for lines in f.readlines():
        if not lines.startswith('#'):
            line = lines.split('\t')
            if line[2] == 'gene':
                s,e = [int(a) for a in line[3:5]]
                #
                gene = line[-1].split('locus_tag=')[1].split(';')[0]
                gene2len[gene] = e-s+1


g2c = {};total = 0
with open(count_f) as f:
    for lines in f.readlines():
        if not lines.startswith('__'):
            g,c = lines.strip().split('\t')
            g = g.split('gene-')[1]
            ##
            c = int(c)
            ##
            g2c[g] = c;total +=c

h = open(rpkm_f,'w')
for g in g2c:
    if g in gene2len:
        c=g2c[g];l = gene2len[g]
        rpkm = 10**9*c/(total*l)
        rpkm = round(rpkm,4)
        h.write(g+'\t'+str(rpkm)+'\n')
h.close()