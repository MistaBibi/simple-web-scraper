import requests, sys, argparse
from bs4 import BeautifulSoup

def get_url_html(url, element, name, img_name):
    print("Attempting to GET request" + url + "...")
    response = requests.get(url, headers={'User-Agent': ""})
    scraped = BeautifulSoup(response.text, "html.parser")
    write_to_file(scraped.find_all(element, {"class": name}), img_name)
    print("Scraped " + url + ".")
    
def write_to_file(tags, img_name):
    f = open("img_src.txt", "a+")
    for tag in tags:
        child_tags = tag.findChildren("img")
        for child_tag in child_tags:
            print(child_tag['alt'])
            if child_tag['alt'] == img_name:
                t = str(child_tag['src'].encode("utf-8")).lstrip('0123456789.- ')
                f.write(t + "\n")
    f.close()

def main():
    f = open("input.txt", "r")
    for x in f:
        args = x.split(",", 3)
        print(args)
        get_url_html(args[0], args[1], args[2], args[3])
    f.close()

if __name__ == '__main__':
    main()
