#!/usr/bin/env python3
# Dave Magee, Vet Sciences Centre

## Placed this script under version control ## 
## To do this ran the following commands: 
	# cd python_scripts_dir
	# git init
	# git status
	# git add assignment_1.py
	# git commit assignment_1.py ## Use this command to commit later versions of the script
	# git config --global user.name "David Magee"

## Call the necessary modules from Python ###
import sys
import math


## Ensure that a python script and 2 arguments are entered on the command line, exit with usage message if not.

if len(sys.argv) != 3:
    print("{}: You must supply a filename for input and a filename for output".format(sys.argv[0]))
    sys.exit(-1)


#############################################################
### Function 1: Calculating the square of the hypotenuse ####
#############################################################

## 	In Function 1, two elements (termed here a and b) will be parsed to the function

def calcHypotenuse(a,b):
	funct1=(a**2)+(b**2)
	return(funct1)
	finish

################################################################
### Function 2: Find the 'hidden text' with a string of text ###
################################################################

##	Note: Five elements will be parsed to the function. The first four elements will be integers and will serve as the 
## 	coordinates that are needed to select the correct text in the 5th element. The 5th element is a string from which the
##	correct text will be selected. 
## 	Note: Need to add '1' to the coordinates defined in elements 'b' and 'd' as Python performs non-inclusive counting.

def calcCharacter(a,b,c,d,e):
	funct2=e[a:b+1]+(' ')+e[c:d+1]	## Add 1 to the 'b' and 'd' elements
	return(funct2)
	finish
	
##################################################################
### Function 3: RNA transcript sequence of a DNA coding strand ###	
##################################################################

##	A single element will be needed to be parsed to this function

def calcRNAtranscript(a):
	funct3=a.replace('T','U')
	return(funct3)
	finish

############################################################	
### Function 4: Nucleotide composition of a DNA sequence ###
############################################################

##	A single element will be needed to be parsed to this function

def calcNucleotideCounts(a):
	funct4=a.count("A"), a.count("C"), a.count("G"), a.count("T")
	return(funct4)
	finish
	
	
##########################################################################################	
###### Reading in data,  command line entries, outputting  results and and looping #######
##########################################################################################

##	The raw data required for this assignment are contained in the 'assignment1_input.txt' input file ##
## 	The output file containing the results is called 'assignment1_output.txt'
## 	On the command line, type: assignment_1.py assignment1_input.txt assignment1_output.txt
##	This script uses the sys.argv() function to run the script


## Begin by opening the file required for assignment 1

with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
 ## Define the input and output files on the command line using the sys.argv function
	
	for line in fin:
		line = line.rstrip()
		## Remove the new line character from the end of the string as do not want python to regard the newline (\n) as a
		## character in the string. 
    	## Will need to provide a newline (\n) in the write statements in the output files.


	## (1) Write the loop for the first part for the assignment	###
		if line=="##INI2":
		## parse through the input file checking for the string '##INI2' in the appropriate position
			line=fin.readline() ## Read in the next line after that appears after ##INI2.
			# print(line)	## Sanity check: Print this line to ensures that the code is reading in the
							## line directly below the line containing '##INI2'. 
							## The 'line' variable consists of a string containing two elements required for the hypotenuse ## calculation. 
			fields=line.split('\t')	## split the two elements in the 'line' variable'. 
			# print(fields) ## Sanity check: Print the 'fields' variable to check that the two elements have been split
			hypotenuse=calcHypotenuse(int(fields[0]),int(fields[1]))
			## parse the two elements in the 'fields' variable to the calcHypotenuse function above. Ensure that the elements ## are converted to integers. 
			
			# print(hypotenuse) # print the calculated square of the hypotenuse

			fout.write("##INI2 \n{} \n".format(hypotenuse))	
			## Write the results to the output file
	
	## (2) Begin the loop for the second part of the assignment ##
		if line=="##INI3":	
		## parse through the input file checking for the string '##INI3' in the appropriate position
			line_2=fin.readline()	## read in the next line after that appears after '##INI3' and store in a variable
									## called 'line_2
			
			line_2=line_2.split('\t')
			#print(line_2) 	## Sanity check: Print this line to ensures that the code is reading in the
							## line directly below the line containing '##INI3'. 
							
			Character=calcCharacter(int(line_2[0]),int(line_2[1]),int(line_2[2]),int(line_2[3]),(line_2[4]))
			## parse the 0th, 1st, 2nd, 3rd and 4th elements from this split line to the calcCharacter function defined above
			## NB. Python starts counting from the 0th element.
			## The 0th-3rd elements need to be converted to integers
			## The 4th element remains a string
			## Store the result in a variable called 'Character'
			
			# print(Character)	## Sanity check to see that the code is printing the correct solution.
			
			fout.write("##INI3 \n{}\n".format(Character))
			## Write the results to the output file

	## (3) Begin the loop for the third part of the assignment ##
		if line=="##RNA":	
		## parse through the input file checking for the string '##RNA' in the appropriate position
			RNA=fin.readline()	## read in the next line after that appears after '##RNA' and store in a variable
								## called 'RNA'	
			RNA_1=RNA.strip()	## Remove the redundant white space at the end of the line in the RNA variable and store in a 
								## new variable called RNA_1
			#print(RNA_1)	## Sanity check to see that the code is reading in the correct lines
			
			RNAsequence=calcRNAtranscript(str(RNA_1)) ## Convert 
			## Parse the sequence in the RNA variable to the calcRNAtranscript function defined above
			## Store the result in a variable called RNAsequence
			
			#print(RNAsequence) ## Sanity check to see that the code is printing the correct solution
			
			fout.write("##RNA \n{}\n".format(RNAsequence))
			## Write the results to the output file
	
	## (4) Begin the loop for the fourth part of the assignment ##
		if line=="##DNA":
		## parse through the input file checking for the string '##DNA' in the appropriate position
			DNA=fin.readline()	## read in the next line after that appears after '##DNA' and store in a variable
								## called 'DNA'
								
			# print(DNA)	## Sanity check to see that the code is reading in the correct lines
			
			DNAcounts=calcNucleotideCounts(DNA)	## parse the DNA variable to the calcNucleotideCounts function defined above
			
			# print(DNAcounts)	## Sanity check to see that the code is printing the correct solution
			
			fout.write("##DNA\nNumber of A={} Number of C={} Number of G={} Number of T={}\n".format(DNAcounts[0],DNAcounts[1],DNAcounts[2],DNAcounts[3]))
			## Write the results to the output file
			      
	else:
            next  # do nothing if line does not contain INI2, INI3, RNA or DNA
sys.exit(0)