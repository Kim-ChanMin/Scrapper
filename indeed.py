import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python%20developer&limit={}&radius=25".format(LIMIT)

def extract_indeed_pages() :

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]  # get last page
    return max_page

def extract_indeed_jobs(last_page) :

    jobs = []
    result = requests.get(f"{URL}&start = {0*LIMIT}") #in first page
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"}) # html lists

    for result in results:
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        company = result.find("span",{"class":"company"})
        company_anchor = company.find("a") #Some company doesn't have a link
        #too many blanks get out. -> use strip to solve
        if company_anchor is not None :
            company = str(company_anchor.string)
        else :
            company = str(company.string)
        company = company.strip() #delete blank
        print(title, company)
    return jobs