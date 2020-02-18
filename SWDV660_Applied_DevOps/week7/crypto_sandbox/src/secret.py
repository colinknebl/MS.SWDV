import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

chunkSize = 64*1024

def encrypt(key, filename):
    outputFileName = "(encrypted)" + filename
    fileSize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFileName, 'wb') as outfile:
            outfile.write(fileSize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunkSize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    outputFileName = filename[11:] # removes the "(encrypted)"

    with open(filename, 'rb') as infile:
        fileSize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFileName, 'wb') as outfile:
            while True:
                chunk = infile.read(chunkSize)
                
                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            
            outfile.truncate(fileSize)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()


def main():
    choice = str(raw_input('Would you like to (E)ncrypt or (D)ecrypt?: '))

    if choice != 'E' and choice != 'D':
        print('Invalid selecting. Closing program...')
        exit(1)
    
    filename = raw_input('File name: ')
    password = getKey(raw_input('Password: '))

    if choice == 'E':
        encrypt(password, filename)
    else:
        decrypt(password, filename)

    print('Done.')

if __name__ == '__main__':
    main()
