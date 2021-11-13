import os
import requests
import urllib.request
from bs4 import BeautifulSoup

# 세기말 풋사과 보습학원 크롤링

# 가져올 웹툰 url
url = "https://comic.naver.com/webtoon/list?titleId=761722&weekday=fri"

# 크롤링 하기 전에 우회하기, 우회하기 위한 헤더 수정
headers = {'User-Agent': 'Mozilla/5.0 (Window NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'}

html = requests.get(url, headers=headers)
result = BeautifulSoup(html.content, "html.parser")

# 이미지 저장하기
# urllib.request.urlretrieve(이미지 경로, 저장경로+저장할파일명(index)+".jpg")
# 웹툰제목 가져오기
name=result.find("span",{"class","wrt_nm"}).parent.get_text().strip().split('\n')


os.mkdir(name[0])
print(name[0])
os.chdir("C:\github\proj1\\"+name[0])    # 제목 폴더로 이동

# 회차별 제목 가져오기
title = result.findAll("td",{"class","title"})

for i in title:
    os.mkdir((i.text).strip())  # 폴더 안에 회차별 폴더 만들기/ strip=제목 공백 제거
    os.chdir(os.getcwd()+"\\"+(i.text).strip()) # ghlckquf vhfejfh dlehd

    url2="https://comic.naver.com"+i.a['href']
    html2=requests.get(url2, headers = headers)
    result2=BeautifulSoup(html2.content, "html.parser")

    webtoonImg = result2.find("div", {"class", "wt_viewer"}).findAll("img")   # class가 wt_viewer인거 에서 div태그찾고 그 안에 img태그 다 찾기
    num = 1 # 이미지 저장 이름

    for j in webtoonImg:
        imgName = os.getcwd() + "//" + str(num) + ".jpg"    # 저장될 위채 + 저장명 + 확장자
        with open(imgName, "wb") as file:
            src = requests.get(j['src'], headers=headers)     # 해더 우회해서 이미지 src가져오는 ㄴ과정
            file.write(src.content)                         # 이미지 저장
        num = num + 1                                       # 이미지 저장 이름 하나씩 늘리기

    os.chdir("..")  # 작업디렉토리 변경, 이전 디렉토리로 이동

    print((i.text).strip()+" 한회 이미지 저장 끝") # 한회 이미지 저장 끝
