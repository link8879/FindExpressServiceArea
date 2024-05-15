import requests
import xml.etree.ElementTree as ET
api_key = '5758303589'

def FoodMenuReader(serviceArea_name):               # return food menu list
    page_num = '1'
    flag = False
    menu = []
    while True:
        url = 'https://data.ex.co.kr/openapi/restinfo/restBestfoodList?key=test&type=xml&numOfRows=10&pageNo='+page_num+'&stdRestNm='+serviceArea_name
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


    pass
def GasstationReader(serviceArea_name):
    page_num = '1'
    flag = False
    oil_price = {}
    while True:
        url = 'https://data.ex.co.kr/openapi/business/curStateStation?key=test&type=xml&numOfRows=10&pageNo='+page_num+'&serviceAreaName='+serviceArea_name
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

def AllServiceAreaReader(ex_name):      #
    ex_code = ExnameToExcode(ex_name)
    page_num = '1'
    flag = False
    service_area_list = []
    while True:
        url = 'https://data.ex.co.kr/openapi/locationinfo/locationinfoRest?key=' + api_key + '&type=xml&routeNo=' + ex_code + '&numOfRows=10&pageNo='+page_num
        # url 불러오기
        response = requests.get(url)
        root = ET.fromstring(response.text)
        flag = root.find("list")
        if flag == None:
            break
        for list in root.iter("list"):
            service_area_list.append(list.findtext("unitName"))

        page_num = str(int(page_num) + 1)
    print(service_area_list)
    return service_area_list

def ExnameToExcode(ex_name):
    url = 'https://data.ex.co.kr/openapi/business/curStateStation?key=test&type=xml&numOfRows=10&pageNo=1&routeName='+ex_name
    response = requests.get(url)
    root = ET.fromstring(response.text)
    flag = root.find("list")
    for list in root.iter("list"):
        routeCode = list.findtext("routeCode")
        return routeCode

AllServiceAreaReader('경부선')
