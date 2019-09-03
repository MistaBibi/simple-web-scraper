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
    """
        I put the example in the input.txt now I want to scrap 2 elements from this site
        First I will provide the url, then the first element and class name, after I will
        provide you the second element and class name. The second element will always be a img class and I want to get the img url which is provided.
        quick side notes sometimes the class name is not provided and in case of that it should just get all the h2 and for img it should only be scrapped if is in the same family/sub class as the h2 
        Exp:
        
      
       we can get the img url from the src field
       which give us the result:
       <img aria-describedby="caption-attachment-25405" class="wp-image-25405 size-large" src="https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-1100x733.jpg" alt="Fushimi Inari shrine in Kyoto, one of the best places to visit in Japan" width="1100" height="733" srcset="https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-1100x733.jpg 1100w, https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-700x467.jpg 700w, https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-768x512.jpg 768w, https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-300x200.jpg 300w, https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-450x300.jpg 450w, https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan.jpg 1500w" sizes="(max-width: 1100px) 100vw, 1100px">
       
       Kyoto https://dwgfmnrdprofc.cloudfront.net/wp-content/uploads/2017/11/planning-a-trip-to-japan-1100x733.jpg
       if you can also make the img around 350x350 if not that's fine sometimes they provide you lower resolution imgs like in here I would prefer the 450x300.
        
        
    
    """

def main():
    f = open("input.txt", "r")
    for x in f:
        args = x.split(",", 3)
        get_url_html(args[0], args[1], args[2])
    f.close()

if __name__ == '__main__':
    main()
