# Install dependencies  
import requests   
from bs4 import BeautifulSoup as bs # importing BeautifulSoup  
import re  
import json as json  


# f = open('filename.txt', 'w',encoding='utf-8')
# for s in sd:
#     print(s, file = f)

ch={'Programming with Mosh':'https://yt3.ggpht.com/tBEPr-zTNXEeae7VZKSZYfiy6azzs9OHowq5ZvogJeHoVtKtEw2PXSwzMBKVR7W0MI7gyND8=s176-c-k-c0x00ffffff-no-rj',
    'Logic First Tamil':'https://yt3.ggpht.com/ytc/AMLnZu-iyk0DAEtQ3ewX34exnecsPSf0DwF-DBqY1RQK=s176-c-k-c0x00ffffff-no-rj',
    'Fireship':'https://yt3.ggpht.com/ytc/AMLnZu80d66aj0mK3KEyMfpdGFyrVWdV5tfezE17IwRkhw=s176-c-k-c0x00ffffff-no-rj',
    'freeCodeCamp.org':'https://yt3.ggpht.com/ytc/AMLnZu9UWrGceKWaqm8AF89vuxrEt8MO3E59qOoQ785Lew=s176-c-k-c0x00ffffff-no-rj-mo'
    
    }
    

def sd(url):
    global like,id,name,sub
    
    soup = bs(requests.get(url).content, "html.parser")
    
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)  
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']  
    videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer'] 
    likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,### likes"  
    likes_str = likes_label.split(' ')[0].replace(',','')
    like = '0' if likes_str == 'No' else likes_str  
    id = soup.find("meta", itemprop="channelId")['content']    
    name = soup.find("span", itemprop="author").next.next['content']  
    sub = videoSecondaryInfoRenderer['owner']['videoOwnerRenderer']['subscriberCountText']['accessibility']['accessibilityData']['label']  
    sa(name)

def sa(g):
    global img
    try:
        img=ch[g]
    except:    
        try:
            url1 = f"https://www.youtube.com/c/{g}/about"  
            soup1 = bs(requests.get(url1).content, "html.parser")
            data1 = re.search(r"var ytInitialData = ({.*?});", soup1.prettify()).group(1)
            data_json1 = json.loads(data1)
            img=data_json1['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][2]['url']
        except :
            img=g
#title
f = open("read.txt", "r")
f2=open('filename.txt', 'w',encoding='utf-8')
print('title={',file=f2)
for x in f:
    sd(x)
    print(f'"{name}",',file=f2)
print('};\n',file=f2)
f2.close

# #sub
f = open("read.txt", "r")
f2=open('filename.txt', 'a',encoding='utf-8')
print('sub={',file=f2)
for q in f:
    sd(q)    
    f2.write(f"'{sub}',\n")
print('};\n',file=f2)
f2.close

# #like
f = open("read.txt", "r")
f2=open('filename.txt', 'a',encoding='utf-8')
print('likes={',file=f2)
for q in f:
    sd(q)    
    f2.write(f"'{like}',\n")
print('};\n',file=f2)
f2.close        

#img
f = open("read.txt", "r")
f2=open('filename.txt', 'a',encoding='utf-8')
print('img={',file=f2)
for q in f:
    sd(q)
    f2.write(f"{name}:'{img}',\n")
print('};\n',file=f2)
f2.close