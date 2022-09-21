from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import sys
sys.path.append("c:\\users\\송민진\\appdata\\local\\programs\\python\\python39")
# import pymysql
# import requests
# from xml.etree.ElementTree import parse
#
#
# # MySQL Connection 연결
# conn = pymysql.connect(host='localhost', user='root', password='1234', db='', charset='utf8')
#
# # Connection으로부터 Cursor 생성
# curs = conn.cursor()
#
# xml 파일 저장하기 코드
def saveListXmlFile(target, totalCnt):

    # 데이터 취합을 위한 빈 문자열 생성
    final_data = ''

    # totalCnt까지 반복문 돌리기
    pages = totalCnt // 100 + 2
    for page in range(pages):
        # 변수로 url 변경하기
        url = 'https://www.law.go.kr/DRF/lawSearch.do'
        queryParams = '?' + urlencode(
            {quote_plus('OC'): 'm_6595',  # 사용자 이메일의 ID
             quote_plus('target'): target,  # 서비스 대상 (판례 목록 = prec)
             quote_plus('type'): 'XML',  # 출력 형태 : HTML / XML
             quote_plus('display'): '100',  # 검색된 결과 개수 (default=20 max=100)
             quote_plus('page'): page})  # 검색 결과 페이지 (default=1)

        # 웹사이트에서 받아온 xml 데이터 출력 테스트
        response = urlopen(url + unquote(queryParams)).read()
        data = response.decode('utf-8')
        print(data)

        # xml 파일 생성
        # xmlFile = f"H:\취업\#00. SW 개발\#03_Experiences & Study\#07_이노베이션 캠프 in 서울\#02_assignments\8주차_실습팀\project-data\precList\precListPage{page}.xml"
        xmlFile = f"H:\취업\#00. SW 개발\#03_Experiences & Study\#07_이노베이션 캠프 in 서울\#02_assignments\8주차_실습팀\project-data\lawList\lawListPage{page}.xml"
        f = open(xmlFile, "w", encoding='utf-8')
        f.write(data)
#
#         # SQL문 실행
#         sql = f"load xml local infile {xmlFile}" \
#               f"into table preclist" \
#               f"rows identified by '<prec>';"
#         curs.execute(sql)

def saveXmlFile(target, case_id):

    # 데이터 취합을 위한 빈 문자열 생성
    final_data = ''

    # 변수로 url 변경하기
    # url = 'https://www.law.go.kr/DRF/lawSearch.do'
    url = 'https://www.law.go.kr/DRF/lawService.do'
    queryParams = '?' + urlencode(
        {quote_plus('OC'): 'm_6595',  # 사용자 이메일의 ID
         quote_plus('target'): target,  # 서비스 대상 (판례 목록 = prec)
         quote_plus('ID'): case_id,  # 서비스 대상 (판례 목록 = prec)
         quote_plus('type'): 'XML'})  # 출력 형태 : HTML / XML

    # 웹사이트에서 받아온 xml 데이터 출력 테스트
    response = urlopen(url + unquote(queryParams)).read()
    data = response.decode('utf-8')
    print(data)

    # xml 파일 생성
    # xmlFile = f'H:\취업\#00. SW 개발\#03_Experiences & Study\#07_이노베이션 캠프 in 서울\#02_assignments\8주차_실습팀\project-data\precCases\precCase{case_id}.xml'
    xmlFile = f'H:\취업\#00. SW 개발\#03_Experiences & Study\#07_이노베이션 캠프 in 서울\#02_assignments\8주차_실습팀\project-data\statuteCases\statuteCase{case_id}.xml'
    f = open(xmlFile, "w", encoding='utf-8')
    f.write(data)

    # # SQL문 실행
    # sql = f"load xml local infile {xmlFile}" \
    #       f"into table preclist" \
    #       f"rows identified by '<prec>';"
    # curs.execute(sql)


# saveListXmlFile('prec', 131)
# saveListXmlFile('law', 131)
# saveXmlFile('prec', 221989)
saveXmlFile('law', '001790')
