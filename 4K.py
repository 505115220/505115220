import requests
from lxml import etree
import datetime


# 爬取今日壁纸
url = "https://www.bingimg.cn"
res = requests.get(url).text
html_file = etree.HTML(res)
div_list = html_file.xpath('//*[@id="a_img_down_uhd"]')
v_list = []
for index in range(len(div_list)):
    # links[index]返回的是一个字典
    if (index % 2) == 0:
        scorces = div_list[index].attrib
        
        for k, v in scorces.items():
            v_list.append(v)
        print(v_list[1])
list2 = v_list[1][2:]
list3 = "https://www.bingimg.cn" + list2
print(list2)
print(list3)

# 练习目标图片
# https://www.bingimg.cn/down/uhd/OHR.AbbeyGardens_ZH-CN4831631801_UHD.jpg

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.25 '
                  'Safari/537.36 Core/1.70.3861.400 '
                  'QQBrowser/10.7.4313.400'
}
pic = requests.get(list3, headers=headers)
print(pic.status_code)

dir_name = r"C:\Users\Ashuai\AppData\Local\Microsoft\BingWallpaperApp\WPImages"  #这里需要替换您自己的bing壁纸软件的图片存放目录

# 设置文件名
today = datetime.date.today()
today = str(today)
name = "\\" + today[0:4] + today[5:7] + today[8:] + ".jpg"

file_name = dir_name + name  # 文件储存地址
with open(file_name, 'wb') as f:  # 把图片数据写入本地，wb表示二进制储存
    for chunk in pic.iter_content(chunk_size=128):
        f.write(chunk)
