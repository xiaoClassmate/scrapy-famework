# -*- coding: utf-8 -*-
import requests
import scrapy
import json
from bs4 import BeautifulSoup
from reebok.items import ReebokItem

class ReebokScrapy(scrapy.Spider):
    name = 'reebok'
    start_urls = []

    def start_requests(self):
        url_men = 'https://www.reebok.com/us/men-apparel-new_arrivals?start=0'
        # for i in range(0, 193, 48):
            # urls_men = url_men + str(i)
        yield scrapy.Request(url_men, self.parse_list)

        # url_women = 'https://www.reebok.com/us/women-apparel-new_arrivals?start='
        # for i in range(0, 241, 48):
        #     urls_women = url_women + str(i)
        #     yield scrapy.Request(urls_women, self.parse_list)

    def parse_list(self, response):
        # domain = 'https://www.reebok.com/'
        # res = BeautifulSoup(response.body, 'lxml')
        # for product in res.select('div.gl-product-card__media'):
            # meta = {
            #     'ImageUrl' : domain + product.select('a')[0]['href']
            # }
            yield scrapy.Request('https://www.reebok.com/us/2019-crossfit-games-fraser-replica-jersey/BI1930.html', self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body, 'lxml')
        # domain = 'https://www.reebok.com/'
        # print('----------------------------------------------------------------')
        # print('I just confirm information of def parse url have correct arrival')
        # print('----------------------------------------------------------------')

        # global ImageUrl
        # try:
        #     if 'Personalize Yours' in res.select('div.gl-badge.gl-badge--large.gl-badge--regular.badge_position___2q9Kl')[0]:
        #         ImageUrl = response.meta['ImageUrl']
        # except:
        #     ImageUrl = 'None'
            
        # global Gender
        # try:
        #     if 'Classics' in res.select('div.breadcrumb___2DviW')[0].text:
        #         Gender = 'unisex'
        #     elif 'Men' in res.select('div.breadcrumb___2DviW')[0].text:
        #         Gender = 'men'
        #     else:
        #         Gender = 'women'
        # except:
        #     pass

        # Sport = []
        # Sport.append(res.select('div.subtitle___2z5HL.gl-label.gl-label--l')[0].text)

        # Name = res.select('h1.product_information_title___2rG9M.product_title.gl-heading.gl-heading--m')[0].text

        # MinPrice = float(res.select('div.gl-price')[0].text.split('$')[-1].strip())
        # MaxPrice = float(res.select('div.gl-price')[0].text.split('$')[-1].strip())

        json_code = res.select('script')[1].text
        # file_name = 'reebok.json'
        # with open (file_name, 'w') as f:
        #     f.write(json_code)
        #     print('OK')

        Color = []
        Color_var = json.loads(json_code.split('window.DATA_STORE = ')[1].strip(';'))
        try:
            for i in range(0, 10):
                # print(i)
                Color.append(Color_var['product']['productData']['product_link_list'][i]['default_color'])
                # print(Color)
        except:
            pass
        if Color == []:
            Color.append(Color_var['product']['productData']['attribute_list']['search_color'])

        
        # Size = json.loads()
        # print(Size)
        # Select_Size = res.select('li.gl-menu__item button.gl-menu__element')
        # for Sizelist in Select_Size:
        #     Size.append(Sizelist.text)

        # StyleNumber = res.select('ul.bullet_list___1JjG2.gl-list.bullet_list--half-width___35Abt li.gl-vspacing-m')[-1].text.split(':')[-1].strip()

        # Feature = []
        # Select_Feature = res.select('div.wrapper___1HYKp.offset-l-1.col-l-11.offset-xl-2.col-xl-10.offset-hg-3.col-hg-9 p')
        # for Featurelist in Select_Feature:
        #     Feature.append(Featurelist.text)

        # Material = []
        # Material_left = []
        # Material_right = []
        # Select_Material_left = res.select('ul.bullet_list___1JjG2.gl-list.bullet_list--half-width___35Abt')[0]
        # Select_Material_right = res.select('ul.bullet_list___1JjG2.gl-list.bullet_list--half-width___35Abt')[1]
        # for Materiallist in Select_Material_left:
        #     Material_left.append(Materiallist.text)
        # for Materiallist in Select_Material_right:
        #     Material_right.append(Materiallist.text)
        # Material_right = Material_right[0:-2]
        # Material.append(''.join(Material_left))
        # Material.append(''.join(Material_right))
        
        # item = ReebokItem()
        # # item['Sport'] = Sport
        # # item['Name'] = Name
        # # item['MinPrice'] = MinPrice
        # # item['MaxPrice'] = MaxPrice
        # item['Color'] = Color
        # # item['StyleNumber'] = StyleNumber
        # # item['Feature'] = Feature
        # # item['Material'] = Material
        # # item['Size'] = Size
        # # item['ImageUrl'] = ImageUrl
        # # item['Gender'] = Gender
        # # item['AverageRating'] = AverageRating
        # # item['ReviewNumber'] = ReviewNumber
        # # return item


