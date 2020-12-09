from bs4 import BeautifulSoup
import requests
import json
import shutil
import os

URL = "https://www.instagram.com/{}/"


def insta_info():

    username = input("USERNAME ☘ : ")
    print('Geting request ☕')
    r = requests.get(URL.format(username))
    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find("meta", property="og:description")
    s = (meta.attrs['content'])
    print('Data found ℹ')
    data = {}
    s = s.split("-")[0]
    s = s.split(" ")
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    print(data)
    print('\n')


def insta_dp():

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }

    INSTA_URL = 'https://www.instagram.com/'
    USER_ID = input("USERNAME ☘ : ")
    tail = "/?__a=1"
    print("Tracking ID ⚠...")


    URL = INSTA_URL+USER_ID+tail

    response = requests.get(URL, headers=header).json()

    image_location = response["graphql"]["user"]["profile_pic_url"]
    hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]

    print("Image Found ℹ...")
    hd_image_response = requests.get(hd_image_location, stream=True)
    with open("hd_img.jpg", "wb") as out_file:
        shutil.copyfileobj(hd_image_response.raw, out_file)

    print("Image Downloaded☑")
    print('\n')

if __name__ == "__main__":

    while True:
        
        print("1: Download insta DP ☸ :")
        print("2: Extract insta info ☢ :")
        take = input("Catch 🕸 : ")

        take = int(take)

        if take == 1:
            insta_dp()

        elif take == 2:
            insta_info()
