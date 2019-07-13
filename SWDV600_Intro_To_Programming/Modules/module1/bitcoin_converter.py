# converts bitcoin to dollars (usd)

# output date and time conversion rate for bitcoins was recorded
print('As of 5/9/19 at 8:11 pm, bitcoin is currently trading at $6160 per bitcoin.')

# get user input of bitcoin
bitcoinAmount = float(input('Enter the bitcoin amount: '))

convertedAmount = int(bitcoinAmount * 6160)

# output the value of the input amount in dollars
# That is worth 1043 us dollars.
print ('That is worth ' + str(convertedAmount) + ' us dollars')
