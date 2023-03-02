import requests
url = "http://testphp.vulnweb.com/login.php"
#url = 'https://news.ycombinator.com/login?goto=news'
values = {'username': 'userw456456', 'password': 'pass345646756'}
r = requests.post(url, data=values)
print(r.content)
#r = requests.get("http://testphp.vulnweb.com/login.php")
if r.status_code == 200:
    print("success")
elif r.status_code == 404:
    print("failure")