import requests
from bs4 import BeautifulSoup
import os


url = '#'
#create function that takes url and directoryName argument
def imageDown(url, directoryName):
    try:
        os.mkdir(os.path.join(os.getcwd(), directoryName))#make directorty 
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), directoryName))# move into directory
    r = requests.get(url)#create request using passed URL argument 
    soup = BeautifulSoup(r.text, 'lxml')#create BS parser with specified markup language
    imageList = soup.find_all('img', {"class": "grid-product__image"})#findall image tag elements with the specified class
    newDict = {}# create a dictionary for the tag elements
    index = 0# create an index for the generator, for while loop
    # while loop that creates dictionary using the alt tags(combined with suffix to prevent duplicate overwrite) as keys and the url "src" as the values
    while index < len(imageList):
            newDict[imageList[index].get('alt') + str(index) + url[-1]] = imageList[index].get('src')
            index += 1
    for i, j in newDict.items():
        print(i,j)
    # name and write each image to above created directory
    for name, link in newDict.items():
        with open(name.replace(' ', '-').replace('/', '').replace('|', '').replace('"', '').replace('*', '') + '.jpg', 'wb') as f:
            results = requests.get('https:' + link)
            f.write(results.content)
            print('Writing ' + name)



imageDown(url, '#')



'''for i, j in enumerate(images):
    print(i, j)
    print(' ')
'''