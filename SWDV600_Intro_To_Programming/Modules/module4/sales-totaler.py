# sales-totaler.py
#
# A program that takes some sales numbers from a file
#   written as dollars (e.g., $1120.47), sums them
#   across rows, and outputs the rows again with the sum at the end.

def main():
    # get the input file (inputFileName)
    inputFileName = input('Enter sales file name: ')
    
    # get the output file (outputFileName)
    outputFileName = input('Enter name for total sales file: ')
    
    # open the files
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')
    
    for line in inputFile:
        # remove the white space
        line = line.strip()
        amt1, amt2 = line.split()
        amt1 = float(amt1[1:])
        amt2 = float(amt2[1:])
        print('${0:8.2f}  ${1:8.2f}  ${2:8.2f}'.format(amt1, amt2, amt1 + amt2), file=outputFile)
    
    # close the files
    inputFile.close()
    outputFile.close()
    
    # print end message
    print('\nDone writing totals to {0}'.format(outputFileName))
    
main()