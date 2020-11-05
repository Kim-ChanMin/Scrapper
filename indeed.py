import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

def extract_indeed_pages() :
    # indeed.com에서 python과 관련된 회사 페이지
    indeed_result = requests.get(URL)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
    # 주소에서 page와 관련된 부분 찾기
    pagination = indeed_soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]  # get last page
    print(max_page)
    return max_page

def extract_indeed_jobs(last_page) :
    for page in range(last_page):
        result = requests.get(f"{URL}&start = {page*LIMIT}")
        print(result.status_code)