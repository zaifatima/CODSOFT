import string
import random 
l= int(input("Enter password length: ")) 
print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''') 
characterList = ""
while(True):
    ch = int(input("Pick a number "))
    if(ch == 1):         
        characterList += string.ascii_letters
        break
    elif(ch == 2):
        characterList += string.digits
        break
    elif(ch == 3):         
        characterList += string.punctuation
        break
    elif(ch == 4):
        break
    else:
        print("Please pick a valid option!") 
password = [] 
for i in range(l):   
    randomchar = random.choice(characterList)    
    password.append(randomchar)
print("The random password is " + "".join(password))
