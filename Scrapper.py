import requests
from bs4 import BeautifulSoup

#indeed.com에서 python과 관련된 회사 페이지
indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
#주소에서 page와 관련된 부분 찾기
pagination = indeed_soup.find("ul",{"class" : "pagination-list"})

pages = pagination.find_all('a')

spans = []
for page in pages :
    spans.append(page.find("span"))

print(spans[:-1]) #except last one
