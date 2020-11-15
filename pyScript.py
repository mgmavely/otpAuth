import random
import twilVar
import string

#Uses for loop to generate random 8-digit verification code and returns
def otpGenerator():
    listLower = list(string.ascii_lowercase)
    listUpper = list(string.ascii_uppercase)
    listNum = []
    for i in range(10):
        listNum.append(str(i))
        
    superList = listLower + listUpper +listNum
    retVal = "";
    
    for i in range(5):
        randVal = superList[random.randint(0,len(superList))]
        retVal += randVal
    return retVal

#Function that sends message given user inputted number and random password
def messageSend(inpNum, password):
    message = twilVar.client.messages.create(
        body="Your verification password is: " + str(password),
        from_=twilVar.twilNum,
        to='+' + str(inpNum)
        )

#Function that validates proper phone number entry
def phoneNumValidate():
    retVal = input('Enter your phone number (with area code i.e Canada [1])\n+')
    return retVal

#Function that verifies the user has entered the random generated password
#received via SMS
def authValidate():
    while True:
        inp = input('Enter the verification code: \n')
        if inp == str(password):
            print('Success!\n')
            break
        else:
            print('Invalid password, try again!\n')
                

password = otpGenerator()
inputNumber = phoneNumValidate()
messageSend(inputNumber, password)
authValidate()


        
            
