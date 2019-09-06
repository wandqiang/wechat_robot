import requests
import bs4
import random
import re
#arg：关键字　图片数量
#return ：fomat（图片格式），如果没找到图片或网页请求失败就返回False
#图片存在当前目录下：/doutu.fomat
def qiotu(keyword):
    url = "http://www.doutula.com/search"
    headers = {"keyword" : keyword}

    r = requests.get(url,headers)
    if+ r.status_code != 200:
        print("网页请求失败：%d" % r.status_code)
        return False
    else:
        soup = bs4.BeautifulSoup(r.text,"html.parser")
        reg = re.compile("http://img\.doutula\.com/production/uploads/image/.*")
        imgtaglist = soup.find_all("img",{"data-backup" : reg})
        if not len(imgtaglist):
            print("找寻图片失败")
            return False
        else:
            imgtag = imgtaglist[random.randint(0,int(len(imgtaglist)))]
            imgurl = imgtag["data-backup"]
            fomat = re.search("\w\w\w$",imgurl).group()
            try:
                f = open("doutu.%s" % fomat,"wb")
                data = requests.get(imgurl)
                print("图片请求完成: %s" % imgurl)
                f.write(data.content)
                print("图片写入完成")
                f.close()
            except IOError:
                print("写入图片错误")
            return fomat


