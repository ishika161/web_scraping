from bs4 import BeautifulSoup
import requests

url="https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/"
# fetching content of a website
raw=requests.get(url)

# display content
content = BeautifulSoup(raw.text,"html.parser")
#print(content.prettify())

# searching for a particular tag
heading=content.find("title")
print(heading.string)

#gathering images
for i in content.find_all("img"):
    print(i['src'])

