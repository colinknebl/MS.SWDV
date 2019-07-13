# sales-invoice-finder.py
#
# A program to find sales information based on
#  invoice identifier (id) or customer's last name (lname)

def main():
    # get search by key
    searchKey = None
    while True:
        searchKey = input('Search by invoice id (id) or customer last name (lname)? ')
        if searchKey == 'id' or searchKey == 'lname':
            break
        else:
            print("ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search")
    
    searchTerm = input('Enter your search term: ')
    
    # open file
    salesFile = open('sales_data.csv', 'r')
    # skip over the column header line
    salesFile.readline()
    
    # initialize the number of records
    numOfMatchedRecords = 0
    
    for line in salesFile:
        lineTokens = line.strip().split(',')
        
        targetColumn = 2 # default is lname column
        if searchKey == 'id':
            targetColumn = 0
        
        if lineTokens[targetColumn] == searchTerm:
            print(line.strip())
            numOfMatchedRecords += 1
    
    print('{} records found.'.format(numOfMatchedRecords))
    
    # close file
    salesFile.close()

main()