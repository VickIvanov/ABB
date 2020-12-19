

import os, sys
sys.path.append('D:/projects/hack/genesis/astra/app')


from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from fastapi import FastAPI
#from .aiorequest import fetch
from aiohttp import ClientSession, ClientResponseError
#import feedparser
#from bs4 import BeautifulSoup
import glob
import json
from logger import get_logger
from models import SupplyModel, Supply, OrganizationModel
from database import init
from settings import  DB_URL, DB_UPDATE_SCHEMA

app = FastAPI()


@app.on_event("startup")
async def startup():
    #print(await SupplyModel.get(id=1))
    pass
    #await database.connect()


@app.on_event("shutdown")
async def shutdown():
    pass
    #await database.disconnect()


@app.get("/")
async def root():
    return {}


@app.get("/all")
async def all():
    o = await SupplyModel.all()
    ans = []
    for obj in o:
        obj.summary = json.loads(obj.summary)
    #return await Supply.from_queryset(SupplyModel.all())
    return o


@app.get("/org")
async def org():
    o = await OrganizationModel.all()
    return o


@app.get("/list")
async def order_list():
    #l = glob.glob("/home/adam/*.pkl")
    return {}


register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


