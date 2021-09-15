#!/usr/bin/python

import argparse
import pandas as pd
import numpy as np

from Bio import SeqIO
from itertools import permutations


codon_tuples = [('Phe', 'TTT'), ('Phe', 'TTC'), ('Leu', 'TTA'), ('Leu', 'TTG'), 
     ('Tyr', 'TAT'), ('Tyr', 'TAC'), ('ter', 'TAA'), ('ter', 'TAG'), 
     ('Leu', 'CTT'), ('Leu', 'CTC'), ('Leu', 'CTA'), ('Leu', 'CTG'), 
     ('His', 'CAT'), ('His', 'CAC'), ('Gln', 'CAA'), ('Gln', 'CAG'), 
     ('Ile', 'ATT'), ('Ile', 'ATC'), ('Ile', 'ATA'), ('Met', 'ATG'), 
     ('Asn', 'AAT'), ('Asn', 'AAC'), ('Lys', 'AAA'), ('Lys', 'AAG'), 
     ('Val', 'GTT'), ('Val', 'GTC'), ('Val', 'GTA'), ('Val', 'GTG'), 
     ('Asp', 'GAT'), ('Asp', 'GAC'), ('Glu', 'GAA'), ('Glu', 'GAG'), 
     ('Ser', 'TCT'), ('Ser', 'TCC'), ('Ser', 'TCA'), ('Ser', 'TCG'), 
     ('Cys', 'TGT'), ('Cys', 'TGC'), ('ter', 'TGA'), ('Trp', 'TGG'), 
     ('Pro', 'CCT'), ('Pro', 'CCC'), ('Pro', 'CCA'), ('Pro', 'CCG'), 
     ('Arg', 'CGT'), ('Arg', 'CGC'), ('Arg', 'CGA'), ('Arg', 'CGG'), 
     ('Thr', 'ACT'), ('Thr', 'ACC'), ('Thr', 'ACA'), ('Thr', 'ACG'), 
     ('Ser', 'AGT'), ('Ser', 'AGC'), ('Arg', 'AGA'), ('Arg', 'AGG'), 
     ('Ala', 'GCT'), ('Ala', 'GCC'), ('Ala', 'GCA'), ('Ala', 'GCG'), 
     ('Gly', 'GGT'), ('Gly', 'GGC'), ('Gly', 'GGA'), ('Gly', 'GGG')]


def codon_chunker(seq):
    """
    Generator function which returns a codon (three bases) at a time.
    """
    for n in range(0, len(seq), 3):
        yield seq[n: n+3] # 输出 3 nt 碱基


def get_blank_codon_table():
    """
    Returns a dictionary with every possible codon as a key.
    """
    codons = {}
    # permutations 生成所有可能的密码子 3mer
    for perm in permutations('AAACCCGGGTTT', 3):
        codons[''.join(perm)] = 0
    
    return codons


def map_codons_to_aa(df, codon_table):
    """
    Takes a dataframe of codon frequencies and returns a sorted,
    indexed dataframe with amino acid -> codon mapping.
    """
    codon_df = pd.DataFrame(codon_table, columns=['AA', 'Codon'])
    codon_df.set_index('Codon', inplace=True)
    
    return codon_df.join(df, how='outer').reset_index().sort_values(by='AA').set_index(['AA', 'Codon'])


def calc_codon_freq(fasta_handle):
    """
    Takes the handle for a fasta file and returns the codon
    usage frequencies and total number of codons.
    ### Take note: this assumes that the fasta seqs are in frame
    ### and continuous (ie do not contain any introns, utrs, etc.)
    ### use something like transdecoder if you need to predict orfs.
    """
    codon_table = get_blank_codon_table()
    total_num_codons = 0
    for rec in SeqIO.parse(fasta_handle, 'fasta'):
        # codon_chunker is a generator which returns three bases
        # 返回 fasta 序列的3碱基密码子
        for codon in codon_chunker(str(rec.seq)):
            # this exception block captures any unknown bases (eg N's)
            try:
                codon_table[codon] += 1 # 计算相应密码子出现次数
                total_num_codons += 1
            except KeyError:
                print ('Warning: unknown codon! {}'.format(codon))

    return codon_table, total_num_codons


def calc_freq(fasta_handle):
    """
    Takes the handle for a fasta file and returns a pandas 
    dataframe containing a codon usage frequencies as well as the
    relative synonomous codon usage values for each codon.
    """
    codon_table, total_num_codons = calc_codon_freq(fasta_handle)
    df = pd.DataFrame.from_dict(codon_table, orient='index')
    df.columns = ['freq']
    df.index.name = 'Codon'
    # calculate the relative synonomous codon usage (rscu)
    df['rscu'] = df['freq'] / float(total_num_codons)
    
    return df, total_num_codons


def cmd_arguments():
    usage = "codon_usage_calculator.py [options] <input fasta>\n"
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument('input_fasta', type=str, 
                        help='The input fasta file of coding sequences')
    parser.add_argument('--out', '-o', dest='write', default=False,
                        help='Path to write codon frequencies to file.')

    return parser.parse_args()


def main():
    args = cmd_arguments()
    fasta_handle = args.input_fasta

    df, total_num_codons = calc_freq(fasta_handle)
    df = map_codons_to_aa(df, codon_tuples)
    if args.write:
        df.to_csv(args.write, sep='\t')
    else:
        print('Codon usage frequencies for: {}'.format(fasta_handle))
        print('Total number of codons in file: {}'.format(total_num_codons))
        print(df.to_string())

if __name__ == '__main__':
    main()
