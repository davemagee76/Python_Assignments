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
    return seq_length


# Expecting three elements from the command line (python script, two input files and output file)
if len(sys.argv) != 4:
    print("{}: You must supply an argument on the command line after the python script".format(sys.argv[0]))
    sys.exit(1)

# fin_1 (i.e. input file 1 = pHCM1.fasta); fin_2 (i.e. input file 2 = pHCM1.tab)
with open(sys.argv[1], 'r') as fin_1, open(sys.argv[2], 'r') as fin_2, open(sys.argv[3], 'w') as fout:
    # To solve part 2 of the assignment
    # For each line in input file:
    for line in fin_1:
        #   strip the line (returns string for the current line)
        data = line.strip()
        #   split the line (returns a list for the current line)
        data = data.split('\t')
    #print(data)

    seq = data[0]
    # print(seq)
    length_of_sequence = count_seq_length(seq)
    #print(length_of_sequence)


    # To solve parts 3 and 4 of the assignment

    features_total_dict = {}  # generate a dictionary for counting all features on both strands
    features_dict_minus = {}  # generate a dictionary for counting all features on minus strand
    features_dict_plus = {}  # generate a dictionary for counting all features on plus strand

    for line in fin_2:
        features = line.strip()
        features = features.split(' ')  # split using a single space
        #print(features)

        if features[3] != "":
            print(features)
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
