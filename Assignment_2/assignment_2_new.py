#!/usr/bin/env python3

__author__ = 'David Magee'

import sys
import math


# Background to problem
# For this problem, the input file has the following structure:
#
# mass(g)    volume(mls)  molarity(M) element1    no_atoms_element1   element2    no-atoms-element2   element3    ....
# 0           1           2           3           4                   5           6
# where, 0, 1,... are the 0th, 1st,... elements in the lines of the input files
#
# mass, volume and molarity are constant variables.
# chemical elements and the number of atoms for each element are changeable variables.
# As, the information for the elements are pairs (i.e. element name and no. of atoms) (i.e. the number of element paris
# will return an even number when divided by 2)
# The length of each line of the list should be an odd number: 3 constant variables + even number of element pairs

# Expecting three elements from the command line (python script, input file and output file)
if len(sys.argv) != 3:
    print("{}: You must supply an argument on the command line after the python script".format(sys.argv[0]))
    sys.exit(1)

# mass_compound equal to sum (no. atoms*molecular weight) for each element in the compound
# Hard coded a dictionary for the mass of the elements
mass_dict = {'H': 1, 'Cl': 35, 'Na': 23, 'C': 12, 'O': 16, 'S': 32, 'Mg': 24, 'Ca': 40, 'Ag': 108, 'N': 14}


# define the function that calculates the molecular weight of the compounds in the list given
# the list of atoms, their respective number of atoms in the compound and their respective molecular weights


def calc_mol_weight (a,b,c):
    for element_1 in y1:
        molweight = mass_dict['Na']+mass_dict['Cl']
        return(molweight)

    '''for element_2 in y2:
        molweight_2 = mass_dict['Mg']+mass_dict['O']
        return(molweight_2)'''


# define the function that solves mass given volume, molarity and the compound molecular weight
#def calc_mass(volume, molarity, elements):
#   mass equals volume*molarity*sum(molecular weight*no. of atoms) for each element in compound
# mass = volume*molarity*()


# Process the input file to perform the calculations:
# Read in the file from the command line and write to an outfile
with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
    # For each line in input file:
    for line in fin:
        #   strip the line (returns string for the current line)
        data = line.strip()
        #   split the line (returns a list for the current line)
        data = data.split('\t')
        #   Sanity check:
        #   if the length of the each line from the input file is not an even number:
        #     return an error message and stop the script
        #     else proceed with the script

        for line in data:
            if len(data) % 2 == 0:
                sys.exit(1)
            else:
                pass

            #   select only those lines that contain a question mark (i.e. lines needed to solve the problem)
            if "?" in line:
                data = data
                #print(data)
                if data[0] == "?":
                    y1 = data
                    for fields in y1:
                        mass_1 = y1[0]
                        volume_1 = y1[1]
                        molarity_1 = y1[2]
                        element_1 = y1[3:]
                    #print(element_1)
                    #print(y1)
                    test = calc_mol_weight(element_1)
                    print(test)
                elif data [1] == "?":
                    y2 = data
                    for fields in y2:
                        mass_2 = y2[0]
                        volume_2 = y2[1]
                        molarity_2 = y2[2]
                        element_2 = y2[3:]
                    #test_2 = calc_mol_weight(element_2)
                    #print (test_2)
                '''elif data [2] == "?":
                    y3 = data
                    for fields in y3:
                        mass_3 = y3[0]
                        volume_3 = y3[1]
                        molarity_3 = y3[2]'''







# Pass the lines to the correct functions for the calculations:
#   if '?' is the mass:
#       then solve the mass problem given volume, molarity and the elements
#   if '?' is the volume
#       then solve the volume problem given the mass, molarity and the elements
#   if '?' is the molarity
#         then solve the molarity problem given the mass, volume and the elements'''







