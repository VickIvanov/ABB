from logger import get_logger

import asyncio
import tortoise
from tortoise.exceptions import DBConnectionError


log = get_logger(__name__)



async def init(db_url, update_schema):
    while True:
        try:
            log.info(f'Tortoise-ORM: {tortoise.__version__}')
            await tortoise.Tortoise.init(
                db_url=db_url,
                modules={'models': ['models']},
                # _create_db=False if settings.APP_ENV is 'dev' else True,
                _create_db=False,
            )
            if update_schema:
                await tortoise.Tortoise.generate_schemas(safe=True)
            return
        except DBConnectionError as db_err:
            log.warning(db_err)
        await asyncio.sleep(5)