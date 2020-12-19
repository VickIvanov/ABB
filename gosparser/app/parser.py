from bs4 import BeautifulSoup
import requests
import time

def firstByClass(root, el='div', class_name=''):
    if root is None:
        return None
    content = root.find_all(el, class_=class_name)
    if len(content)>0:
        return content[0].text.strip().replace('\xa0','')
    return None

def firstByClassEl(root, el='div', class_name=''):
    if root is None:
        return None
    content = root.find_all(el, class_=class_name)
    if len(content)>0:
        return content[0]
    return None


def parse_ea44(content):
    soup = BeautifulSoup(content, features="html.parser")
    content = soup.find_all("div", class_="wrapper")[0]
    d = {}
    card = content.find_all("div", class_="cardMainInfo")
    if len(card) == 1:
        card = card[0]
    else:
        return d
    card = card.find_all("div", class_="sectionMainInfo")
    if len(card) < 2:
        return d
    d['purchaseLink'] = firstByClass(card[0], 'span', class_name='cardMainInfo__purchaseLink')
    d['state'] = firstByClass(card[0], 'span', class_name='cardMainInfo__state')
    d['content'] = firstByClass(card[0], 'span', class_name='cardMainInfo__content')

    org = card[0].find_all('div', class_='cardMainInfo__section')
    if len(org) > 1:
        org = firstByClassEl(org[1], 'span', class_name='cardMainInfo__content')
        if org is not None:
            d['org_url'] = org.a.attrs['href']
            d['org'] = org.a.text

    price = card[1].find_all('div', class_='price')[0]
    d['price'] = firstByClass(price, 'span', class_name='cardMainInfo__content')
    date = card[1].find_all('div', class_='date')[0]
    date = date.find_all('span', class_='cardMainInfo__content')
    if len(date) == 3:
        d['create_date'] = date[0].text.strip()
        d['update_date'] = date[1].text.strip()
        d['end_date'] = date[2].text.strip()

    blocks = content.find_all("div", class_="blockInfo")
    dd = {}
    for bl in blocks:
        sections = bl.find_all("section")
        for sc in sections:
            td = sc.find_all("span")
            if len(td) == 2:
                d[td[0].text.strip()] = td[1].text.strip().replace('\xa0', '').replace('\n', '')

    return d


def parse_ea44_result(content):
    soup = BeautifulSoup(content, features="html.parser" )
    content = soup.find_all("div", class_="wrapper")[0]
    d = {}

    tables = content.find_all('table')
    if len(tables) > 1:
        tbl = tables[1]
        th = tbl.find_all('th')
        result = []
        for r in tbl.find_all('tr'):
            res = {}
            for i, t in enumerate(r.find_all('td')):
                k = th[i].text.strip().replace('\n', '').replace('\xa0', '')
                k = " ".join(k.split())
                res[k] = t.text.strip().replace('\n', '').replace('\xa0', '')
            if len(res) > 0:
                result.append(res)
    d = result

    return d


def get_ea44(regNum='0815300003220000693'):
    for i in range(10):
        url = f'https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber={regNum}'
        data1 = requests.get(url, headers={'User-Agent': 'Custom'})
        if data1.status_code != 200:
            time.sleep(5)
            continue
    if data1.status_code == 200:
        result = {'common': parse_ea44(data1.content)}
        if result['common']['state'] == 'Определение поставщика завершено':
            for i in range(10):
                url = f'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber={regNum}'
                data2 = requests.get(url, headers={'User-Agent': 'Custom'})
                if data2.status_code != 200:
                    time.sleep(5)
                    continue
                result['result'] = parse_ea44_result(data2.content)
                return result
        else:
            return result

    return {'error': 'get data error'}