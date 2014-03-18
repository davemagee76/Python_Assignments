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


# define a function that calculates the molecular weight of the compounds in the list given
# the list of atoms, their respective number of atoms in the compound and their respective molecular weights
# for this, will generate a dictionary from the list of elements defined below in the code

# For each element pair in the ion list, place the first element (ion ID) as the key and the second element
# (ion molecular weight)as the value


# Define a function that generates a new dictionary (called mol_dict) from the lists in the ions variable
def generate_mol_dict(ions):
    mol_dict = {}
    # each list in the ions variable consists of pairs of elements (ion ID; ion mol weight)
    # each list in ions has a length of even number
    # divide the range of the length of each list by 2, so that the loop will perform the function for each pair
    # i refers to the indices in the lists of the ions variable
    # loop through each list in the ions variable; for each pair of elements assign the first element to a variable called
    # 'key' and the second variable called 'value'
    # return the mol_dict
    # This will generate (dynamically) a new dictionary called mol_dict from the list of elements in the ions variable
    for i in range(len(ions) // 2):
        key = ions[2 * i]
        value = ions[2 * i + 1]
        mol_dict[key] = int(value)  # assign to each key the corresponding molecular weight (convert to an integer)
    return mol_dict


# Define a function that calculates the molecular weight of each molecule in the mol_dict dictionary
# This dictionary will call the keys and values assigned in the mass_dict dictionary
def calc_compound_mol_weight(mol_dict):
    mol_weight = 0  # before adding to the mol_weight variable, initialise it to zero
    for ion in list(mol_dict.keys()):  # convert the dictionary keys to a list. list(dict.keys()) is a python function
        mol_weight += int(mol_dict[ion]) * int(mass_dict[ion])  # sum
        #print(int(mol_dict[ion])) # the integer values from the mol_dict dictionary (i.e. no. of ions)
        #print(int(mass_dict[ion])) # the integer values from the mass_dict dictionary (i.e. mol weight of each ion)
    return (mol_weight)


# Define a function that solves mass given volume, molarity and the compound molecular weight
# mass equals volume*molarity*sum(molecular weight*no. of atoms) for each element in compound
def calc_mass(data):
    for field in data:
        grams = (float(volume) / 1000) * float(molarity) * int(compound_mol_weight)
    return grams


# Define a function that solves volume given mass, molarity and the compound molecular weight
# volume equals ((mass/molecular weight)/molarity)
def calc_vol(data):
    for field in data:
        volume = (int(mass) / int(compound_mol_weight)) / float(molarity)
    return volume

# Define a function that solves molarity given mass, volume and the compound molecular weight
# molarity equals ((mass/molecular weight)/volume)
def calc_mol(data):
    for field in data:
        molarity = (int(mass) / int(compound_mol_weight)) / (int(volume)/1000)
    return molarity

# Process the input file to perform the calculations:
# Read in the file from the command line and write to an outfile
with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
    # For each line in input file:
    for line in fin:
        #   strip the line (returns string for the current line)
        data = line.strip()
        #   split the line (returns a list for the current line)
        data = data.split('\t')
        #print(data)

        #   Sanity check:
        # the length of each list in the data variable should be an odd number
        # if the length of the each line from the input file is not an even number:
        # return an error message and stop the script
        # else proceed with the script
        if len(data) % 2 == 0:
            print("expect length of the lists should be an odd number: mass, vol, mol, elements in pairs")
            sys.exit(2)
        else:
            pass

        # Select only those lines in the input file that contain a "?"
        if "?" in data:
            # define the elements in the data variable
            mass = data[0]
            volume = data[1]
            molarity = data[2]
            ions = data[3:]
            #print(mass)

            # Need molecular weights for the calculations:
            # Generate a dictionary from the ions variable by passing the elements to the generate_mol_dict function
            mol_dict = generate_mol_dict(ions)
            #print(mol_dict)
            # Calculate the molecular weights for each compound in the mol_dict dictionary using
            # the calc_compound_mol_weight
            compound_mol_weight = calc_compound_mol_weight(mol_dict)
            # print(compound_mol_weight)

    # Solve for mass
            if mass == "?":
                grams = calc_mass(data)
                # print(grams)
                fout.write("mass in grams \n{}\n".format(grams))
    #Solve for volume
            if volume == "?":
                volume = calc_vol(data)
                # print(volume)
                #fout.write("volume in litres \n{}\n".format(volume))
    #Solve for molarity
            if molarity == "?":
                molarity = calc_mol(data)
                #print(molarity)
                #fout.write("molarity \n{}\n".format(volume))
