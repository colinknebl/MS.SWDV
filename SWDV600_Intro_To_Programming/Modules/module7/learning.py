def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n -1)
    
#fact(3)
    
    
def returnFunc():
    var = 'can you see me?'
    
    def returnedFunc(v):
        print('var:', var)
        print('v:', v)
    
    return returnedFunc