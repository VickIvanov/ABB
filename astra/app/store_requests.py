import asyncio
import os
from aiohttp import ClientSession, ClientResponseError
# from aiohttp_retry import RetryClient, RetryOptions


async def fetch(url, body, session):
    async with session.get(url,json=body) as response:
        if response.status not in (200, 429,):
            raise ClientResponseError()
        return await response.json()