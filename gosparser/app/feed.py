import feedparser



def get_feed():
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1&OrderPlacementSmallBusinessSubject=on&OrderPlacementRnpData=on&OrderPlacementExecutionRequirement=on&orderPlacement94_0=0&orderPlacement94_1=0&orderPlacement94_2=0'
    feed = feedparser.parse(url)
    feed_entries = feed.entries
    entr = sorted(feed.entries, key=lambda x: x.published_parsed)
    ret = []
    for entry in entr:

        article_title = entry.title
        article_link = entry.link
        article_published_at = entry.published # Unicode string
        article_published_at_parsed = entry.published_parsed # Time object
        # article_author = entry.author  DOES NOT EXIST
        #content = entry.summary
        # article_tags = entry.tags  DOES NOT EXIST

        d = {
            'title': article_title,
            'link' : article_link,
            'author': entry.author,
            'published': entry.published,
            'published_parsed':entry.published_parsed,
            'summary': entry.summary
        }
        ret.append(d)
    return ret