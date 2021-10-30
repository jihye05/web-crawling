import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

web=urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup=BeautifulSoup(web, "html.parser")  # BeautifulSoup이용 파싱하기
tmp=soup.select('a')
# links=soup.find_all('a')
# cell_line=[]

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***")
print("학과".ljust(20),"홈페이지")

for link in soup.find_all('a'):
    # print(link['href'])
    web2=urllib.request.urlopen("http://www.swu.ac.kr"+link['href'])
    soup2=BeautifulSoup(web2,"html.parser")
    Search_data=soup2.find('a', class_='btn btn_xl btn_blue_gray')
    Search_title=soup.find('a', class_='titl1')

    print(link.text.strip().ljust(20),end='')
    try:
        if Search_data.text == "홈페이지 바로가기":
            print(Search_data.get('href'))
            # if Search_data.text == NoneType:
            #     return
        else:
            print("홈페이지가 존재하지 않음")
    except AttributeError as err:
        print("홈페이지가 존재하지 않음")
