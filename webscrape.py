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
    parser = argparse.ArgumentParser()
    requiredargs = parser.add_argument_group('required arguments')
    requiredargs.add_argument("-u", "--url", help="the url to request data from", required=True)
    requiredargs.add_argument("-e", "--element", help="the HTML element to find all occurences for", required=True)
    parser.add_argument("-n", "--name", help="the name of the element to scrape data from")
    args = parser.parse_args()
    get_url_html(args.url, args.element, args.name)

if __name__ == '__main__':
    main()
