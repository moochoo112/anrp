import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
import urllib.request
import os


#working with insecam url
insecam = "insecam"
prvgld = "prvgld"

urlList = ["http://www.insecam.org/en/view/854253/"]


#define headers
#we do this to trick websites into thinking we are real users
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def url_to_image(url):
	response = urllib.request.urlopen(url)
	image = np.asarray(bytearray(response.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

def get_image_url_from_page(url):
	#load the webpage and add the header as header
	response = requests.get(urlList[0], headers=headers)
	response.request.headers
	{'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 		 'Accept': '*/*'}

	soupPage = BeautifulSoup(response.text, "html.parser")

	if(insecam in url):
		imageElement = soupPage.find("img", {'id':'image0'})
	if(prvgld in url):
		imageElement = soupPage.find("div", {'class':'html5-video-container'})
	return imageElement['src']

while True:
    for url in urlList:
        imageUrl = get_image_url_from_page(url)
        image = url_to_image(imageUrl)
        print(url)
        cv2.imwrite('data/images1/screenshot.png', image)
        os.system('py anpr.py --i data/images1/screenshot.png')
