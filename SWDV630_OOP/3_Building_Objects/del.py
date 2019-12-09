class DepClass:
    def __init__(self):
        print('DepClass initialized')

    def __del__(self):
        print('DepClass garbage collected')
        

class MyClass:
    def __init__(self):
        print('MyClass ininialized!')
        self.depClass = DepClass()

    def __del__(self):
        print('MyClass garbage collected!')


if __name__ == '__main__':
    myClass = MyClass()
    myClass = None # myClass gets garbage collected here
    print('this happened')
