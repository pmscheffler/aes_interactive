import sys
from typing import List
from util_functions import toHex, toStr
from argparse import ArgumentParser

# we will need a series of keys for the example
# 128B          1234567890ABCDEF
myAESkey = "My 128b AES _key"
#myHexKey = ''.join(str(ord(c)) for c in myAESkey)

#TODO: need to open and read the file passed in by --file or -f
#TODO: need to handle more than 128B (text is hardcoded for 9 rounds/128B)

parser = ArgumentParser()

parser.add_argument("-m", "--message", help="The message to be enciphered", 
                    type=str, default="This is the default message to be enciphered")
parser.add_argument("-k", "--mykey", help="This is your key, the first 16 characters will be used", 
                    type=str, default=myAESkey)
parser.add_argument("-d", "--decode", help="Set to 1 if you want to decode an enciphered string", default=0)

parser.add_argument("-f", "--file", help="Open a file to encipher or decipher * ASCII please")



def readSBoxData() -> []:
    # we can define the substitution box here
    sbox = []
    with open("sbox.txt", "r") as sboxFile:
        i = 0
        for line in sboxFile:
            curLine = line.split()
            for itm in curLine:
                sbox.append(itm)
                i += 1

        sboxFile.close()
    
    return sbox

def runSBox(sbox, message) -> str:
    for elem in message:
        # covert each character in the passed message thru the substitution box
        print(elem, "(", ord(elem), ")", "=>", sbox[ord(elem)])


def main(args: List[str]) -> None:

    commandArgs = parser.parse_args()

    myAESkey = commandArgs.mykey

    if commandArgs.decode == 1:
        print("\nWe will decode the message\n\n")
    else:
        print("\nWe will encipher this message\n\n")

    if len(myAESkey) < 16:
        print("Your key is not secure enough, please retry")
        sys.exit()

    if len(myAESkey) > 16:
        myAESkey = myAESkey[:16]

    myHexKey = toHex(myAESkey)
    
    print("myAESKey: ", myAESkey , ": Length: ", len(myAESkey))
    print("myHexKey: ", myHexKey , ": Length: ", len(myHexKey))
    print("Plain Text: ", commandArgs.message, "\n")    

    print("First we will generate our ROUND CIPHERS\n")

    print("Round 1: This is the key broken into 4 chunks\n")

    sbox_data = readSBoxData()

    runSBox(sbox_data, commandArgs.message)





if __name__ == "__main__":
    print("\n\n\n\nThis is a working example of how AES operates\nThis will cycle through the necessary\nrounds to (de/en)cipher"
            " your message with the supplied key\nusing ",
            "the 128bit AES encryption algorithm\n\nPeter Scheffler \nIn Covid-19 Quarantine March 2020\n\n\n")
    main(sys.argv[1:])    

