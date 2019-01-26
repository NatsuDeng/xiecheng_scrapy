# -*- coding: utf-8 -*-
import json

import scrapy
from prettytable import PrettyTable


class XcSpider(scrapy.Spider):
    name = 'xc'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://flights.ctrip.com/itinerary/api/12808/products']

    def __init__(self,dcity,acity,date):
        super(XcSpider, self).__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Content-Type": "application/json",
        }

        self.city = {'阿尔山': 'YIE', '阿克苏': 'AKU', '阿拉善右旗': 'RHT', '阿拉善左旗': 'AXF', '阿勒泰': 'AAT', '阿里': 'NGQ', '澳门': 'MFM',
                '安庆': 'AQG', '安顺': 'AVA', '鞍山': 'AOG', '巴彦淖尔': 'RLK', '百色': 'AEB', '包头': 'BAV', '保山': 'BSD',
                '北海': 'BHY',
                '北京': 'BJS', '白城': 'DBC', '白山': 'NBS', '毕节': 'BFJ', '博乐': 'BPL', '重庆': 'CKG', '昌都': 'BPX', '常德': 'CGD',
                '常州': 'CZX', '朝阳': 'CHG', '成都': 'CTU', '池州': 'JUH', '赤峰': 'CIF', '揭阳': 'SWA', '长春': 'CGQ', '长沙': 'CSX',
                '长治': 'CIH', '承德': 'CDE', '沧源': 'CWJ', '达县': 'DAX', '大理': 'DLU', '大连': 'DLC', '大庆': 'DQA', '大同': 'DAT',
                '丹东': 'DDG', '稻城': 'DCY', '东营': 'DOY', '敦煌': 'DNH', '芒市': 'LUM', '额济纳旗': 'EJN', '鄂尔多斯': 'DSN',
                '恩施': 'ENH',
                '二连浩特': 'ERL', '佛山': 'FUO', '福州': 'FOC', '抚远': 'FYJ', '阜阳': 'FUG', '赣州': 'KOW', '格尔木': 'GOQ',
                '固原': 'GYU',
                '广元': 'GYS', '广州': 'CAN', '贵阳': 'KWE', '桂林': 'KWL', '哈尔滨': 'HRB', '哈密': 'HMI', '海口': 'HAK',
                '海拉尔': 'HLD',
                '邯郸': 'HDG', '汉中': 'HZG', '杭州': 'HGH', '合肥': 'HFE', '和田': 'HTN', '黑河': 'HEK', '呼和浩特': 'HET',
                '淮安': 'HIA',
                '怀化': 'HJJ', '黄山': 'TXN', '惠州': 'HUZ', '鸡西': 'JXA', '济南': 'TNA', '济宁': 'JNG', '加格达奇': 'JGD',
                '佳木斯': 'JMU',
                '嘉峪关': 'JGN', '金昌': 'JIC', '金门': 'KNH', '锦州': 'JNZ', '嘉义': 'CYI', '西双版纳': 'JHG', '建三江': 'JSJ',
                '晋江': 'JJN',
                '井冈山': 'JGS', '景德镇': 'JDZ', '九江': 'JIU', '九寨沟': 'JZH', '喀什': 'KHG', '凯里': 'KJH', '康定': 'KGT',
                '克拉玛依': 'KRY',
                '库车': 'KCA', '库尔勒': 'KRL', '昆明': 'KMG', '拉萨': 'LXA', '兰州': 'LHW', '黎平': 'HZH', '丽江': 'LJG', '荔波': 'LLB',
                '连云港': 'LYG', '六盘水': 'LPF', '临汾': 'LFQ', '林芝': 'LZY', '临沧': 'LNJ', '临沂': 'LYI', '柳州': 'LZH',
                '泸州': 'LZO',
                '洛阳': 'LYA', '吕梁': 'LLV', '澜沧': 'JMJ', '龙岩': 'LCX', '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '漠河': 'OHE',
                '牡丹江': 'MDG', '马祖': 'MFK', '南昌': 'KHN', '南充': 'NAO', '南京': 'NKG', '南宁': 'NNG', '南通': 'NTG', '南阳': 'NNY',
                '宁波': 'NGB', '宁蒗': 'NLH', '攀枝花': 'PZI', '普洱': 'SYM', '齐齐哈尔': 'NDG', '黔江': 'JIQ', '且末': 'IQM',
                '秦皇岛': 'BPE',
                '青岛': 'TAO', '庆阳': 'IQN', '衢州': 'JUZ', '日喀则': 'RKZ', '日照': 'RIZ', '三亚': 'SYX', '厦门': 'XMN', '上海': 'SHA',
                '深圳': 'SZX', '神农架': 'HPG', '沈阳': 'SHE', '石家庄': 'SJW', '塔城': 'TCG', '台州': 'HYN', '太原': 'TYN',
                '扬州': 'YTY',
                '唐山': 'TVS', '腾冲': 'TCZ', '天津': 'TSN', '天水': 'THQ', '通辽': 'TGO', '铜仁': 'TEN', '吐鲁番': 'TLQ', '万州': 'WXN',
                '威海': 'WEH', '潍坊': 'WEF', '温州': 'WNZ', '文山': 'WNH', '乌海': 'WUA', '乌兰浩特': 'HLH', '乌鲁木齐': 'URC',
                '无锡': 'WUX',
                '梧州': 'WUZ', '武汉': 'WUH', '武夷山': 'WUS', '西安': 'SIA', '西昌': 'XIC', '西宁': 'XNN', '锡林浩特': 'XIL',
                '香格里拉(迪庆)': 'DIG',
                '襄阳': 'XFN', '兴义': 'ACX', '徐州': 'XUZ', '香港': 'HKG', '烟台': 'YNT', '延安': 'ENY', '延吉': 'YNJ', '盐城': 'YNZ',
                '伊春': 'LDS',
                '伊宁': 'YIN', '宜宾': 'YBP', '宜昌': 'YIH', '宜春': 'YIC', '义乌': 'YIW', '银川': 'INC', '永州': 'LLF', '榆林': 'UYN',
                '玉树': 'YUS',
                '运城': 'YCU', '湛江': 'ZHA', '张家界': 'DYG', '张家口': 'ZQZ', '张掖': 'YZY', '昭通': 'ZAT', '郑州': 'CGO',
                '中卫': 'ZHY',
                '舟山': 'HSN',
                '珠海': 'ZUH', '遵义(茅台)': 'WMT', '遵义(新舟)': 'ZYI'}
        date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
        self.request_payload = {"flightWay": "Oneway",
                           "classType": "ALL",
                           "hasChild": 'false',
                           "hasBaby": 'false',
                           "searchIndex": 1,
                           "portingToken": "3fec6a5a249a44faba1f245e61e2af88",
                           # "airportParams": [
                           #     {"dcity": self.city.get(dcity), "acity": self.city.get(acity), "dcityname": dcity,
                           #      "acityname": acity,
                           #      "date": date}]}
                            "airportParams": [
                                {"dcity": self.city.get(dcity), "acity": self.city.get(acity), "dcityname": dcity, "acityname": acity,
                                 "date": date}]}
        self.meta={"acity":acity,"dcity":dcity,"date":date}

    def start_requests(self):
        cookie = '_abtest_userid=dd5e7435-9d98-432e-ad4a-a8b0b164fdb0; gad_city=1580b16db58f18f4e6710a5322448203; _ga=GA1.2.1249578506.1548422094; _gid=GA1.2.1530883516.1548422094; MKT_Pagesource=PC; _RSG=2xqp.Ztvlv6KDj9kyk1OEA; _RDG=28012f52ad0a0a24e733e4e65837c11d73; _RGUID=6e6fe778-fecf-4ec2-a398-06ef2e26d354; DomesticUserHostCity=SIA|%ce%f7%b0%b2; appFloatCnt=1; FD_SearchHistorty={"type":"S","data":"S%24%u9752%u5C9B%28TAO%29%24TAO%242019-02-12%24%u5317%u4EAC%28BJS%29%24BJS%24%24%24"}; _gat=1; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1549069264968; _RF1=123.138.79.10; manualclose=1; _bfa=1.1548422090933.3n6525.1.1548433053594.1548464461409.3.21; _bfs=1.2; MKT_OrderClick=ASID=&CT=1548464477898&CURL=https%3A%2F%2Fflights.ctrip.com%2Fitinerary%2Foneway%2Ftao-bjs%3Fdate%3D2019-02-12&VAL={"pc_vid":"1548422090933.3n6525"}; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1548464477903%7D%5D; _jzqco=%7C%7C%7C%7C%7C1.1790562638.1548422098336.1548464465045.1548464477969.1548464465045.1548464477969.0.0.0.20.20; __zpspc=9.4.1548464465.1548464477.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D100101991%26v1%3D21%26v2%3D20'
        cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ')}
        data = json.dumps(self.request_payload)
        yield scrapy.Request(self.start_urls[0],method='POST',headers=self.headers,body=data,cookies=cookie_dict,callback=self.parse,meta={'meta':self.meta})

    def parse(self, response):
        meta = response.meta['meta']
        acity=meta["acity"]
        dcity=meta["dcity"]
        date=meta["date"]
        print('#'*50)
        print(type(response.body))
        res = response.body
        res = res.decode('utf-8')
        routeList = json.loads(res).get('data').get('routeList')
        table = PrettyTable(
            ["Airline", "FlightNumber", "DepartureDate", 'ArrivalDate', 'PunctualityRate', 'LowestPrice'])

        for route in routeList:
            if len(route.get('legs')) == 1:
                info = {}
                legs = route.get('legs')[0]
                flight = legs.get('flight')
                info['Airline'] = flight.get('airlineName')
                info['FlightNumber'] = flight.get('flightNumber')
                info['DepartureDate'] = flight.get('departureDate')[-8:-3]
                info['ArrivalDate'] = flight.get('arrivalDate')[-8:-3]
                info['PunctualityRate'] = flight.get('punctualityRate')
                info['LowestPrice'] = legs.get('characteristic').get('lowestPrice')

                table.add_row(info.values())

        print(dcity,'------->',acity,date)
        print(table)

