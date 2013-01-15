from bs4 import BeautifulSoup
import urllib2

url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20130114&page='
for i in range(21):
    url = url+str(i)
    handle = urllib2.urlopen(url)
    data = handle.read()
    soup = BeautifulSoup(data)
    for text in soup.find_all("div",class_="tit5"):
        print(text.contents[1].string.encode("utf-8"))
    url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20130114&page='
