# caesar-encrypter.py
#
# This program will have a user input a message,
#   a shift key, and an output file name.
#   It will then use a Caesar cipher to encrypt
#   the message and write the encrypted message
#   out to the output file.

def main():
    # get user message input (message)
    message = input('Enter the message to encrypt: ')
    # get user specified shift key (shiftKey)
    shiftKey = int(input('Enter the shift key: '))
    # get output file name (outFileName)
    outFileName = input('Enter the output file name: ')
    
    # shift the alphabet by slicing the alphabet sequence
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    shiftedAlphabet = alphabet[len(alphabet) - shiftKey:] + alphabet[:len(alphabet) - shiftKey]
    
    #print(alphabet)
    #print(shiftedAlphabet)
    
    # initialize accumulator (encryptedMessageSeq) as empty sequence
    encryptedMessageStr = ''
    
    # for each character in message
    for ch in message:
        # find the index of ch in alphabet
        plainTextCharaIndex = alphabet.find(ch)
        encryptedChara = shiftedAlphabet[plainTextCharaIndex]
        # concatenate that letter to encryptedMessageStr
        encryptedMessageStr = encryptedMessageStr + encryptedChara
        # print('{0} -> {1}'.format(ch, encryptedChara))
        
    #print(encryptedMessageStr)
    
    # open user specified output file (outFileName) in write mode
    outFile = open(outFileName, 'w')
    
    # write the encryptedMessageStr to the outFile
    print(encryptedMessageStr, file=outFile)
    
    # close outFile
    outFile.close()
    
    print()
    print('The encrypted message is: {0}'.format(encryptedMessageStr))
    print('Done writing message to {0}'.format(outFileName))


main()