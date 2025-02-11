#from urllib.request import Request,urlopen as uReq
#import requests
#import time
#from bs4 import BeautifulSoup
#from selenium import webdriver
#import urllib.request
import os
from osUtils import osUtils
from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin

from imageScrapperService import imageScrapperService

app = Flask(__name__)



@app.route('/',methods=['GET'])
@cross_origin()
def home_page():

    return render_template("home.html")


@app.route('/review',methods=['POST'])
@cross_origin()
def image_page():
    print(request.form)
    imageObj = imageScrapperService()

    if request.form['number_of_images']=='' or request.form['keyword']=='':
        return "Invalid inputs"
    else:
        number_of_images = int(request.form['number_of_images'])
        keyword = request.form['keyword']

    url = "https://www.google.com/search?q={SEARCHTERM}&tbm=isch".format(SEARCHTERM=keyword)
    print(url)
    if(number_of_images>50):
        number_of_images=50

    # clearing the images folder

    osObj = osUtils()
    osObj.create_folder()
    images_list = osObj.get_list_of_images()
    osObj.delete_images(images_list)

    imageScrapObj = imageScrapperService()
    image_urls = imageScrapObj.get_imageurls(url, number_of_images)
    print(len(image_urls))
    osObj.persist_image(image_urls, keyword)
    images_names = osObj.get_list_of_images()
    print(images_names)
    return render_template("image.html",user_images=images_names)


port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(host='0.0.0.0', port=port)

