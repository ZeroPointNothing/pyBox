"""
Password generator.
"""
import random
import sys
from time import sleep
sys.dont_write_bytecode = True
try:
    import py_pgs
except ModuleNotFoundError: ## If pyPgs.py does not exist, catch the exception and print instead.
    print('Unable to find required script modules. Please verify they exist.')
    sleep(3)
    quit()

##words that can be used for the beginning portion of the password.
word_start = [
    "stupendous_",
    "superb_",
    "strange_",
    "exotic_",
    "interesting_",
    "stunning_"
]
##words that can be used for the end portion of the password.
word_end = [
    "bread",
    "chickn",
    "pizza",
    "cheese",
    "tornado",
    "house",
    "kitchen",
    "butters",
]


def pass_word():
    """
    Creates five passwords using combinations of words, four random numbers,
    three exclaimation marks, and a random capital letter.
    """
    py_pgs.cls()
    print ("Creating Five Passwords...")
    sleep(3)
    print()
    passnum=0
    for _ in range(0,5):
        start = random.choice(word_start) #Chooses a random value from the list.
        end = random.choice(word_end)
        num = "".join(random.sample("1234567894254936747", 4)) #Grabs characters randomly.
        char = "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1))
        output = start + end + '!!!' + num + char
        passnum=passnum+1
        print("Generated Password", passnum, ": ")
        print(output)
        print()
        sleep(0.5)
    dummyvar = input("Press ENTER to Continue...")





##script begin -
print("Enter password type.")
pass_type = input('> ')
pass_word()












#
#Old password gen.
#
###Generate password.
### hey, ma! Look! I can code!
##
###import string
##import random
##import sys
##from threading import Event
##import os
##
##os.system("title Password Generator")
##
##print("What kind of password would you like?")
##pass_type = int(input("1.) string 2.) word : "))
##
##if pass_type == 1:
##    pyPgs.cls()
##    pass_length = int(input("Enter Password Length:  "))
##    if pass_length < 0:
##        print()
##        print("Password Password length cannot be Negative!")
##        sleep(2)
##        sys.exit()
##
##    if pass_length==0:
##        print()
##        print("Please input a value.")
##        sleep(2)
##        sys.exit()
##
##    if pass_length > 150:
##        print()
##        print("Too Long! (Why are you even trying to make a password this long?)")
##        sleep(2)
##        sys.exit()
##
##    print ("Creating Five Passwords...")
##    sleep(3)
##    print()
##    passnum = 0
##
##
##    ##Creates the password.
##    for i in range(0,5):
##        ##Characters that can appear in the password.
##        ##The more of one that exists, the more common it will be.
##        LOWER_CASE = "aaabbccddddefghiiijkllllmnoooopppqrrrrstuuuvwxxxxyz"
##        UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##        NUMBER = "123456789873458734587634567834867678"
##        SYMBOLS = "!*$!!!!!*****%%%%*****$$$$$$!!!!!~~~__~~~____"
##        ##Combines the possible characters.
##        USE_FOR = SYMBOLS + LOWER_CASE + UPPER_CASE + NUMBER
##        ##Takes the Use_for variable and randomly selects characters to keep
##        ##with the max amount determined by pass_length
##        password = "".join(random.sample(USE_FOR, pass_length))
##        passnum=passnum+1
##        print ("Password" ,passnum ,": ")
##        print (password)
##        print()
##        sleep(0.5)
##    dummyvar = input("Press ENTER to close ")
##    sys.exit()
##
##if pass_type == 2:
##    pyPgs.cls()
##    print ("Creating Five Passwords...")
##    sleep(3)
##    print()
##    passnum=0
##    for i in range(0,5):
##        input1 = ["stupendous_", "superb_", "strange_", "exotic_", "interesting_", "stunning_"]
##        output1 = random.choice(input1) #Chooses a random value from the list.
##        input2 = ["bread", "chickn", "pizza", "cheese", "tornado", "house", "kitchen"]
##        output2 = random.choice(input2)
##        input3 = ("1234567894254936747")
##        output3 = "".join(random.sample(input3, 4)) #Grabs characters randomly from the variable.
##        input5 = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##        output5 = "".join(random.sample(input5, 1))
##        output4 = ("!!!")
##        output6 = output1 + output2 + output4 + output3 + output5
##        passnum=passnum+1
##        print("Generated Password", passnum, ": ")
##        print(output6)
##        print()
##        sleep(0.5)
##    dummyvar = input("Press ENTER to Continue...")
##else:
##    print("Invalid Response")
