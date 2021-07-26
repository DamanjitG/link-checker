from bs4 import BeautifulSoup
from http import HTTPStatus as hs
import requests, sys

if len(sys.argv) > 1:
    base = sys.argv[1]
else:
    base = input("Please enter your URL:\n")

def recurseLinks(target):
    try:
        page = requests.get(target)
    except Exception as e:
        print(f"Error requesting: {e}")
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Checking links on " + target)
    linksOnPage = soup.find_all("a", href=True)
    '''
    # strip any non-web links
    for link in linksOnPage:
        print(link.get('href'))
        if 'http' not in str(link.get('href')):
            linksOnPage.remove(link)
    print(linksOnPage)
    '''

    if not len(linksOnPage):
        print("No links on this page")
    else:
        for link in linksOnPage:
            if 'http' not in str(link.get('href')):
                continue
            else:
                if True:
                    try:
                        response = requests.get(link.get('href'))
                        print(f"Link: {link.get('href')}: {response.status_code} ({hs(response.status_code).phrase})") 
                    except Exception as e:
                        print(f"Error retrieving status code: {e}")
        for link in linksOnPage:
            if 'http' not in str(link.get('href')):
                continue
            else:
                if input("Input 'y' if you would like to recurse through link " + (link.get('href')) + '\n') == 'y':
                    recurseLinks(str(link.get('href')))
    print(f"Completed operations on page {target}\n")

recurseLinks(base)

