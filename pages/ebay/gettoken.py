from urllib.request import Request, urlopen

if __name__ == '__main__':
    url = 'https://api.ebay.com/ws/api.dll'

    data = '''<?xml version="1.0" encoding="utf-8"?>
    <GetClientAlertsAuthTokenRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
    <eBayAuthToken>AgAAAA**AQAAAA**aAAAAA**A+qlXA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4aiCJmHowqdj6x9nY+seQ**bfMEAA**AAMAAA**DT5omO/XPO8OWCTEfTjXVCmRSaZVTkE+gZWD1ASxB6zLtB9SEWasWSrDuhj4We2m8YNTOqkH0qtFURWBxHHgfdLgRFax0AdWg34WUNAAtPem9OP35QiC4mmzWCOVOnqFB0qEqQhHTedbHTFifwD+GluznrSh6mfzVqKiMsvL8rKw3t9LAZwfUz0JGLmzNc+DnpDrm7+1yVWrZhb07eS/JELB+VApuZxOaNBQB7orB2pQpIUWOKMUAApMJe17cT6jLFdHzaGxBVRlYYnQL5TDc4LZun0Yc+To5AzODdPRjth8GbWettLQ22ikejjIvgKlGUnlvLGDEbkIaGESJw9l9BYvmLUStAfXlSoX5qdL4si2EbLrAkIp8WwWCvL8g4JwffMtPCf1HPfuqUHJfWlo00jbj6/0XvL5mAAqhRfxrQTIM3sJF/0BmZosy9ANB4D9PyaQZr4bsyXB7sRSEtcAaknM0HO8jvZJf8wrEfFNU0UYYw8xFUqxQkhCeIKn7m8+kthsVnLj+jMG1v+SHdcd3tyJD8U0tOyo4jiNU3Y8evunUDFAKwE9/pFRgSg/IgtHaKMTACis8aeuXfkybE5lzZlFqNiN8qYp22UCWEkvcdCqwREOCzIQpj0uSU4YmN1PdUZltO2i2R3fPZA7kBa5RbRZJaalHm4TeuyVPs3AjAOrxsHhXWD+J+kRTLh2ocWB+l+t0LQxTMz2GTVZ8jibMwrreU6tBsoDiZYov6Ek1g7IVdxh0U4cuwS0fsLed4yu</eBayAuthToken>
    </RequesterCredentials>
    <ErrorLanguage>en_US</ErrorLanguage>
    <WarningLevel>High</WarningLevel>
    </GetClientAlertsAuthTokenRequest>'''

    headers = {
        "Content-Type": "text/xml",
        "X-EBAY-API-COMPATIBILITY-LEVEL": 851,
        "X-EBAY-API-DEV-NAME": "42a4f464-e24f-4fbb-928e-6ab66f7aaa6e",
        "X-EBAY-API-APP-NAME": "YounessM-tutordev-SBX-579658d5d-811712f2",
        "X-EBAY-API-CERT-NAME": "SBX-79658d5d9ed8-e598-4c67-a24f-10ef",
        "X-EBAY-API-SITEID": 0,
        "X-EBAY-API-CALL-NAME": "GetClientAlertsAuthToken",
    }

    data = data.encode("utf-8")

    request = Request(url)
    request.add_header('User-Agent', headers)
    response = urlopen(request)
    content = response.read()

    #print(response)

