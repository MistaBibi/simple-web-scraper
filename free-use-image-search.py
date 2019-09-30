from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
import os
import json
import requests
import sys

# adding path to geckodriver to the OS environment variable
# assuming that it is stored at the same path as this script
os.environ["PATH"] += os.pathsep + os.getcwd()
sources = ["https://www.pexels.com/search/", "https://www.unsplash.com/s/photos/", "https://www.shutterstock.com/search/"]
source_img_classes = ["photo-item__img", "_2zEKz", "z_g_g"]
num_results = 3

def get_img_url(searchtext):
    # collection of img urls
    img_urls = []

    # initiate MF web driver
    driver = webdriver.Firefox()

    # iterate through sources and retrieve images
    for i in range(len(sources)):
        print("Attempting retrieval from source: " + "/".join(sources[i].split('/', 3)[:3]))
        driver.get(sources[i] + searchtext)
        # retrieve all images from the source
        elements = driver.find_elements_by_xpath('//img[@class="' + source_img_classes[i] + '"]')
        for element in elements:
            # if the number of results has been satisfied, return results
            if len(img_urls) >= num_results:
                driver.quit()
                return img_urls
            img_urls.append(element.get_attribute("src"))
        print("Result count has not been satisfied; moving on to the next source.")
    driver.quit()
    print("Insufficient result count from provided sources, returning all procured results.")
    return img_urls

def main():
    try:
        inputfile = open("scraped_data.txt", "r")
        outputfile = open("copyright_free_img_urls.txt","a+")
        for searchtext in inputfile:
            print("Extracting the first image result url for " + searchtext + "...")
            img_srcs = get_img_url(searchtext)
            for img_src in img_srcs:
                outputfile.write("\"" + img_src + "\",")
            outputfile.write("\n")    
            print("Success.")
    except Exception as e:
        print("Extraction failed.", e)
    finally:
        outputfile.close()
        inputfile.close()

if __name__ == "__main__":
    main()