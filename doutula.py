import requests
import bs4
import random
import re
#arg：keyword      
#return ：fomat（like img gif..）
#save as ：/tem/doutu.fomat
def qiotu(keyword):
    url = "https://www.doutula.com/search"
    parms = {"keyword" : keyword}
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66"}

    r = requests.get(url,params=parms,headers = headers)
    #print(r.text)
    if r.status_code != 200:
        print("web request fail：%d" % r.status_code)
        return False
    else:
        soup = bs4.BeautifulSoup(r.text,"html.parser")
        reg = re.compile("http://img\.doutula\.com/production/uploads/image/.+\.(png|gif|jpg)")
        imgtaglist = soup.find_all("img",{"data-backup" : reg})
        #print(imgtaglist)
        if not len(imgtaglist):
            print("find emoji fail")
            return False
        else:
            imgtag = imgtaglist[random.randint(0,int(len(imgtaglist)))]
            imgurl = imgtag["data-backup"]
            fomat = re.search("\w\w\w$",imgurl).group()
            try:
                f = open("./doutu.%s" % (fomat),"wb")
                data = requests.get(imgurl)
                print("find emoji: %s" % imgurl)
                f.write(data.content)
                print("write emoji")
                f.close()
            except IOError:
                print("write emoji fail")
            return fomat


