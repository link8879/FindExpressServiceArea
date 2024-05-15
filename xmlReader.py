import requests
import xml.etree.ElementTree as ET
api_key = '5758303589'

# # url 입력
# url = 'https://data.ex.co.kr/openapi/business/serviceAreaRoute?key='+api_key+'&type=xml&routeName='+ex_name+'&numOfRows=50&pageNo=1'
# #url = 'https://data.ex.co.kr/openapi/specialAnal/trafficFlowByTime?key=5758303589&type=xml&iStdYear=2024'
# # url 불러오기
# response = requests.get(url)
#
# #데이터 값 출력해보기
# print(response.text)
# page_num = '1'
# while True:
#     url = 'https://data.ex.co.kr/openapi/business/serviceAreaRoute?key=' + api_key + '&type=xml&routeName=' + ex_name + '&numOfRows=10&pageNo='+ page_num
#     print(url)
#     response = requests.get(url)
#     root = ET.fromstring(response.text)
#
#     flag = root.find("list")
#
#     if flag == None:
#         break
#
#     for list in root.iter("list"):
#         print(list.findtext("brand"))
#     page_num = str(int(page_num) + 1)


def FoodMenuReader(serviceArea_name):
    page_num = '1'
    flag = False
    while True:
        url = 'https://data.ex.co.kr/openapi/restinfo/restBestfoodList?key=test&type=xml&numOfRows=10&pageNo='+page_num+'&stdRestNm='+serviceArea_name
    # url 불러오기
        response = requests.get(url)
        response = requests.get(url)
        root = ET.fromstring(response.text)
        flag = root.find("list")

        if flag == None:
            break
        for list in root.iter("list"):
            print(list.findtext("foodNm"))
        page_num = str(int(page_num)+1)



    pass
def GasstationReader(serviceArea_name):
    url = 'https://data.ex.co.kr/openapi/business/serviceAreaRoute?key=' + api_key + '&type=xml&routeName=' + ex_name + '&numOfRows=50&pageNo=1'
    # url = 'https://data.ex.co.kr/openapi/specialAnal/trafficFlowByTime?key=5758303589&type=xml&iStdYear=2024'
    # url 불러오기
    response = requests.get(url)
    pass
def NameServiceAreaReader(serviceArea_name):
    url = 'https://data.ex.co.kr/openapi/business/serviceAreaRoute?key=' + api_key + '&type=xml&routeName=' + ex_name + '&numOfRows=50&pageNo=1'
    # url = 'https://data.ex.co.kr/openapi/specialAnal/trafficFlowByTime?key=5758303589&type=xml&iStdYear=2024'
    # url 불러오기
    response = requests.get(url)
    pass
def ExNameServiceAreaReader(ex_name):
    pass

FoodMenuReader('죽암')
