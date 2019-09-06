from wxpy import *
import tuling
import doutula

EN_tuling = False#图灵机器人开关
EN_dotula = True#斗图网开关
IMG_NUM = 2#斗图的数量

bot = Bot(cache_path=True)
friend0 = bot.search("张克宁")[0]
friend1 = bot.search("岑龙鼎")[0]
friend2 = bot.search("高志宏")[0]
friend3 = bot.search("林泽森")[0]
friend4 = bot.search("王圣鑫")[0]
friend5 = bot.search("席佳伟")[0]
friend6 = bot.search("王肖")[0]
group0 = bot.search("斗图啦")[0]
accesslist = [friend0,friend1,friend2,friend3,friend4,friend5,friend6]
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
            sender.send_msg("【わはは】：%s " % rep_text)
        if EN_dotula:
            i = IMG_NUM
            while i:
                re = doutula.qiotu(msg.text)
                if not re:
                    sender.send_msg("没找到表情包，可惜可惜")
                else:
                    rep_img_format = re
                    sender.send_image("doutu.%s" % rep_img_format)
                    sender.send_file
                    print("图片发送完成")
                i = i-1

embed()
