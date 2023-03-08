import sys
from pathlib import Path

from sys import argv
# This imports the password cracking python file to log into a username
from password_crack import password_crack

# These lines record the number of command lines and print them
n = len(argv)
print("total arguments passed: " + str(n))
# These lines define if there are username and password commands
defUsername = 0
defWordlist = 0
# These lines check where username or text file commands take place in the commandline.
if n > 5:
    sys.exit("Error: Too many commands")
elif n == 5:
    if argv[1] == "-u":
        username = argv[2]
        defUsername = 2
    elif argv[1] == "-b" and Path(argv[2]).is_file():
        wordList = argv[2]
        defWordlist = 2
    if argv[3] == "-u":
        username = argv[4]
        defUsername = 4
    elif argv[3] == "-b" and Path(argv[4]).is_file():
        wordList = argv[4]
        defWordlist = 4
elif 5 > n > 1:
    if argv[1] == "-u":
        username = argv[2]
        defUsername = 2
    elif argv[1] == "-b" and Path(argv[2]).is_file():
        wordList = argv[2]
        defWordlist = 2
# These lines print if certain commands are successful in the commandline, and what they entail.
if defUsername:
    print("Successful username commandline argument, username: " + argv[defUsername])
else:
    print("username commandline argument not submitted, Default username: test")
    username = "test"
if defWordlist:
    print("Successful wordlist commandline argument, wordlist: " + argv[defWordlist])
else:
    print("wordlist commandline argument not submitted / not found, Default wordlist: book2.txt")
    wordlist = "book2.txt"
# This line redirects the wordlist and username variable values into the password cracking function.
password_crack(wordlist, username)
