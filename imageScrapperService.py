import time
#import urllib
import os

from selenium import webdriver
from ImageUtils import ImageUtils
#from webdriver_manager.chrome import ChromeDriverManager
class imageScrapperService:

    def get_imageurls(self,url,number_of_images):
        image_urls=[]
        imageObj = ImageUtils()
        #driver = webdriver.Chrome('./chromedriver')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')

        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        driver.get(url)
        #driver.implicitly_wait(30)

        #scroll page to bottom
        imageObj.scroll_to_bottom(driver)


        thumbnailList = driver.find_elements_by_css_selector('img.Q4LuWd')
        print(len(thumbnailList))
        #image_name = "mahi"
        for image in thumbnailList:
            #image_name = image_name + "s"
            image.click()
            time.sleep(0.5)
            imageurl = driver.find_elements_by_css_selector('img.n3VNCb')
            if(len(image_urls)>=number_of_images):
                break
            for i in imageurl:
                try:

                    if ('http' in i.get_attribute('src')):
                        img = i.get_attribute('src')
                        print(i.get_attribute('src'))
                        if img not in image_urls:
                            image_urls.append(img)
                            break
                        #urllib.request.urlretrieve(img, "./downloadedImages/" + image_name + ".jpg")

                except:
                    continue

        print("number-",len(image_urls))
        return image_urls