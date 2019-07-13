class RowSlot:
    
    def __repr__(self):
        return '{} instance of RowSlot'.format(self.__item_name)
    
    def __init__(self, data):
        # self.slot_number = data['slot_number']
        self.__item_name = data['item_name']
        self.__item_price = data['item_price']
        self.__last_stock = data['last_stock']
        self.__current_stock = data['current_stock']
        self.__current_deficit = 8 - self.__current_stock
        self.__amount_sold_since_last_stock = self.__last_stock - self.__current_stock
        self.__total_sold_dollars = self.__amount_sold_since_last_stock * self.__item_price
    
    def getTotalSold(self):
        return self.__total_sold_dollars

    def getAmountSold(self):
        return self.__amount_sold_since_last_stock

    def getName(self):
        return self.__item_name

    def getLastStock(self):
        return self.__last_stock

    def getCurrentStock(self):
        return self.__current_stock

    def getPrice(self):
        return self.__item_price
    
    def getDetails(self):
        return {
            'last_stock': self.__last_stock,
            'current_stock': self.__current_stock,
        }


class VMRow:
    
    def __repr__(self):
        return '{} instance of VMRow'.format(self.__row)
    
    def __init__(self, data):
        self.__row = data['row']
        self.__slots = []
        
        for slotDataDict in data['slots']:
            self.__slots.append(RowSlot(slotDataDict))
    
    def getSlots(self):
        return self.__slots
        

class VendingMachine:
    
    def __repr__(self):
        return '{} instance of VendingMachine'.format(self.__machine_id)
    
    def __init__(self, data):
        #  one row can hold up to 72 beverages
        self.__machine_id = data['machine_id']
        self.__machine_label = data['machine_label']
        self.__contents = []
        
        for contentDict in data['contents']:
            rowData = {}
            for key in contentDict:
                rowData[key] = contentDict[key]
            
            self.__contents.append(VMRow(rowData))
        
        self.__currentStock = self.__calculateStock()
        percentSold, salesTotal = self.__calculateCurrentInventory()
        self.__percent_sold_since_last_stock = percentSold
        self.__total_sales_since_last_stock = salesTotal
    
    def getContents(self):
        return self.__contents

    def getLabel(self):
        return self.__machine_label

    def getInventoryData(self):
        return self.__percent_sold_since_last_stock, self.__total_sales_since_last_stock

    def __calculateStock(self):
        currentStock = 0
        for row in self.__contents:
            for slot in row.getSlots():
                currentStock += slot.getCurrentStock()
        return currentStock

    def __calculateCurrentInventory(self):
        """Calculates the current inventory of the vending machine."""
        amountSold = 0
        amountStocked = 0
        salesTotal = 0.0
        for row in self.__contents:
            for slot in row.getSlots():
                amountStockedInSlot = slot.getLastStock()
                amountStocked += amountStockedInSlot

                numberSoldInSlot = slot.getAmountSold()
                amountSold += numberSoldInSlot

                salesTotal += slot.getTotalSold()
        
        percentSold = (amountSold / amountStocked) * 100
        return percentSold, salesTotal


class VendingMachineMgr:
    """
    A class to perfrom calculations on the managed Vending machines.
    """
    
    def __init__(self, machines, sortDict):
        self.__machines = machines
    
    def printInventory(self):
        "Prints our the inventory data of the managed machines."
        print('{}\t\t{}\t{}'.format('Label', 'Pct Sold', 'Sales Total'))
        machineDataDict = self.__getMachineInventoryData()
        for machineLabel in machineDataDict:
            percentSold = machineDataDict[machineLabel]['percent_sold']
            totalSales = machineDataDict[machineLabel]['sales_total']
            print('{0}\t\t{1:0.2f}%\t\t${2:8.2f}'.format(machineLabel, percentSold, totalSales))

    def __getMachineInventoryData(self):
        "Creates a dictionary of machine data for the inventory."
        machineInventoryDict = {}

        for machine in self.__machines:
            percentSold, salesTotal = machine.getInventoryData()
            machineInventoryDict[machine.getLabel()] = {
                'percent_sold': percentSold,
                'sales_total': salesTotal
            }
        return machineInventoryDict
        
    def sortBy(self, sortBy):
        "Handles a sort request."
        contentDict = self.__calculateStockNeeds(self.__getMachineData())
        sortedData = self.__sortData(contentDict, sortBy)
        self.__printData(sortedData)

    def __getMachineData(self):
        "Adds the vending machine data to a dictionary."
        contentDict = {}

        for machine in self.__machines:
            for content in machine.getContents():
                for slot in content.getSlots():
                    slotDetails = slot.getDetails()
                    slotName = slot.getName()

                    if slotName in contentDict:
                        for key in contentDict[slotName]:
                            if key == 'number_of_slots':
                                contentDict[slotName]['number_of_slots'] += 1
                            else:
                                contentDict[slotName][key] += slotDetails[key]
                    else:
                        contentDict[slotName] = slotDetails
                        contentDict[slotName]['number_of_slots'] = 1
        
        return contentDict

    def __calculateStockNeeds(self, contentDict):
        "Calculates the number of items required to fill the item's stock to full capacity."
        for itemName in contentDict:
            item = contentDict[itemName]
            totalStockCapacity = item['number_of_slots'] * 8
            item['stock_required'] = totalStockCapacity - item['current_stock']

            numSold = item['last_stock'] - item['current_stock']
            item['number_sold'] = numSold

            percentSold = numSold / item['last_stock']
            item['percent_sold'] = percentSold * 100

            del item['last_stock']
            del item['number_of_slots']
        
        return contentDict

    def __sortData(self, data, sortBy):
        "Sorts the Vending Machine data."

        def sortByKey(item):
            return item[sortBy]

        if sortBy == 'item_name':
            reverseSort = False
        else:
            reverseSort = True
           
        reformatted = self.__reformatData(data)
        reformatted.sort(key=sortByKey, reverse=reverseSort)

        return reformatted

    def __reformatData(self, data):
        "Takes the dictionary of contents to a sequence for easier sorting."
        reformatted = []
        
        for itemName in data:
            newItem = {}
            newItem['item_name'] = itemName
            for key in data[itemName]:
                newItem[key] = data[itemName][key]
            reformatted.append(newItem)
        return reformatted

    def __printData(self, sortedVendingContents):
        "prints the data to the console."
        print('\n{0:21}{1:8}{2:10}{3:10}{4:12}'.format('Item Name', 'Sold', '% Sold', 'In Stock', ' Stock needs'))
        for listItem in sortedVendingContents:
            print('{0:21}{1:7}{2:9.2f}%{3:8}{4:11}'.format(listItem['item_name'], listItem['number_sold'], listItem['percent_sold'], listItem['current_stock'], listItem['stock_required']))
        print('\n')
