import requests, sys, argparse
from bs4 import BeautifulSoup

def get_url_html(url, element, name):
    print("Attempting to GET request" + url + "...")
    response = requests.get(url)
    scraped = BeautifulSoup(response.text, "html.parser")
    write_to_file(scraped.find_all(element, {"class": name}))
    print("Scraped " + url + ".")
    
def write_to_file(tags):
    f = open("scraped_data.txt","a+")
    for tag in tags:
        t = str(tag.text.encode("utf-8")).lstrip('0123456789.- ')
        f.write(t + "\n")
    f.close()

def main():
    f = open("input.txt", "r")
    for x in f:
        args = x.split(",", 3)
        get_url_html(args[0], args[1], args[2])
    f.close()

if __name__ == '__main__':
    main()
