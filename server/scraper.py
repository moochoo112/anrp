#imports
from selenium import webdriver
from PIL import Image
import operator
import time

#set options for the chrome driver that opens
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

#find driver
driver = webdriver.Chrome(options=options)

#open the driver with the link to the site
driver.get('https://www.youtube.com/watch?v=RTT8ia0nRQU&ab_channel=GeldersVerkeer')

#maximize window
driver.maximize_window()

#agree to cookies 
element = driver.find_element_by_xpath("//button[@jscontroller='soHxf']")
element.click()

#wait for the video to load
time.sleep(3)


#locate the video
element = driver.find_element_by_xpath("//video[@class='video-stream html5-main-video']")
location = element.location

#function to make the screenshot
def Make_Screenshot():
    #take screenshot
    size = element.size
    driver.save_screenshot("screenshot.png")

    #crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    #open screenshot
    im = Image.open('screenshot.png')
    #crop screenshot
    im = im.crop((int(x), int(y), int(width), int(height)))
    #save screenshot
    im.save('screenshot.png')

while True:
    Make_Screenshot()

driver.quit()