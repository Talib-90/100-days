from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.text)
# print(soup.prettify())
all_tags = soup.find_all(name='a')
# print(all_tags)

select_all = soup.select_one(selector="p a")
# print(select_all)

heading = soup.select("#heading")
print(heading)