#!/usr/bin/env python3
from pages.ebaysdk.finding import Connection


def findbykeywords():
    api = Connection(appid="YounessM-tutordev-PRD-079703086-3fff9e70", config_file=None)

    request = {
        'keywords': 'educated',
        'itemFilters': [
            {'name': 'condition', 'value': 'new'}
        ],
        'paginationInput': {
            'entriesPerPage': 20,
            'pageNumber': 10
        },
        'sortOrder': 'PricePlusShippingLowest'
    }

    response = api.execute('findItemsByKeywords', request)

    items = {}
    i = 1
    for item in response.reply.searchResult.item:
        items[i] = {
            'Category': item.primaryCategory.categoryName,
            'Title': item.title,
            'URL': item.viewItemURL,
            'Price': item.sellingStatus.currentPrice.value,
        }
        i += 1
    return items
