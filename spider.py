import bs4   #网页解析，获取数据
import re   # 正则表达式
import urllib.request   #制定URL，获取网页数据
import xlwt   #进行excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # #1.爬取网页
    # datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250.xls"
    # #3.保存数据
    # saveData(savepath)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用获取页面信息的函数 10次
        url = baseurl + str(i*25)
        html = askURL(url)  #保存获取到的网页源码

        # 2.逐一解析数据

    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {  #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36"
    }
    #用户代理：表示告诉豆瓣服务器，我们是什么类型的机器(本质上告诉浏览器我们可以接受什么水平的文件)
    request = urllib.request.Request(url,headers= head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html





#保存数据
def saveData(savepath):
    print("save.....")


if __name__ == '__main__':
    askURL("https://movie.douban.com/top250?start=")