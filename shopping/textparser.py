from feedin.parser import TaobaoParser
import feedin.models
import urllib
html = open('/home/jing/Downloads/item.html').read()
#url = 'http://item.taobao.com/item.htm?spm=a230r.1.14.1.HaoFoW&id=19823663991'
#html = urllib.urlopen(url).read()
p = TaobaoParser()
p.feed(html)
item = p.get_commodity()
