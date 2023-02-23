import requests
import time
import multiprocessing
from PIL import Image
from functools import partial

url_list = ["https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1493976040374-85c8e12f0c0e.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1504198453319-5ce911bafcde.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1507143550189-fed454f93097.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1513938709626-033611b8cc03.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1516117172878-fd2c41f4a759.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1516972810927-80185027ca84.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1522364723953-452d3431c267.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1524429656589-6633a470097c.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1530122037265-a5f1f91d3b99.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1530224264768-7ff8c1789d79.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1532009324734-20a7a5813719.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1541698444083-023c97d3f4b6.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1549692520-acc6669e2f0c.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1550439062-609e1531270e.jpg",
            "https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/photo-1564135624576-c5c88640f235.jpg"]


def download(url_list):
    for url in url_list:
        # print(url)
        response = requests.get(url)
        # print(response.content)
        file_name = url.split('/')[-1]
        # print(file_name)
        file = open('pic/'+ file_name, "wb")
        # print("Opened successfully!")
        file.write(response.content)
        # print("Successfully write content into file")
        file.close()
        # print("Closed file successfully")

        try:
            image = Image.open('pic/'+ file_name)
            # print("Image opened")
            image = image.convert('L')
            image.save('pic/'+ file_name)
            print(file_name, "DONE!")
        except Exception as e:
            pass
            print("\nomitted: ", file_name, "\n")

download(url_list)


####  Worked fine!!! Remember to set your own paths/folder where you want the pics to be downloaded!!!