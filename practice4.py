import requests
res = requests.get("http://www.google.com")
res.text

file = open("html_page.txt", 'w')
file.write(res.text)
file.close()
