from wxpy import *
import tuling
import doutula

EN_tuling = True#when this is True,you'll auto replying. 
EN_dotula = True#when this is True,you'll get emoji fighting feature.
IMG_NUM = 1 #the number of emoji.

bot = Bot(cache_path=True)
friend0 = bot.search("天使")[0]#turn the string to your real wechat friend's nick name.and you could add other friends like friend1 or friend2 etc.but you should add 'friend1' or 'friend2' to the array 'accesslist' below.
#group0 = bot.search("group")[0] #just like friend0.
accesslist = [friend0] #where you add your friend or group.
@bot.register(msg_types="Text")
def auto_rep(msg):
    sender = msg.sender
    if sender in accesslist:
        if isinstance(sender,Friend):
            bot.file_helper.send_msg("%s: " % sender.remark_name+ msg.text)
        else:
            bot.file_helper.send_msg("%s: " % sender.name + msg.text)
        if EN_tuling:
            rep_text = tuling.tuling_reply(msg.text)
            sender.send_msg("【robot】：%s " % rep_text)
        if EN_dotula:
            i = IMG_NUM
            while i:
                re = doutula.qiotu(msg.text)
                if not re:
                    sender.send_msg("there is no emoji!")
                else:
                    rep_img_format = re
                    sender.send_image("./doutu.%s" % (rep_img_format))
                    sender.send_file
                    print("send is ok")
                i = i-1

embed()
