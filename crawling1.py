from urllib.request import urlopen
from bs4 import BeautifulSoup

web=urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup=BeautifulSoup(web, "html.parser")
tmp=soup.select('.col_list0')

for link in soup.find_all('a'):
    print(link.text.strip(), "http://www.swu.ac.kr"+link.get('href'))
