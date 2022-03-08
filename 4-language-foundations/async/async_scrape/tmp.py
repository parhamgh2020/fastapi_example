import datetime
from pprint import pprint
import re
import httpx
import asyncio

url = f'https://talkpython.fm/'

# resp = httpx.get(url)
# pprint(resp.status_code)


async def func(episode):
    global url
    url += f'/{episode}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp


asyncio.create_task()

if __name__ == '__main__':
    asyncio.run(main())
