# accept user phrase input
userInput = input('Input your phrase: ')

# accept # of repetitions
repeat = int(input('How many times should it be repeated? '))

for i in range(repeat):
    print(str(i + 1) + ' ' + userInput)