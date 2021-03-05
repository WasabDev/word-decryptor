letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","é","è","ê","ë","ô","ö","ç","à","ù"]
blacklist = ["&","(",")","-","_","~","#","{","}","[","]","|","`","^","@","¨","¤","£","$","%","µ","*","!","?",".",",",";",":","/","§"]
reset = True

def check_word():
    for c in word:
        if c in letter:
            print("This word contains the letter : " ,c)
        elif c in blacklist:
            print("This word contains a blacklisted character !") 

while reset:
    word = input("Enter any word : ")
    check_word()