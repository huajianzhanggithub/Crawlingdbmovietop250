from lxml import etree
import requests
import time
for a in range(10):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(a*25)
    data = requests.get(url).text
    # print(data)
    s = etree.HTML(data)
    file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for div in file:
        movie_ranking=div.xpath('./div/div[1]/em/text()')[0]
        movies_name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        movies_score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        movies_href = div.xpath('./div/div[2]/div[1]/a/@href')[0]
        movies_number = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0].strip("(").strip( ).strip(")")
        movie_scrible = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')
        # time.sleep(1)
        if len(movie_scrible)>0:
            print("{}.{} {} {} {} {}".format(movie_ranking,movies_name,movies_href,movies_score,movies_number,movie_scrible[0]))
        else:
            print("{}.{} {} {} {}".format(movie_ranking,movies_name,movies_href,movies_score,movies_number))
#--------------------- 
#作者：云南省高校数据化运营管理工程研究中心 
#来源：CSDN 
#原文：https://blog.csdn.net/m0_37788308/article/details/80378042 
#版权声明：本文为博主原创文章，转载请附上博文链接！
