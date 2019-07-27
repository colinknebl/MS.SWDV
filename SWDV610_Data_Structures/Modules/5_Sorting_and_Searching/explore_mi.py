# What is the difference between a list and a dictionary?
#    lists based on position; indexed starting at 0
#    dictionaries based on keys


# How are they coded differently and what different implementations they have?
#    lists use brackets: []
#    dictionaries use curly braces: {}

# Build a script that utilizes at least one list and one dictionary.

miAirports = {
    'BTL': 'Battlecreek',
    'DTW': 'Detroit Metropolitan Airport',
    'DET': 'Detroit',
    'FNT': 'Flint',
    'GRR': 'Grand Rapids',
    'AZO': 'Kalamazoo-Battle Creek International Airport',
    'LAN': 'Lansing',
    'MBS': 'Saginaw'
}


def get_airport():
    # ask question
    print('Which airport will you be flying in at? ')
    i = 0

    # print out each airport code
    for k in miAirports:
        end = ', ' if i < len(miAirports) - 1 else ''
        print(k, end=end)
        i += 1

    # get user input
    valid = False
    code = None
    while not valid:
        code = input('\nEnter Airport code: ').upper()
        if code in miAirports:
            valid = True
        else:
            print('Airport code invalid, try again')
    return code


def main():
    print('Let\'s explore Michigan!\n')

    code = get_airport()

    numOfPassengers = int(input('How many passengers are flying? '))
    passengers = []

    for i in range(numOfPassengers):
        passengers.append(input('What is the name of passenger {}? '.format(i + 1)))

    print()
    print('The airport name is: ', miAirports[code])
    print('passengers: ', passengers)

if __name__ == '__main__':
    main()