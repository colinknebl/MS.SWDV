# vending_status_checker.py
#
# A program called vending_status_checker that will read and
#   report on the status of three vending machines' status
#   as given in JSON data files.
# The report is sortable based on the user's choice:
#   item name, sold %, or stocking needs.
# Can also produce an inventory report with percent sold and
#   sales data

import json
from vending_machine import VendingMachine, VendingMachineMgr

def mainLoop(vendingMachineMgr, sortDict):
    
    while True:
        userInput = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
        
        if userInput == 'q':
            break
        elif userInput in sortDict:
            vendingMachineMgr.sortBy(sortDict[userInput])
        else:
            print('Please enter a valid character.')

def main():

    SORT_DICTIONARY = {
        'n': 'item_name',
        'p': 'percent_sold',
        's': 'stock_required'
    }
    
    vendingMachineFileNames = [
        './REID_1F_20171004.json',
        './REID_2F_20171004.json',
        './REID_3F_20171004.json'
    ]
    vendingMachines = []
    
    for fileName in vendingMachineFileNames:
        jsonFile = open(fileName, 'r')
        machineData = json.loads(jsonFile.read())
        vendingMachines.append(VendingMachine(machineData))
    
    vendingMachineMgr = VendingMachineMgr(vendingMachines, SORT_DICTIONARY)

    reportType = input('Would you like the (m)achine report or the (i)nventory report? ')

    if reportType == 'i':
        mainLoop(vendingMachineMgr, SORT_DICTIONARY)
    else:
        vendingMachineMgr.printInventory()

if __name__ == '__main__':
    main()