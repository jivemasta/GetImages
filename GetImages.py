import urllib
import urllib.request
import time
import re
import os
from bs4 import BeautifulSoup

running = True
sleepMinutes = 10
rootUrl = "http://www.noahbradley.com/images/4k/"

while running:
    images = []

    #starting loop
    print("Running...")

    response = urllib.request.urlopen(rootUrl)

    soup = BeautifulSoup(response.read(),"html.parser")

    for link in soup.findAll('a') :
        if link.has_attr('href'):
            t = re.match(".*\....",link['href'])
            if t :
                images.append(link['href'])

    print("Found {} images".format(len(images)))

    files = []


    for image in images:
        if not os.path.isfile(image):
            print("Downloading: {}".format(image))
            urllib.request.urlretrieve(rootUrl + image,image)

    #go to sleep for some amount of time
    print("Sleeping for {} minutes".format(sleepMinutes))
    time.sleep(sleepMinutes*60)