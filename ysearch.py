from unicodedata import name
from youtubesearchpython import *

cs=CustomSearch('java',VideoDurationFilter.long,limit=5)


for i in range(5):
    _name=cs.result()['result'][i]['channel']['name']
    link=cs.result()['result'][i]['link']
    dur=cs.result()['result'][i]['duration']
    icon=cs.result()['result'][i]['channel']['thumbnails'][0]['url']
    view=cs.result()['result'][i]['viewCount']['short']
    url =icon.replace("s68", "s200" )
    
    print("------------------------------")
    print(_name)
    print(link)
    print(dur)
    print(view)
    print(url)