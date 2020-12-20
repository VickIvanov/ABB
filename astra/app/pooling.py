from logger import get_logger
from settings import DOCKER_LIST
from store_requests import fetch
from migration import insert_supply,insert_organization
from urllib.parse import quote
import asyncio
import re
import os
import hashlib
from aiohttp import ClientSession, ClientResponseError

log = get_logger(__name__)


async def pooling_rss():
    while 1:
        log.info('Pooling RSS: by 1 hour')
        async with ClientSession() as session:
            for url in DOCKER_LIST:
                log.info('get:'+url)
                try:
                    data = await fetch(url+'feed', None, session)
                    if len(data) > 0:
                        await rss_proceed(data, url, session)

                except Exception as e:
                    log.error(e)
        await asyncio.sleep(60*60)

async def rss_proceed(feed, url, session):
    for f in feed:
        regNum = re.findall(r'\d{10,30}', f['link'])
        if len(regNum) == 1:
            regNum = regNum[0]
            fname = f'{regNum}.pkl'
            if os.path.isfile(fname):
                continue

            url_feed = f'{url}parse?regnum={regNum}'
            data = await fetch(url_feed, None, session)
            if len(data) > 2:
                #data = data.json()
                if 'error' not in data:
                    insert_supply(data)
                    url_org = quote(data['common']['org_url'])
                    url_org = f'{url}org?url={url_org}'
                    org = await fetch(url_feed, None, session)
                    insert_organization(org)
            await asyncio.sleep(1)