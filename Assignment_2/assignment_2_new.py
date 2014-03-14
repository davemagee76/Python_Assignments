#!/usr/bin/env python3

__author__ = 'David Magee'

import sys

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


# define the function that calculates the mass of the compounds in the list given the list of atoms, their respective
# number of atoms in the compound and their respective molecular weights

# mass_compound equal to sum (no. atoms*molecular weight) for each element in the compound
# Hard coded a dictionary for the mass of the elements
massDict = {'H':1, 'Cl':35, 'Na':23,'C':12, 'O':16,'S':32,'Mg':24,'Ca':40,'Ag':108,'N':14}



# define the function that solves mass given volume, molarity and the elements
#def calc_mass(volume, molarity, elements):
#   mass equals volume*molarity*sum(molecular weight*no. of atoms) for each element in compound
    # mass = volume*molarity*()


# Process the input file to perform the calculations:
# Read in the file





# For each line in input file:
#   strip the line (returns string for the current line)
#   split the line (returns a list for the current line)
#   Sanity check:
#   if the length of the each line from the input file is not an even number:
#     return an error message and stop the script:
#   else keep processing the list
#   the 0th element of the list is the mass
#   the 1st element of the list is the volume
#   the 2nd element of the list is the molarity
#   the other elements that follow are the chemical elements (consisting of a pair of element name and no. of atoms)

# Pass the lines to the correct functions for the calculations:
#   if '?' is the mass:
#       then solve the mass problem given volume, molarity and the elements
#   if '?' is the volume
#       then solve the volume problem given the mass, molarity and the elements
#   if '?' is the molarity
#         then solve the molarity problem given the mass, volume and the elements







