# caesar-decrypter.py
#
# This program will have the user provide a file name
#   for a file that contains an encrypted message, and
#   also the shift key necessary to decrypt that message.
#   It will then use the Caesar cipher to decrypt the
#   message and write it out to the shell.

def main():
    # get input file name (inFileName)
    inFileName = input('Enter the name of the file with the encrypted message: ')
    
    # get the shift amount (shiftKey)
    shiftKey = int(input('Enter the decryption key (shift amount): '))
    
    # get the message from the input file
    inputFile = open(inFileName, 'r')
    message = inputFile.read()
    message = message.strip()
    inputFile.close()
    
    # shift the alphabet by slicing the alphabet sequence
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    shiftedAlphabet = alphabet[len(alphabet) - shiftKey:] + alphabet[:len(alphabet) - shiftKey]
    
    # initialize accumulator (decryptedMsgStr) as empty string
    decryptedMsgSeq = []
    
    # for each character in message
    for ch in message:
        encryptedCharaIndex = shiftedAlphabet.find(ch)
        decryptedChara = alphabet[encryptedCharaIndex]
        decryptedMsgSeq.append(decryptedChara)
        
    print('\nThe message is:', ''.join(decryptedMsgSeq))
    
main()