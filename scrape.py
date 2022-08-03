from bs4 import BeautifulSoup

#open html file 
with open ("index.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")
#print(doc)
#use prettify for proper indentation
#print(doc.prettify())

#getting tag - first appearing
tag_head1=doc.h1
print(tag_head1)

#getting all tags
tag_all_head=doc.find_all("h1")
print(tag_all_head)