import requests
import json
import shutil
import os

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

INSTA_URL = 'https://www.instagram.com/'
USER_ID = input('Enter the USER NAME : ')
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
