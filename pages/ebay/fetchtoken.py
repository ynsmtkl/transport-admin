#!/usr/bin/env python3
from pages.ebaysdk.trading import Connection
from ebaytrading import settings
api = Connection(config_file=None, appid="YounessM-tutordev-SBX-579658d5d-811712f2", certid="SBX-79658d5d9ed8-e598-4c67-a24f-10ef", devid="42a4f464-e24f-4fbb-928e-6ab66f7aaa6e", token="AgAAAA**AQAAAA**aAAAAA**IGSfXA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4aiCJmHowqdj6x9nY+seQ**bfMEAA**AAMAAA**DT5omO/XPO8OWCTEfTjXVCmRSaZVTkE+gZWD1ASxB6zLtB9SEWasWSrDuhj4We2m8YNTOqkH0qtFURWBxHHgfdLgRFax0AdWg34WUNAAtPem9OP35QiC4mmzWCOVOnqFB0qEqQhHTedbHTFifwD+GluznrSh6mfzVqKiMsvL8rKw3t9LAZwfUz0JGLmzNc+DnpDrm7+1yVWrZhb07eS/JELB+VApuZxOaNBQB7orB2pQpIUWOKMUAApMJe17cT6jLFdHzaGxBVRlYYnQL5TDc4LZun0Yc+To5AzODdPRjth8GbWettLQ22ikejjIvgKlGUnlvLGDEbkIaGESJw9l9BYvmLUStAfXlSoX5qdL4si2EbLrAkIp8WwWCvL8g4JwffMtPCf1HPfuqUHJfWlo00jbj6/0XvL5mAAqhRfxrQTIM3sJF/0BmZosy9ANB4D9PyaQZr4bsyXB7sRSEtcAaknM0HO8jvZJf8wrEfFNU0UYYw8xFUqxQkhCeIKn7m8+kthsVnLj+jMG1v+SHdcd3tyJD8U0tOyo4jiNU3Y8evunUDFAKwE9/pFRgSg/IgtHaKMTACis8aeuXfkybE5lzZlFqNiN8qYp22UCWEkvcdCqwREOCzIQpj0uSU4YmN1PdUZltO2i2R3fPZA7kBa5RbRZJaalHm4TeuyVPs3AjAOrxsHhXWD+J+kRTLh2ocWB+l+t0LQxTMz2GTVZ8jibMwrreU6tBsoDiZYov6Ek1g7IVdxh0U4cuwS0fsLed4yu", domain="api.sandbox.ebay.com", debug=True)


def get_session_id():
    request = {
        "RuName": settings.URNAME
    }

    return api.execute('GetSessionID', request).reply.SessionID


def get_token():
    session_id = get_session_id
    request = {
        "SessionID": session_id
    }
    response = api.execute('FetchToken', request)

    return response.reply.eBayAuthToken
