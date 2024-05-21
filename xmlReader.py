import requests
import xml.etree.ElementTree as ET
api_key = '5758303589'

class XmlReader:
    @staticmethod
    def FoodMenuReader(serviceArea_name):               # serviceArea name and return food menu list
        page_num = '1'
        flag = False
        menu = []
        while True:
            url = 'https://data.ex.co.kr/openapi/restinfo/restBestfoodList?key=test&type=xml&numOfRows=99&pageNo='+page_num+'&stdRestNm='+serviceArea_name
        # url 불러오기
            response = requests.get(url)
            root = ET.fromstring(response.text)
            flag = root.find("list")

            if flag == None:
                break
            for list in root.iter("list"):
                menu.append(list.findtext("foodNm"))
            page_num = str(int(page_num)+1)
        return menu

    @staticmethod
    def GasstationReader(serviceArea_name):         #serviceArea to Gasstation company and price
        page_num = '1'
        flag = False
        oil_price = {}
        while True:
            url = 'https://data.ex.co.kr/openapi/business/curStateStation?key=test&type=xml&numOfRows=99&pageNo='+page_num+'&serviceAreaName='+serviceArea_name
            # url 불러오기
            response = requests.get(url)
            root = ET.fromstring(response.text)
            flag = root.find("list")

            if flag == None:
                break
            for list in root.iter("list"):
                company_name = list.findtext("oilCompany")
                oil_price[company_name] = {'disel':0,'gasoline':0}
                oil_price[company_name]['disel'] = list.findtext("diselPrice")
                oil_price[company_name]['gasoline'] = list.findtext("gasolinePrice")

            page_num = str(int(page_num) + 1)
        #print(oil_price)   If you don't know return type, you have to remove comment and check the result
        return oil_price

    @staticmethod
    def AllServiceAreaReader(ex_name):      # Routename to all service area
        ex_code = XmlReader.ExnameToExcode(ex_name)
        page_num = '1'
        flag = False
        service_area_list = []
        # while True:
        #     url = 'https://data.ex.co.kr/openapi/locationinfo/locationinfoRest?key=' + api_key + '&type=xml&routeNo=' + ex_code + '&numOfRows=99&pageNo='+page_num
        #     # url 불러오기
        #     response = requests.get(url)
        #     root = ET.fromstring(response.text)
        #     flag = root.find("list")
        #     if flag == None:
        #         break
        #     for list in root.iter("list"):
        #         service_area_list.append(list.findtext("unitName"))
        #
        #     page_num = str(int(page_num) + 1)

        url = 'https://data.ex.co.kr/openapi/restinfo/hiwaySvarInfoList?key='+api_key+'&type=xml&routeCd='+ex_code
        # url 불러오기
        response = requests.get(url)
        root = ET.fromstring(response.text)

        for list in root.iter("list"):
            if '휴게소' == list.findtext("svarGsstClssNm"):
                service_area_list.append(list.findtext("svarNm"))

        return service_area_list

    @staticmethod
    def serviceAreaLocationReader(serviceArea_name):
        #serviceArea_code = serviceAreaNameToServiceAreaCode(serviceArea_name)
        page_num = '1'
        while True:
            url = 'https://data.ex.co.kr/openapi/locationinfo/locationinfoRest?key='+api_key+'&type=xml&numOfRows=99&pageNo='+page_num
            response = requests.get(url)
            root = ET.fromstring(response.text)
            flag = False
            location = {'x':0,'y':0}
            for list in root.iter("list"):
                if serviceArea_name+'휴게소' == list.findtext("unitName"):
                    flag = True
                    location['x'] = list.findtext('xValue')
                    location['y'] = list.findtext('yValue')
                    break
            if flag:
                break
            page_num = str(int(page_num) + 1)
        return location

    @staticmethod
    def AllExReader(): # all route name
        page_num = '1'
        ex_set = set()
        # while True:
        #     url = 'https://data.ex.co.kr/openapi/locationinfo/locationinfoRest?key='+api_key+'&type=xml&numOfRows=99&pageNo='+page_num
        #     # url 불러오기
        #     response = requests.get(url)
        #     root = ET.fromstring(response.text)
        #     flag = root.find("list")
        #     if flag == None:
        #         break
        #     for i in root.iter("list"):
        #        ex_set.add(i.findtext("routeName"))
        #     page_num = str(int(page_num) + 1)
        url = 'https://data.ex.co.kr/openapi/restinfo/hiwaySvarInfoList?key='+api_key+'&type=xml'
        # url 불러오기
        response = requests.get(url)
        root = ET.fromstring(response.text)
        for i in root.iter("list"):
            ex_set.add(i.findtext("routeNm"))
        ex_list = list(ex_set)
        return ex_list

    @staticmethod
    def ExnameToExcode(ex_name):
        url = 'https://data.ex.co.kr/openapi/restinfo/hiwaySvarInfoList?key='+api_key+'&type=xml'
        response = requests.get(url)
        root = ET.fromstring(response.text)
        flag = root.find("list")

        for list in root.iter("list"):
            if ex_name == list.findtext("routeNm"):
                route_code = list.findtext("routeCd")
                return route_code

    @staticmethod
    def serviceAreaNameToServiceAreaCode(serviceArea_name):
        url = 'https://data.ex.co.kr/openapi/restinfo/restBestfoodList?key='+api_key+'&type=xml&numOfRows=99&pageNo=1&stdRestNm='+serviceArea_name
        response = requests.get(url)
        root = ET.fromstring(response.text)
        flag = root.find("list")
        for list in root.iter("list"):
            serviceArea_code = list.findtext("restCd")
            return serviceArea_code

