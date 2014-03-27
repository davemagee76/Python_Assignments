#!/usr/bin/env python3

__author__ = 'David Magee'

import sys
import re
from collections import defaultdict
from collections import Counter
import itertools


''' Problems to be solved:
1: Read in input file
2: Define a function to calculate and print sequence length
3: Define a function that will calculate and print:
    (a) the Plus Strand Features:number
    (b) the Minus Strand Features:number
    (c) the Total Features:number
4: Define a function that counts how many of each Feature type are annotated on each strand:
    (a) print Feature_type:Plus_strand:number
    (b) print Feature_type:Minus_strand:number,
    where Feature_type is how it appears in the file
5: Define a function that will extract the sequence of CDS features in the first 20,600 base pairs and write them to a
file'''


def count_seq_length(seq):
    seq_length = len(seq)
    return (seq_length)

def calc_rev_comp(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in reversed(seq)])


def calc_CDS_plus(a, b, seq):
    CDS_seq_plus = seq[a:b]
    return (CDS_seq_plus)

def calc_CDS_minus(d, e, reverse_complement):
    CDS_seq_minus = reverse_complement[d:e]
    return (CDS_seq_minus)


#def calcCharacter(a,b,c,d,e):
#funct2=e[a:b+1]+(' ')+e[c:d+1]	## Add 1 to the 'b' and 'd' elements
#return(funct2)
#finish



# Expecting three elements from the command line (python script, two input files and output file)
if len(sys.argv) != 3:
    print("{}: You must supply an argument on the command line after the python script".format(sys.argv[0]))
    sys.exit(1)

# fin_1 (i.e. input file 1 = pHCM1.fasta); fin_2 (i.e. input file 2 = pHCM1.tab)
#with open(sys.argv[1], 'r') as fin_1, open(sys.argv[2], 'r') as fin_2, open(sys.argv[3], 'w') as fout:
with open(sys.argv[1], 'r') as fin_1, open(sys.argv[2], 'r') as fin_2:
    # To solve part 2 of the assignment
    # For each line in input file:
    for line in fin_1:
        #   strip the line (returns string for the current line)
        data = line.strip()
        #   split the line (returns a list for the current line)
        data = data.split('\t')
    #print(data)

    seq = data[0]
    print(seq)
    length_of_sequence = count_seq_length(seq)
    #print(length_of_sequence)

    # get reverse complement
    reverse_complement = calc_rev_comp(seq)
    #print(reverse_complement)

    # To solve parts 2 and 3 of the assignment

    features_total_dict = {}  # generate a dictionary for counting all features on both strands
    features_dict_minus = {}  # generate a dictionary for counting all features on minus strand
    features_dict_plus = {}  # generate a dictionary for counting all features on plus strand
    CDS_dict = {}

    # initialise a counter
    CDS_count = 0

    for line in fin_2:
        features = line.strip()
        features = features.split(' ')  # split using a single space
        #print(features)

        if features[3] != "":
            #print(features)
            if features[3] in features_total_dict:
                features_total_dict[features[3]] += 1
            else:
                features_total_dict[features[3]] = 1
                #print(features_total_dict)

        if features[3] != "":
            if "complement" in features[-1]:
                #print(features)
                if features[3] in features_dict_minus:
                    features_dict_minus[features[3]] += 1
                else:
                    features_dict_minus[features[3]] = 1
                    #print(features_dict_minus)

        if features[3] != "":
            if "complement" not in features[-1]:
                #print(features)
                if features[3] in features_dict_plus:
                    features_dict_plus[features[3]] += 1
                else:
                    features_dict_plus[features[3]] = 1
                    #print(features_dict_plus)

        # To solve part 4 of the assignment
        if features[3] == "CDS":  # select only those features that are CDS sequences on plus and minus strands
            CDS_count += 1  # generate a variable called header that is the total number of CDS sequences
            header = CDS_count
            #print(header)
            #print(features)
            #if features[3] in CDS_dict:
            #CDS_dict[features[3]] += 1
            #else:
            #CDS_dict[features[3]] = 1
            #print(CDS_dict) # There are 246 CDS features in this Genbank entry


            # get the plus co-ordinates
            if "complement" not in features[-1]:
                CDS_coords_plus = features[-1]
                #print(CDS_coords_plus)
                CDS_coords_plus = CDS_coords_plus.split('..')
                a = CDS_coords_plus[0]
                a = int(a)  # convert to integer
                #print(a)
                b = CDS_coords_plus[1]
                b = int(b) + 1  # add 1 to the each field in the list
                c = b - a  #print(c) # get the length of each CDS sequence for sanity checks
                CDS_sequences_plus = calc_CDS_plus(a,b,seq)
                #print("> \n{}\n".format(CDS_sequences_plus))

            # get the minus co-ordinates
            if "complement" in features[-1]:
                CDS_coords_minus = features[-1]
                CDS_coords_minus = CDS_coords_minus.split('(')
                CDS_coords_minus = CDS_coords_minus[-1]
                CDS_coords_minus = CDS_coords_minus[:-1]
                #CDS_coords_minus = CDS_coords_minus.split('..')

                #print(CDS_coords_minus)
                pattern = re.compile("(\d+)\.\.(\d+)")
                match = pattern.search(CDS_coords_minus)
                if match:
                    #print(match.group(0))
                    CDS_coords_minus = match.group(0).split('..')
                    #print(CDS_coords_minus)

                d = CDS_coords_minus[0]
                #print(d)
                d = int(d)
                e = CDS_coords_minus[1]
                e = int(e)+1
                print(e-d)
                CDS_sequences_minus = calc_CDS_minus(d,e,reverse_complement)
                print(">> \n{}\n".format(CDS_sequences_minus))