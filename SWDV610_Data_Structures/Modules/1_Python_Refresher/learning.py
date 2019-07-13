def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k
            
f = factors(100)
#print(f)

#print(next(f))

x = 1 if False else 0

d = {
    'foo': 'bar',
    'baz': 'buz'
}

for k, v in d.items():
    print(k, v)
    
def printMe(msg):
    '''
        prints the passed in argument
        @param msg: any; The message to be printed
        @return None
    '''
    print('m', m)

p = printMe