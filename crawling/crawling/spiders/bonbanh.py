import scrapy

class DetailSpider(scrapy.Spider):
    name = "bonbanh"
    start_urls = ["https://bonbanh.com/oto"]

    def parse(self, response):
        bonbanh_page_links = response.css("li.car-item  a::attr(href)")
        yield from response.follow_all(bonbanh_page_links, self.parse_bonbanh)

        next_page = response.css("div.navpage span.bbl::attr(url)")[-2].get()
        if next_page is not None and next_page != 'https://bonbanh.com/oto/page,51': 
            yield response.follow(next_page, callback=self.parse)

    def parse_bonbanh(self, response):
        details = response.css("div.txt_input span.inp::text")

        yield {
            "Tên xe" :  response.css("span b i::text").get(),
            "Năm sản xuất" :  details[0].get().strip(),
            "Tình trạng" :    details[1].get().strip(),
            "Số km đã đi" :   details[-8].get().strip(),
            "Xuất xứ" :       details[-7].get().strip(),
            "Kiểu dáng" :     details[-6].get().strip(),
            "Hộp số" :        details[-5].get().strip(),
            "Động cơ" :       details[-4].get().strip(),
            "Màu ngoại thất": details[-3].get().strip(),
            "Màu nội thất":   details[-2].get().strip(),
            "Dẫn động sau":   details[-1].get().strip(),
            "Giá xe"  :  response.css("div.title h1::text").get().split("-")[-1].strip()
        }
