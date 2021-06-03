import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
import urllib.request
import os
import re


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
		detailCells = soupPage.find_all("a", {'class': 'camera-details__link'})
		for detailCell in detailCells:
			if "View online network cameras in" in detailCell['title']:
				tempLoc = detailCell['title']
				location = tempLoc.replace("View online network cameras in",'')

	
	return [imageElement['src'], location]

# while True:
for url in urlList:
	imageUrl, location = get_image_url_from_page(url)
	image = url_to_image(imageUrl)
	cv2.imwrite('data/images1/screenshot.png', image)
	if not location: 
		location="No Location"
	os.system('py anpr.py --i data/images1/screenshot.png --l '+ location)
