import re
string = "1斗图啦总总群 › Eric : 再来一次 2(Text)"
text = "hill hiee ehie"
r = re.search(r"^.*:",string)
print(r)
print(r.group())