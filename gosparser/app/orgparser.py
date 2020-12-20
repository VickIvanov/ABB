from bs4 import BeautifulSoup
import re
import requests



def parse_organisation(content, organizationCode):
    soup = BeautifulSoup(content)
    content = soup.find_all("div", class_="registry-entry__form")[0]
    sks = {}
    name = content.find_all('div',class_='registry-entry__header-mid__number')
    sks['name'] = name[0].text.strip()
    sks['orgid'] = re.findall(r'\d{4,30}',name[0].a.attrs['href'])[0]
    sks['orgcode'] = organizationCode[0]
    d = content.find_all('div', class_='registry-entry__body-block')
    k = d[0].find_all('div', class_='registry-entry__body-title')[0].text.strip()
    v = d[0].find_all('div', class_='registry-entry__body-value')[0].text.strip()
    sks[k] = v

    d = d[1].find_all('div', class_='col-4')
    for dd in d:
        k = dd.find_all('div', class_='registry-entry__body-title')[0].text.strip()
        v = dd.find_all('div', class_='registry-entry__body-value')[0].text.strip()
        sks[k] = v
    return sks


def org_parser(url):
    organizationCode = re.findall(r'\d{8,30}', url)
    data = requests.get(url, headers={'User-Agent': 'Custom'})
    if data.status_code==200:
        return parse_organisation(data.content, organizationCode)
    return None

