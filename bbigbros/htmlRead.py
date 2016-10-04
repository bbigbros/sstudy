 #URL을 열고 HTML을 읽는 모듈, urllib을 불러온다

from urllib.request import urlopen
from bs4 import BeautifulSoup

def htmlRead(url):
    res = urlopen(url).read()
    readhtml = BeautifulSoup(res)
    return readhtml


if __name__ == "__main__":
    inputUrl = input("URI 입력하세요 > ")
    print(inputUrl)
    readPage = htmlRead(inputUrl)
    print(readPage)
