import os
import requests
from lxml import html

#print('URL : ')
#url = input()
#response = requests.get(url)
url = 'https://news.google.com'
print ('Lang : ')
lang = input()
if(lang == 'pt'):
    url = url + '/?ned=pt-br_br&gl=BR&hl=pt-br'
else:
    url = url + '/?ned=us&gl=US&hl=en'

print(url)

response = requests.get(url)

f = open('titles.txt', 'w')

#response ok
if(response.status_code == 200):
    print('Reponse OK!')

    page = html.fromstring(response.text)
    #text = page.cssselect('a.nuEeue.hzdq5d.ME7ew')[0].text
    for a in page.cssselect('a.nuEeue.hzdq5d.ME7ew'):
        f.write(a.text)
        #f.write(str(a.text_content().encode('utf-8'))[2:-1])
        f.write(os.linesep)
        #f.write('\n')
        #print(a.text_content().encode('utf-8'))

    f.close()
else:
    print('Requests failed!')