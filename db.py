from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
from xml.etree.ElementTree import parse
import xmltodict

# url 변경 부분
url = 'https://www.law.go.kr/DRF/lawSearch.do'
queryParams = '?' + urlencode(
    {quote_plus('OC'): 'm_6595',  # 사용자 이메일의 ID
     quote_plus('target'): 'prec',  # 서비스 대상 (판례 목록 = prec)
     quote_plus('type'): 'XML',  # 출력 형태 : HTML / XML
     quote_plus('display'): 100,  # 검색된 결과 개수 (default=20 max=100)
     quote_plus('page'): 1})  # 검색 결과 페이지 (default=1)
request = urllib.request.Request(url + unquote(queryParams))

response_body = urlopen(request).read()
decode_data = response_body.decode('utf-8')
print(decode_data)
