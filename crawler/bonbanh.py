import requests
from bs4 import BeautifulSoup
import csv
from unidecode import unidecode

def get_data(max_page):
    page = 1
    while page <= max_page:
        url = "https://bonbanh.com/oto/page," + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cars = soup.find_all('li', class_ = 'car-item')
        for car in cars:
            link = 'https://bonbanh.com/' + car.find('a').get('href')
            with open('bonbanh.csv', 'a', newline='', encoding ='utf8') as file:
                writer = csv.writer(file)
                get_detail(link,writer)
        page += 1 


with open('bonbanh.csv', 'w', newline='', encoding ='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(['Năm sản xuất', 'Tình trạng xe', 'Số km đã đi', 'Xuất xứ', 'Kiểu dáng', 'Hộp số', 'Động cơ', 
    'Màu ngoại thất','Màu nội thất', 'Số chỗ', 'Số cửa', 'Dẫn động trước', 'Tên xe', 'Giá xe'])

def get_detail(url,writer):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    car_detail = [car.text.strip() for car in soup.find_all('span', class_ = 'inp')]
    my_list = []
    my_list.extend(car_detail[:2])
    my_list.extend(car_detail[-10:])
    my_list.append(soup.find('i').text)
    my_list.append(soup.find('h1').text.strip().split('- ')[-1])
    writer.writerow(my_list)

get_data(1839)