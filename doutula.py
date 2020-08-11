import requests
import bs4
import random
import re
#arg：keyword      
#return ：fomat（like img gif..）
#save as ：/tem/doutu.fomat
def qiotu(keyword):
    url = "http://www.doutula.com/search"
    headers = {"keyword" : keyword}

    r = requests.get(url,headers)
    if r.status_code != 200:
        print("web request fail：%d" % r.status_code)
        return False
    else:
        soup = bs4.BeautifulSoup(r.text,"html.parser")
        reg = re.compile("http://img\.doutula\.com/production/uploads/image/.*")
        imgtaglist = soup.find_all("img",{"data-backup" : reg})
        if not len(imgtaglist):
            print("find emoji fail")
            return False
        else:
            imgtag = imgtaglist[random.randint(0,int(len(imgtaglist)))]
            imgurl = imgtag["data-backup"]
            fomat = re.search("\w\w\w$",imgurl).group()
            try:
                f = open("/tmp/doutu.%s" % fomat,"wb")
                data = requests.get(imgurl)
                print("find emoji: %s" % imgurl)
                f.write(data.content)
                print("write emoji")
                f.close()
            except IOError:
                print("write emoji fail")
            return fomat


