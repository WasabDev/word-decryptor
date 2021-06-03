import string
letter = string.ascii_letters
blacklist = ["&","(",")","-","_","~","#","{","}","[","]","|","`","^","@","¨","¤","£","$","%","µ","*","!","?",".",",",";",":","/","§"]

def check_word():
    for c in word:
        if c in letter:
            print("This word contains the letter : " ,c)
        elif c in blacklist:
            print("This word contains a blacklisted character !")

while True:
    word = input("Enter any word : ")
    check_word()
