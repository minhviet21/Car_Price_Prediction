import requests
from bs4 import BeautifulSoup
import csv

def trade_spider(max_page):
    count_car = 0
    page = 1
    while page <= max_page:
        url = "https://xe.chotot.com/mua-ban-oto?page=" + str(page)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('div', {'class' : 'ListAds_ListAds__rEu_9 col-xs-12 no-padding'}):
            for item in links.findAll('a'):
                car = get_item("https://xe.chotot.com/"+item.get('href'))
                write_car_to_csv(car)
                count_car += 1
        page += 1
        if count_car == 30000:
            print(count_car)
            break

with open('chotot.csv', 'w', newline='', encoding ='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tiêu đề','Hãng', 'Dòng xe', 'Năm sản xuất', 'Số km đã đi', 'Tình trạng', 'Hộp số', 'Nhiên liệu', 'Xuất xứ', 'Kiểu dáng', 'Số chỗ', 'Giá xe'])

def get_item(item_url):
    source = requests.get(item_url)
    soup = BeautifulSoup(source.text, "html.parser")
    info = soup.findAll('div', {'class', 'media-body media-middle'})
    temp = {}
    temp["Tiêu đề"] = title_process(str(soup.find('h1' , {'class' : 'AdDecriptionVeh_adTitle__vEuKD'})))
    temp["Giá xe"] = cost_process(str(soup.find('span', {'itemprop' : 'price'})))

    for i in info:
        data_array = data_process(str(i))
        for i in range(len(data_array)):
            temp[data_array[0]] = data_array[1]
            
    return temp

def title_process(title):
    begin = title.find("<!-- --> <!-- -->") + 17
    end = title.find("<\h1>") - 4
    return title[begin:end]

def cost_process(salary):
    begin = salary.find("<span itemprop=\"price\">") + len("<span itemprop=\"price\">")
    end = salary.find("<!-- -->")
    return salary[begin:end]

def data_process(data):
    category = ""
    value = ""
    begin = data.find("<span><span>")
    check = data.find("</span><a ")
    if check != -1:
        middle = data.find('</span><a class="AdParam_adParamValue__IfaYa"')
        brand = data.find('itemprop="carbrand">')
        model = data.find('itemprop="carmodel">')
        end = data.find("</a></span></div>")
        category = data[begin + len("<span><span>"):middle - 2]
        if brand != -1:
            value = data[brand + len('itemprop="carbrand">'):end]
        else:
            value = data[model + len('itemprop="carmodel">'):end]
    else:
        middle = data.find('</span><span class="AdParam_adParamValue__IfaYa"')
        end = data.find("</span></span>")
        category = data[begin + len("<span><span>"):middle - 2]
        value_pre = data[middle + len("</span><span class=\"AdParam_adParamValue__IfaYa\">"):end]
        check = value_pre.find('">')
        value = value_pre[check + 2:]
    return [category, value]

def write_car_to_csv(car):
    with open('chotot.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([car.get('Tiêu đề', ''),car.get('Hãng', ''), car.get('Dòng xe', ''), car.get('Năm sản xuất', ''), car.get('Số km đã đi', ''), car.get('Tình trạng', ''), car.get('Hộp số', ''), car.get('Nhiên liệu', ''), car.get('Xuất xứ', ''), car.get('Kiểu dáng', ''), car.get('Số chỗ', ''), car.get('Giá xe', '')])

trade_spider(1000)