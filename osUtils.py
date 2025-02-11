import os
import requests

class osUtils:

    def get_list_of_images(self):
        print("in list of images")
        images_list = [i for i in os.listdir("static") if '.jpg' in i ]
        print(images_list)
        return images_list


    def delete_images(self,images_list):
        print("in delete images")
        for image in images_list:
            os.remove("static/"+image)

    def create_folder(self):
        print("in create folder")
        if os.path.exists("static"):
            print( "path exists")
        else:
            os.makedirs("static")

    def persist_image(self,image_urls,keyword):
        print("in persist images")
        file_name=keyword
        counter =1
        for url in image_urls:
            image_content =  requests.get(url).content
            f = open(f'./static/{keyword}_{str(counter)}.jpg','wb')
            f.write(image_content)
            counter = counter+1
            f.close()



