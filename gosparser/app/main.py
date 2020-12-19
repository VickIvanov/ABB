
from fastapi import FastAPI
from .aiorequest import fetch
from .parser import get_ea44
from .feed import get_feed
from .orgparser import org_parser
from aiohttp import ClientSession, ClientResponseError
import feedparser
from bs4 import BeautifulSoup


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World "}


@app.get("/parse")
async def parse(regnum : str):
    return get_ea44(regnum)


@app.get("/feed")
async def feed():
    return get_feed()

@app.get("/org")
async def org(url :str):
    return org_parser(url)


@app.get("/parse2")
async def parse():
    return {'im':'parse2'}
