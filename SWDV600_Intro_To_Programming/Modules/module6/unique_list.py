# unique_list.py
#
# Compares values in a sequence for any duplicates

def getInput(text):
	return int(input(text))

def isSeqUnique(seq, userInput):
	if seq.count(userInput) > 1:
		return False
	else:
		return True

def main():
	print('This program tests if the sequence of positive numbers you input are unique')
	print('Enter -1 to quit')

	userInput = getInput('Enter the first number: ')
	seq = []
	isUnique = True

	while userInput != -1:

		seq.append(userInput)
		if isUnique == True:
			isUnique = isSeqUnique(seq, userInput)

		userInput = getInput('Next: ')

	if isUnique:
		negativeText = ''
	else:
		negativeText = ' NOT'
		
	print('The sequence {0} is{1} unique!'.format(seq, negativeText))

main()