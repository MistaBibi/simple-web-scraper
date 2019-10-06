from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
import requests
import sys

# adding path to geckodriver to the OS environment variable
# assuming that it is stored at the same path as this script
os.environ["PATH"] += os.pathsep + os.getcwd()

def get_img_url(searchtext):
    # Google search query
    # &tbm=isch - image search
    # &tbs=isz:m - image size is medium
    # iar:s - image aspect ratio is square
    # sur:fc - 
    url = "https://www.google.com/search?q="+searchtext+"&tbm=isch&tbs=sur:fc"

    # initiate MF web driver
    driver = webdriver.Firefox()

    # using driver, retrieve webpage based on url
    driver.get(url)

    # retrieve the first image of the results
    img = driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/div[1]')

    # if found, retrieve the image source
    img_url = ""
    if img:
        img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
    driver.quit()
    return img_url

def main():
    try:
        inputfile = open("scraped_data.txt", "r")
        outputfile = open("img_urls.txt","a+")
        for searchtext in inputfile:
            print("Extracting the first image result url for " + searchtext + "...")
            outputfile.write("\"" + get_img_url(searchtext) + "\",\n")
            print("Success.")
    except Exception as e:
        print("Extraction failed.", e)
    finally:
        outputfile.close()
        inputfile.close()

if __name__ == "__main__":
    main()
