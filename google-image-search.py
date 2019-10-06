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
    img1 = driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/div[1]')
    img2 = driver.find_element_by_xpath('//*[@id="rg_s"]/div[2]/div[1]')
    img3 = driver.find_element_by_xpath('//*[@id="rg_s"]/div[3]/div[1]')
    # if found, retrieve the image source
    img_url = []
    if img1:
        img_url.append(json.loads(img1.get_attribute('innerHTML'))["ou"])
    if img2:
        img_url.append(json.loads(img2.get_attribute('innerHTML'))["ou"])
    if img3:
        img_url.append(json.loads(img3.get_attribute('innerHTML'))["ou"])
    print(img_url)
    driver.quit()
    return img_url

def main():
    try:
        inputfile = open("scraped_data.txt", "r")
        outputfile = open("google_img_urls.txt","a+")
        for searchtext in inputfile:
            print("Extracting the first image result url for " + searchtext + "...")
            outputList = get_img_url(searchtext)
            outputString = "["
            for i in outputList:
                outputString = outputString + "\""+ i + "\",\n"
            outputString = outputString + "]\n"
            outputfile.write(outputString)
            print("Success.")
    except Exception as e:
        print("Extraction failed.", e)
    finally:
        outputfile.close()
        inputfile.close()

if __name__ == "__main__":
    main()
