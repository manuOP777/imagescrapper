import time

class ImageUtils:

    def scroll_to_bottom(self,driver):
        i=0
        while(driver.find_element_by_css_selector('div.YstHxe').get_attribute("style")=="display: none;" and i<10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i=i+1


