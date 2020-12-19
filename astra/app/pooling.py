from logger import get_logger
from settings import DOCKER_LIST
import asyncio

log = get_logger(__name__)


async def pooling_rss():
    while 1:
        await asyncio.sleep(20)
        log.info('Pooling RSS: by 20 sec')
        for url in DOCKER_LIST:
            log.info('get:'+url)
