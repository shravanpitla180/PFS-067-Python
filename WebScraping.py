# # Web Scraping :--> It is a process of automatically collecting the information from websitesusing a program
# '''
# Where is this used ?
# ->extracting article headlines
# ->collecting products data
# ->gathering job listing
# ->collecting publicly available research data.
# '''
# # 2.Request module :-
# # The rerquest library allows Python to send http requests to websites and receive their responses...


# import requests
# url = "https://brandforce.co.in/"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)


# #Adding basic error handling
# print("Adding basic error handling")
# import requests
# url = "https://brandforce.co.in/"
# try:
#     response = requests.get(url,timeout=10)
#     response.raise_for_status()
#     print(response.text)
# except requests.RequestException as error:
#     print("request failes: ",error)

# #BeautifulSoup:
# #Requests download the HTML, but we need a convenient way to find a particular elements insude it.
# # That's where BeautifulSouphelps

# from bs4 import BeautifulSoup

# html = """
# <html>
# <head>
#     <title>My first website</title>
# </head>
# <body>
#     <h1>Welcome to pyhton</h1>
#     <p>Learn web scraping.</p>
# </body>
# </html>
# """

# soup = BeautifulSoup(html,"html.parser")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.h1.get_text())
# print(soup.p.get_text())


# #Important BeautifulSoup
# # 1.find()-->finds the first matching element
# soup.find("p")

# # 2. find_all() -->Finds all matching elements
# soup.find_all("p")

# # 3.get_text ()-->Extract text

# # 4.get()-->Extracts an attribute
# # link = soup.find("a")
# # print(link.get("href"))


# #Extracting Web-site Data

# import requests
# from bs4 import BeautifulSoup
# url = "https://theuselessweb.com/"
# response = requests.get(url, timeout = 10)
# response.raise_for_status()
# soup = BeautifulSoup(response.text, "html.parser")
# title = soup.title.get_text(strip=True)
# heading = soup.find("h1").get_text(strip = True)
# print("Page Title: ",title)
# print("Heading: ",heading)


#Extract all links
import requests
from bs4 import BeautifulSoup
url = "https://brandforce.co.in/"
response = requests.get(url, timeout = 10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a")
for link in links:
    text = link.get_text(strip = True)
    url = link.get_text("href")
    print("Link Text: ",text)
    print("URL: ",url)

    