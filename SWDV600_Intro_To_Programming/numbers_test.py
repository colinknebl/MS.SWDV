#def accumulate(x):
#    acc = x
#    accumulated = x
#    for i in range(acc - 1):
#        acc = acc - 1
#        accumulated = accumulated * (acc)
#    return accumulated
#
#result = accumulate(5)
#print('result', result)
#
#print(5 * 4 * 3 * 2 * 1)


numberOfScoops = int(input('How many scoops? '))
totalScoopOrderings = 1
for scoopChoicesLeft in range(numberOfScoops, 0, -1):
    totalScoopOrderings = totalScoopOrderings * scoopChoicesLeft
print('totalScoopOrderings', totalScoopOrderings)