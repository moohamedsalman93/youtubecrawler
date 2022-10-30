from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession


url="https://www.youtube.com/results?search_query=cyber+security"

session=HTMLSession()
res = session.get(url)
res.html.render(timeout=8000,sleep=8)
soup = bs(res.html, "html.parser")
d=soup.find_all("ytd-video-renderer")
for sa in d:
    u=sa.find("a",{"class":"yt-simple-endpoint style-scope ytd-video-renderer"})
    print(u)