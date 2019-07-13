sales = [23, 32, 25]

print(sales[-1])

totalSales = 0
for sale in sales:
    totalSales = totalSales + sale

averageSales = totalSales / len(sales)

print('total sales   : ', totalSales)
print('average sales : ', averageSales)

multiplier = 2# int(input('Enter your multiplier: '))
nums = [52, 1, 34, 23, 18, -9, 21, 4, 79]

for num in nums:
    print(num * multiplier)

print()
print()
# Sequence and string operators:
print('Sequence and string operators:')


str1 = 'a string'
str2 = 'another string'

print('length of str1:', len(str1))
print('colin'[0])

# concatenation operator, +
print(sales + sales)
print(str1 + ' ' + str2)

# repition operator, *
print(sales * 3)
print(str1 * 5)

# slice operator, [int:int]
print(sales[1:-1])
print(str1[2:])

for character in str1:
    print(character)
    

print()
print()
# Encoding/Decoding of strings
print('Encoding/Decoding of strings')

# ord function returns the number represented by the string
print(ord('a'))
print(ord('\n'))

# chr function return the character represented by the number
print(chr(97))
print(chr(36))

print()
print()
# Splitting strings
header = 'Splitting strings'
print(header)
print(header.split('t'))
print(header.split(' '))
eat = 'eat, drink, be merry'
print(eat.split(', '))

print()
print()
header2 = '4.6 Manipulating Strings with Other String Methods'
print(header2)

# lower, upper, & casefold
print('lowercase:', header2.lower())
print('uppercase:', header2.upper())
print('casefold (language independent way to convert to lowercasae):', header2.casefold())

# strip, lstrip, rstrip
print(' test . '.strip())
print(' test . '.rstrip())
print('*'.join(eat.split(', ')))

# appending to a sequence
seq = []
seq.append('test')
print(seq)


print()
print()
header3 = '4.7 String Formatting'
print(header3)
testString = 'Hi {0}, your order {1} is being processed - thanks for your order, {0}'
print(testString)
print('formatted: ', testString.format('Colin', '9953'))

# number formatting
# width
# number of decimals
# fixed point
tempString = 'Temp is {0:0.5} degrees in F'
print(tempString.format(230/3))


print()
print()
print('4.8 File Input and Output')
# File process
#    1. Open file: function 'open'
#       - name
#       - mode: 'r', 'w'
#    2. Use the file (read, write, or append)
#       - read methods: read, readline, readlines
#       - write methods: print
#    3. Close the file: function 'close'

file = open('./test.txt', 'a')

#print(file.read())
#print(file.readline())
#print(file.readline())
#print(file.readlines()) # comment out the read and readline calls above

print('This is a second sentence', file=file)
file.close()
