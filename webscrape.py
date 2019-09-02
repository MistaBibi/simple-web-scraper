import requests
import sys, getopt
from bs4 import BeautifulSoup

def get_url_html(url, name):
    print("Attempting to GET request" + url + "...")
    response = requests.get(url)
    scraped = BeautifulSoup(response.text, "html.parser")
    write_to_file(scraped.find_all("h2", {"class": name}))
    print("Scraped" + url + ".")
    
def write_to_file(tags):
    f = open("scraped_data.txt","w+")
    for tag in tags:
        t = str(tag.text.encode("utf-8")).lstrip('0123456789.- ')
        f.write(t + "\n")
    f.close()

def main():
    get_url_html(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
