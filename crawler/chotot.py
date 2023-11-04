import requests
from bs4 import BeautifulSoup
import json
import csv
# from selenium import webdriver

def trade_spider(max_page):
    count_car = 0
    page = 1
    cars_array = {}
    cars = []
    while page <= max_page:
        url = "https://xe.chotot.com/mua-ban-oto?page=" + str(page)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('div', {'class' : 'ListAds_ListAds__rEu_9 col-xs-12 no-padding'}):
            for item in links.findAll('a'):
                cars.append(get_item("https://xe.chotot.com/"+item.get('href')))
                count_car += 1
        page += 1
        if count_car == 2000:
            print(count_car)
            break
    cars_array["cars"] = cars
    # writeJSONFile(cars_array)
    writeCSVFile(cars)
    # printToConsole(cars)

def get_item(item_url):
    source = requests.get(item_url)
    soup = BeautifulSoup(source.text, "html.parser")
    # soup = click_show_more(item_url)
    info = soup.findAll('div', {'class', 'media-body media-middle'})
    #Temporary store data crawled
    temp = {}
    temp["Tiêu đề"] = title_process(str(soup.find('h1' , {'class' : 'AdDecriptionVeh_adTitle__vEuKD'})))
    temp["Gia"] = cost_process(str(soup.find('span', {'itemprop' : 'price'})))

    for i in info:
        data_array = data_process(str(i))
        for i in range(len(data_array)):
            temp[data_array[0]] = data_array[1]

    #Filter data need to store
    car_item = filter_data(temp)
    return car_item

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

def filter_data(dict):
    car = {}
    if "Tiêu đề" in dict:
        car['car_title'] = dict["Tiêu đề"]
    if "Hãng" in dict:
        car['company'] = dict['Hãng']  
    if "Gia" in dict:
        car['cost'] = dict['Gia']
    if "Năm sản xuất" in dict:
        car['mfdate'] = dict['Năm sản xuất']
    if "Dòng xe" in dict:
        car['type'] = dict['Dòng xe']
    if "Số Km đã đi" in dict:
        car['mileage_v2'] = dict['Số Km đã đi']
    if "Tình trạng" in dict:
        car['condition_ad'] = dict['Tình trạng']
    if "Hộp số" in dict:
        car['gearbox'] = dict["Hộp số"]
    if "Nhiên liệu" in dict:
        car['fuel'] = dict["Nhiên liệu"]
    if "Xuất xứ" in dict:
        car['carorigin'] = dict['Xuất xứ']
    if "Kiểu dáng" in dict:
        car['cartype'] = dict['Kiểu dáng']
    if "Số chỗ" in dict:
        car['carseats'] = dict['Số chỗ']
    if "Chính sách bảo hành" in dict:
        car['veh_warranty_policy'] = dict['Chính sách bảo hành']
    if "Trọng lượng" in dict:
        car['veh_unladen_weight'] = dict['Trọng lượng']
    if "Trọng tải" in dict:
        car['veh_gross_weight'] = dict['Trọng tải']
    return car 

def writeJSONFile(dictionary):
    # Serializing json  
    json_object = json.dumps(dictionary, indent=len(dictionary.keys()), ensure_ascii=False)

    with open("sample301_400.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)

def writeCSVFile(data):
    with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['company', 'type', 'mfdate', 'mileage_v2', 'condition_ad', 'gearbox', 'fuel', 'carorigin', 'cartype', 'carseats', 'veh_warranty_policy', 'veh_unladen_weight', 'veh_gross_weight', 'cost'])
        for car in data:
            writer.writerow([car.get('company', ''), car.get('type', ''), car.get('mfdate', ''), car.get('mileage_v2', ''), car.get('condition_ad', ''), car.get('gearbox', ''), car.get('fuel', ''), car.get('carorigin', ''), car.get('cartype', ''), car.get('carseats', ''), car.get('veh_warranty_policy', ''), car.get('veh_unladen_weight', ''), car.get('veh_gross_weight', ''), car.get('cost', '')])

def printToConsole(dictionary):
    index = 1
    for i in dictionary:
        print(index)
        for key, value in i.items():
            print(key + ': ', end = '')
            print(value)
        print("------------------")
        index += 1

trade_spider(30)