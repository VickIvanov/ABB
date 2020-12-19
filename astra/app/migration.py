import asyncio
from logger import get_logger
from settings import  DB_URL, DB_UPDATE_SCHEMA
from database import init
from models import SupplyModel, OrganizationModel
from datetime import datetime
import joblib
import json
import re

import os

log = get_logger(__name__)

def main(loop):
    log.info('Initialize db...')
    loop.run_until_complete(
        init(
            DB_URL,
            DB_UPDATE_SCHEMA,
        )
    )
    log.info('done db...')
    loop.run_until_complete(migrate_files())



async def migrate_files():
    import glob
    l = glob.glob('D:/projects/hack/genesis/research/orders/*.pkl')
    for f in l:
        refnum = os.path.basename(f)[:-4]
        data = joblib.load(f)
        await insert_supply(data)
        log.info(f'Ref num: {refnum}')
    l = glob.glob('D:/projects/hack/genesis/research/zakaz/*.pkl')
    for f in l:
        orgnum = os.path.basename(f)[:-4]
        data = joblib.load(f)
        await insert_organization(data)
        log.info(f'Org num: {orgnum}')


async def insert_supply(data):
    refnum = int(re.findall(r'\d{8,30}', data['common']['purchaseLink'])[0])
    sp = await SupplyModel.filter(id=refnum).first()
    if sp is None:
        sp = await SupplyModel.create(id=int(refnum))
    d = data['common']

    sp.status = d['state']
    sp.title = d['content']
    sp.org_name = d['org']
    sp.organization_id = re.findall(r'\d{8,30}', d['org_url'])[0]
    sp.refnum = refnum
    # sp.id = refnum
    sp.price = float(d['price'][:-1].strip().replace(',', '.'))

    if 'create_date' in d:
        sp.created_at = datetime.strptime(d['create_date'],'%d.%m.%Y')
    if 'update_date' in d:
        sp.modified_at = datetime.strptime(d['update_date'],'%d.%m.%Y')
    if 'end_date' in d:
        sp.end_at = datetime.strptime(d['end_date'],'%d.%m.%Y')
    sp.summary = json.dumps(d)

    if 'Идентификационный код закупки (ИКЗ)' in d:
        sp.iks = d['Идентификационный код закупки (ИКЗ)']

    if 'Требуется обеспечение исполнения контракта' in d:
        if d['Требуется обеспечение исполнения контракта'] == 'Да':
            sp.require = 1
            sp.credit = d['Размер обеспечения исполнения контракта']

    if 'result' in data:
        d = data['result']
        if len(d) > 0:
            d = d[0]
            sp.partner1_name = d['Участник(и), с которыми планируется заключить контракт']
            sp.partner1_type = d['Порядковый номер, полученный по результатам рассмотрения заявки']
            sp.partner1_price = d['Предложение участника, ₽']
        d = data['result']
        if len(d) > 1:
            d = d[1]
            sp.partner2_name = d['Участник(и), с которыми планируется заключить контракт']
            sp.partner2_type = d['Порядковый номер, полученный по результатам рассмотрения заявки']
            sp.partner2_price = d['Предложение участника, ₽']

    await sp.save()

async def insert_organization(data):
    orgcode = int(data['orgcode'])
    sp = await OrganizationModel.filter(id=orgcode).first()
    if sp is None:
        sp = await OrganizationModel.create(id=int(orgcode))
    sp.orgid = int(data['orgid'])
    sp.name = data['name']
    sp.inn = data['ИНН']
    sp.ogrn = data['ОГРН']
    sp.kpp = data['КПП']
    sp.address = data['Местонахождение']
    await sp.save()


if __name__ == '__main__':
    main(asyncio.get_event_loop())