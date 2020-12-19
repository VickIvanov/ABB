from .logger import get_logger
import asyncio

log = get_logger(__name__)


async def pooling_rss():
    while 1:
        log.info('Pooling RSS: by 5 sec')
        asyncio.sleep(5)