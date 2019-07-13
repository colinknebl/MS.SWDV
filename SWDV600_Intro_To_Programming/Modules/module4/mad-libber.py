# mad-libber.py
#
# A program that creates a mad lib

def main():
    print('Madlib Maker')
    
    
    def printTwinkle(punctuation):
        print('{0}, {0} little {1}, how I {2} what you are{3}'.format(adjective, noun, verb, punctuation))
    
    noun = input('thing: ')
    place = input('place: ')
    adjective = input('adjective: ')
    verb = input('verb: ')
    verb2 = input('another verb: ')
    
    print()
    
    printTwinkle('.')
    print('Up above the world so high, like a diamond in the {0}.'.format(place))
    printTwinkle('!')
    print('When the {0} sun is gone, when there\'s nothing he {1} upon...'.format(adjective, verb2))
    
main()