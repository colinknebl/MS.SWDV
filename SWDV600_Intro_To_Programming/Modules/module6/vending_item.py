

class VendingItem():
    """
        A Class for a vending machine item.
    """
    a = 1
    def __repr__(self):
        #return self.__dict__
        return '{}; VendingItem instance, {}'.format(self.name, self.__dict__)
    
    def __init__(self, name):
        self.name = name
        
        

def main():
    item = VendingItem('Gatorade')
    print(item)
    #help(VendingItem)
    
if __name__ == '__main__':
    main()