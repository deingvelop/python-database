from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
from xml.etree.ElementTree import parse

# url 생성하기
url = 'https://www.law.go.kr/DRF/lawSearch.do'
queryParams = '?' + urlencode(
    {quote_plus('OC'): 'm_6595',  # 사용자 이메일의 ID
     quote_plus('target'): 'prec',  # 서비스 대상 (판례 목록 = prec)
     quote_plus('type'): 'XML',  # 출력 형태 : HTML / XML
     quote_plus('display'): 100,  # 검색된 결과 개수 (default=20 max=100)
     quote_plus('page'): 1})  # 검색 결과 페이지 (default=1)

# 웹사이트에서 받아온 xml 데이터 출력 테스트
response = urlopen(url + unquote(queryParams)).read()
data = response.decode('utf-8')
print(data)

# xml 파일 생성
xmlFile = "H:\취업\#00. SW 개발\#03_Experiences & Study\#07_이노베이션 캠프 in 서울\#02_assignments\8주차_실습팀\project-data\precList\dbtest.xml"
f = open(xmlFile, "w", encoding='utf-8')
f.write(data)
