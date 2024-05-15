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

def NameServiceAreaReader(serviceArea_name):
    url = 'https://data.ex.co.kr/openapi/business/serviceAreaRoute?key=' + api_key + '&type=xml&routeName=' + ex_name + '&numOfRows=50&pageNo=1'
    # url = 'https://data.ex.co.kr/openapi/specialAnal/trafficFlowByTime?key=5758303589&type=xml&iStdYear=2024'
    # url 불러오기
    response = requests.get(url)
    pass
def ExNameServiceAreaReader(ex_name):
    pass

GasstationReader('죽암(서울)')
