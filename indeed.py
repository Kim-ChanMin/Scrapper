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
    for page in range(last_page):
        print(f"Scrapping page {page}.")
        result = requests.get(f"{URL}&start = {page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"}) # html lists

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs

def extract_job(html) :
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")  # Some company doesn't have a link
    # too many blanks get out. -> use strip to solve
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()  # delete blank
    location = html.find("div",{"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return{'title' : title, 'company' : company, 'location' : location, "link" : "https://www.indeed.com/viewjob?jk={}".format(job_id)}