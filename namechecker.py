import requests
from lxml import html

a = raw_input("Username : ")
r = requests.get('https://twitter.com/' + a)
if r.status_code == 200:
    print "Twitter : "+a + " is taken. Sorry."
elif r.status_code==404:
    print "Twitter : "+a + " is available. Yay!"
else:
    print "Error."            

r = requests.get('https://facebook.com/' + a)
if r.status_code == 200:
    print "Facebook : "+a + " is taken. Sorry."
elif r.status_code==404:
    print "Facebook : "+a + " is available. Yay!"
else:
    print "Error." 
r = requests.get('http://' + a + '.tumblr.com/')
if r.status_code == 200:
    print "Tumblr : "+a + " is taken. Sorry."
elif r.status_code==404:
    print "Tumblr : "+a + " is available. Yay!"
else:
    print "Error."
r = requests.get('https://youtube.com/'+a)
if r.status_code == 200:
    print "Youtube : "+a + " is taken. Sorry."
elif r.status_code==404:
    print "Youtube : "+a + " is available. Yay!"
else:
    print "Error."
r = requests.get('https://instagram.com/'+a)
if r.status_code == 200:
    print "Instagram : "+a + " is taken. Sorry."
elif r.status_code==404:
    print "Instagram : "+a + " is available. Yay!"
else:
    print "Error."
r = requests.get('https://t.me/'+a)
text = 'class="tgme_icon_user"'
if text in r.text:
    print "Telegram : "+a + " is available. Yay!"
elif r.status_code==200:
    print "Telegram : "+a + " is taken. Sorry."
else:
    print "Error."
print "Domain :"
r = requests.get('https://who.is/whois/'+a+".com")
text = 'No Data Found'
if text in r.text:
    print a + ".com is available. Yay!"
elif r.status_code==200:
    print a + ".com is taken. Sorry."
    tree = html.fromstring(r.content)
    info = tree.xpath('//div[@class="col-md-8 queryResponseBodyValue"]/text()')
    print "Expire date : " + info[5]
else:
    print "Error."
r = requests.get('https://who.is/whois/'+a+".co")
text = 'No Data Found'
if text in r.text:
    print a + ".co is available. Yay!"
elif r.status_code==200:
    print a + ".co is taken. Sorry."
    tree = html.fromstring(r.content)
    info = tree.xpath('//div[@class="col-md-8 queryResponseBodyValue"]/text()')
    print "Expire date : " + info[-7]
else:
    print "Error."
r = requests.get('https://who.is/whois/'+a+".org")
text = 'No Data Found'
if text in r.text:
    print a + ".org is available. Yay!"
elif r.status_code==200:
    print a + ".org is taken. Sorry."
    tree = html.fromstring(r.content)
    info = tree.xpath('//div[@class="col-md-8 queryResponseBodyValue"]/text()')
    print "Expire date : " + info[-7]
else:
    print "Error."
r = requests.get('https://who.is/whois/'+a+".net")
text = 'No Data Found'
if text in r.text:
    print a + ".net is available. Yay!"
elif r.status_code==200:
    print a + ".net is taken. Sorry."
    tree = html.fromstring(r.content)
    info = tree.xpath('//div[@class="col-md-8 queryResponseBodyValue"]/text()')
    print "Expire date : " + info[-7]
else:
    print "Error."
r = requests.get('https://who.is/whois/'+a+".biz")
text = 'No Data Found'
if text in r.text:
    print a + ".biz is available. Yay!"
elif r.status_code==200:
    print a + ".biz is taken. Sorry."
    tree = html.fromstring(r.content)
    info = tree.xpath('//div[@class="col-md-8 queryResponseBodyValue"]/text()')
    print "Expire date : " + info[-7]
else:
    print "Error."


