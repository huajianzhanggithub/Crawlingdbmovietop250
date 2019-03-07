from lxml import etree
import requests
from time import sleep
from os import path,listdir,rename
import os
#for a in range(10):
#    url = 'https://movie.douban.com/top250?start={}&filter='.format(a*25)
#    data = requests.get(url).text
#    # print(data)
#    s = etree.HTML(data)
#    file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')
#    for div in file:
#        movie_ranking=div.xpath('./div/div[1]/em/text()')[0]
#        movies_name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
#        movies_score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
#        movies_href = div.xpath('./div/div[2]/div[1]/a/@href')[0]
#        movies_number = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0].strip("(").strip( ).strip(")")
#        movie_scrible = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')
#        # time.sleep(1)
#        if len(movie_scrible)>0:
#            print("{}.{} {} {} {} {}".format(movie_ranking,movies_name,movies_href,movies_score,movies_number,movie_scrible[0]))
#        else:
#            print("{}.{} {} {} {}".format(movie_ranking,movies_name,movies_href,movies_score,movies_number))
def crawlingdbmovietop250():
    list1=[]

    for a in range(10):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(a*25)
        data = requests.get(url).text
        # print(data)
        s = etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for div in file:
            movies_ranking=div.xpath('./div/div[1]/em/text()')[0]
            movies_name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
            movies_score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
            #sleep(3)
            movies_rns="排名第{}-{}-评分{}".format(movies_ranking,movies_name,movies_score)
            list1.append(movies_rns)
    return list1
def changemoviesname(movies_rns):
    read_file_dir = "D:/娱乐/电影"

    files = listdir(read_file_dir) # 列出当前目录下所有的文件
    try:
    
            for filename in files:
                oldmoviename = path.splitext(filename) # 分离文件名字和后缀
                if oldmoviename[0].count(movies_rns.split("-")[1])!=0:  #检测扩展名
                    newname = movies_rns+oldmoviename[1]  #改新的新扩展名
                    os.chdir(read_file_dir)  
                    os.rename(filename,newname)
                    print(os.path.basename(filename)+' -> '+ os.path.basename(newname))
    
    except :
        pass
if __name__=="__main__":
    movieslist=crawlingdbmovietop250()
    for ml in movieslist:
        changemoviesname(ml)
        #movieslist.pop(movieslist.index(ml))
