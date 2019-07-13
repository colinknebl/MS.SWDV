import learning_import as li

print('name in learning', __name__)

def getNum():
    return int(input('number:'))

try:
#    valid = False
#    while not valid:
#        try: 
#            val = getNum()
#            valid = True
#            print('you entered {0}'.format(val))
#        except ValueError:
#            print('please enter a valid number')
            
    # sentinel loop
    # while the inputValue != sentinel
    # proceed with loop
    
    
    # validation loop
    while True:
        newPass = input('enter your new password: ')
        if len(newPass) >= 12:
            confirm = input('confirm your new password: ')
            if confirm == newPass:
                print('Your new password is', confirm)
                break
            else:
                print('your passwords did not match. please enter your new password')
        else:
            print('password must be at least 12 characters long')

except:
    print('Uh oh! An error occured!')