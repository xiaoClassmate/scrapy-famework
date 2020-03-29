import scrapy
from bs4 import BeautifulSoup
from mizuno.items import MizunoItem
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor
import json

class MizunoSpider(CrawlSpider):
    name = 'mizuno'
    start_urls = []
    # rules = [
    #     Rule(
    #         LinkExtractor(allow=('/category/mens/')),
    #         callback = 'parse_list',
    #     )
    # ]
    def start_requests(self):
        urls1 = 'https://www.mizunousa.com/category/mens/apparel.do?category=APPAREL&c=100263.100385&sortby=newArrivalsDescend&pp=40&page='
        for i in range(1, 5):
            url1 = urls1 + str(i)
            # print(url)
            # print('************************************')
            yield scrapy.Request(url1, self.parse_list)

        urls2 = 'https://www.mizunousa.com/category/womens/apparel.do?category=APPAREL&c=100264.100408&sortby=newArrivalsDescend&pp=40&page='
        for i in range(1, 5):
            url2 = urls2 + str(i)
            # print(url)
            # print('------------------------------------')
            yield scrapy.Request(url2, self.parse_list)
        
    def parse_list(self, response):
        # print(response.url)
        domain = ['https://www.mizunousa.com']
        res = BeautifulSoup(response.body, 'lxml')
        # post = res.select('div.ml-grid-view-item')[0]
        for post in res.select('div.ml-grid-view-item'):
            if 'NewFlag' in post.select('img')[0]['src'] or 'NewProductFlag' in post.select('img')[0]['src'] or 'NewColorFlag' in post.select('img')[0]['src']:
            # print(post.select('img')[0]['src'])
                meta ={'A':'123', 'B':'456'}
                yield scrapy.Request(domain[0] + post.select('a')[0]['href'], self.parse_detail, meta = meta)
                # print('----------------------------------')
                # print(domain[0] + post.select('a')[0]['href'])
            else:
                pass
# domain[0] + post.select('a')[0]['href']
    def parse_detail(self, response):
        X = response.meta['B']
        print(X)
    #     res = BeautifulSoup(response.body, 'lxml')
    #     print(response.url)
    #     sporttag = res.select('ol.breadcrumb li')
    #     # print(tag)
    #     sport = []
    #     sportcls1 = sporttag[-2].text.strip()
    #     # sportcls1 = tag[-2].text.replace(' ','').split('\n')
    #     sportcls2 = sporttag[-3].text.strip()
    #     sport.append(sportcls2)
    #     sport.append(sportcls1)

    #     colortag = res.select('div.ml-product-swatches img')
    #     # print(colortag)
    #     colors = []
    #     for color in colortag:
    #         colors.append(color['title'])
  
    #     # print(colors)

    #     sizes = []
    #     sizetag = res.select('div.ml-product-swatches input.ml-product-optionUnSelected')
    #     # print(sizetag)
    #     for size in sizetag:
    #         # print(size['value'])
    #         sizes.append(size['value'])
    #      # print(sizes)

    #     rating = json.loads(res.select('script')[-6].text)
    #     try:
    #        ratingValue = (rating[0]['aggregateRating']['ratingValue'])
    #        ratingCount = (rating[0]['aggregateRating']['ratingCount'])
    #     #    print(ratingValue)
    #     #    print(ratingCount)
    #     except:
    #         ratingValue = 0
    #         ratingCount = 0

    #     try:
    #         statement = res.select('div#accordionTarget01 div.panel-body')[0]
    #         h1 = statement.select('h1')[0].text
    #         ptag = statement.select('p')
    #         ps=[]
    #         for plist in ptag:
    #             # ps.append(plist.text.replace('\n',' '))

    #         ps.append(h1).replace('\n',' ')
    #         material = str(ps)
    #         # print(h1)
    #         # print(ps)
    #         # print(material)
    #     except:
    #         statement = res.select('div#accordionTarget01 div.panel-body')[0]
    #         ptag = statement.select('p')
    #         ps=[]
    #         for plist in ptag:
    #             ps.append(plist.text.replace('\n',' '))

    #         material = str(ps)

    #     try:
    #         feature = res.select('div.dl-key-features')[0].text.strip().replace('\n',' ')
    #     except:
    #         feature = ''

    #     crawlitem = MizunoItem()
    #     crawlitem['Sports'] = sport
    #     crawlitem['Name'] = res.select('div.ml-product-name')[0].text.strip()
    #     crawlitem['Code'] = res.select('div.ml-product-code')[0].text.strip()
    #     price = res.select('span.productPricing')[0].text.strip()
    #     crawlitem['Price'] = price.replace('\n','')
    #     crawlitem['Colors'] = colors
    #     crawlitem['Size'] = sizes
    #     crawlitem['RatingValue'] = str(ratingValue).strip()
    #     crawlitem['RatingCount'] = str(ratingCount).strip()
    #     crawlitem['Material'] = material.strip()
    #     crawlitem['Feature'] = feature.replace('\n','')
    #     # print(crawlitem)
    #     return crawlitem