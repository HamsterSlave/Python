import requests
from bs4 import BeautifulSoup
import time

headers ={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
}
def judgment_sex(class_name):
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'

def get_links(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list>ul>li>a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tittles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_1 > span')
    imgs = soup.select('#floatRightBox  dix.js_box_clearfix > div_member_pic > a > img')
    names = soup.select('#floatRightBox  dix.js_box_clearfix > div_w240 > h6 > a')
    sexs = soup.select('#floatRightBox  dix.js_box_clearfix > div_member_pic > div')
    for tittle,address,price,img,name,sex in zip(tittles,addresses,prices,imgs,names,sexs):
        data = {
            'tittle': tittle.getText().strip(),
            'address': address.getText().strip(),
            'price': price.getText(),
            'img': img.get("src"),
            'name': name.getText(),
            'sex' :judgment_sex(sex.get("class"))
        }
        print(data)

if __name__ == '__main__':
    url = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0'.format(number) for number in range(1,14)]
    for single_url in url:
            get_links(single_url)
            time.sleep(2)
